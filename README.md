Twitter Scraper
This project is a simple Python application that scrapes tweets containing a specified keyword within a given date range. The scraped data can be displayed in a dataframe, uploaded to a MongoDB database, and downloaded in CSV or JSON format.

Workflow
The user inputs a keyword, start date, end date, and number of tweets to scrape in the Streamlit app.
The app scrapes tweets containing the specified keyword within the given date range using the snscrape and pandas libraries.
The scraped data is displayed in a dataframe in the Streamlit app.
The user can choose to upload the data to a MongoDB database using the pymongo library.
The user can choose to download the scraped data in CSV or JSON format.

Execution
Clone the repository: git clone https://github.com/venkatesan1412/twitter-scraper.git
Install the required packages:pip install snscrape
                              pip install pandas
                              pip install pymongo
                              pip install streamlit
                              pip install IPython
Run the Streamlit app: streamlit run twitterdatascraper.py
Enter a keyword, start date, end date, and number of tweets to scrape in the Streamlit app.
Click the "Scrape Tweets" button to scrape tweets.
Click the "Upload data to MongoDB" button to upload data to a MongoDB database (optional).
Select a download format (CSV or JSON) and click the download button to download the scraped data.
Note: Before running the app, make sure to set up a MongoDB database and replace the client variable in the if upload_to_mongodb block with your own MongoDB client.
