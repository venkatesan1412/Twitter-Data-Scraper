import snscrape.modules.twitter as tw
import pandas as pd
from pymongo import MongoClient
import streamlit as st
from IPython.display import display, FileLink

# Set page title and favicon
st.set_page_config(page_title='Twitter Scraper', page_icon=':bird:')

# Add title and description
st.title('Twitter Scraper')
st.write('This app scrapes tweets containing a given keyword within a specified date range.')

# Get input from user
keyword = st.text_input('Enter keyword to search for')
start_date = st.date_input('Enter start date')
end_date = st.date_input('Enter end date')
num_tweets = st.number_input('Enter number of tweets to scrape', value=100)
scrape_button = st.button('Scrape Tweets')


# Convert start and end dates to datetime objects
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

if start_date >= end_date:
    st.error('Error: Start date must be before end date.')
else:
    if scrape_button:
        # Define query string
        query = f'{keyword} since:{start_date.date()} until:{end_date.date()}'

        # Scrape tweets
        tweets = []
        for i, tweet in enumerate(tw.TwitterSearchScraper(query).get_items()):
            if i >= num_tweets:
                break
            tweets.append({
                'date': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
                'id': tweet.id,
                'url': tweet.url,
                'content': tweet.rawContent,
                'user': tweet.user.username,
                'reply_count': tweet.replyCount,
                'retweet_count': tweet.retweetCount,
                'language': tweet.lang,
                'source': tweet.sourceLabel,
                'like_count': tweet.likeCount
            })

        # Create dataframe from scraped data
        df = pd.DataFrame(tweets, columns=['date', 'id', 'url', 'content', 'user', 'reply_count', 'retweet_count', 'language', 'source', 'like_count'])

        # Show dataframe in output section
        st.write(df)

        # Ask user if they want to store data in MongoDB
        upload_to_mongodb = st.button('Upload data to MongoDB')

        if upload_to_mongodb:
            # Store data in MongoDB
            client = MongoClient('localhost', 27017)
            db = client['twitter_data']
            collection = db['scraped_data']
            collection.insert_one({
                'scraped_word': keyword,
                'scraped_date': f'{start_date.date().strftime("%Y-%m-%d")} to {end_date.date().strftime("%Y-%m-%d")}',
                'scraped_data': df.to_dict('records')
            })

            # Print success message
            st.success(f'{len(tweets)} tweets scraped and stored in MongoDB')

        # Provide download link to user
        download_format = st.selectbox('Select format to download', ('CSV', 'JSON'))

        if download_format == 'CSV':
            df.to_csv('scraped_data.csv', index=False)
            st.download_button(label='Download CSV', data='scraped_data.csv', file_name='scraped_data.csv')
        elif download_format == 'JSON':
            json = df.to_json(orient='records')
            st.download_button(label='Download JSON', data=json, file_name='scraped_data.json')
        else:
            st.error('Error: Invalid format selected. Please choose either CSV or JSON.')

