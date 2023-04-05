# Twitter Scraper

Twitter Scraper is a Python application that allows you to scrape tweets containing a specified keyword within a given date range. The scraped data can be displayed in a dataframe, uploaded to a MongoDB database, and downloaded in CSV or JSON format.

## Workflow

* The user inputs a keyword, start date, end date, and number of tweets to scrape in the Streamlit app.
* The app scrapes tweets containing the specified keyword within the given date range using the snscrape and pandas libraries.
* The scraped data is displayed in a dataframe in the Streamlit app.
* The user can choose to upload the data to a MongoDB database using the pymongo library.
* The user can choose to download the scraped data in CSV or JSON format.

## Execution

1. Clone the repository: `git clone https://github.com/venkatesan1412/twitter-scraper.git`
2. Install the required packages: 
    * `pip install snscrape`
    * `pip install pandas`
    * `pip install pymongo`
    * `pip install streamlit`
    * `pip install IPython`
3. Run the Streamlit app: `streamlit run twitterdatascraper.py`
4. Enter a keyword, start date, end date, and number of tweets to scrape in the Streamlit app.
5. Click the "Scrape Tweets" button to scrape tweets.
6. Click the "Upload data to MongoDB" button to upload data to a MongoDB database (optional).
7. Select a download format (CSV or JSON) and click the download button to download the scraped data.

Note: Before running the app, make sure to set up a MongoDB database and replace the client variable in the `if upload_to_mongodb` block with your own MongoDB client.

