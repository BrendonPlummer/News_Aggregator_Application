import requests
import os
import datetime

user_api = os.environ.get('FETCH_NEWS_API_KEY')

#Simple display function to output JSON data to console
def display(news_title, news_source, news_url):
    print("----------------------------------------------------------------------")
    print("Title: " + news_title)
    print("Source: " + news_source)
    print("URL: {0}".format(news_url))
    print("----------------------------------------------------------------------")

#Seperated from other functions for readability and ease of use, function takes API JSON and loops through and displays
def fetch_display(API_JSON):
    if(API_JSON['status'] == "ok"):
        total_results = len(API_JSON['articles'])
        for x in range(total_results - 1):
            news_title = API_JSON['articles'][x]['title']
            news_source = API_JSON['articles'][x]['source']['name']
            news_url = API_JSON['articles'][x]['url']
            display(news_title, news_source, news_url)
    else:
        error_message = API_JSON
        print("Failure to fetch data from API. Error: {0}".format(error_message))  

#Seperated each API call into seperate functions for readability
def fetchNews_TopHeadlines_Country(country, api_key): #Get the current top headlines for a country or category
    FETCHNEWS_TOPHEADLINES_COUNTRY_API_KEY = "https://newsapi.org/v2/top-headlines?country=" + country + "&apiKey=" + api_key
    fetchNews = requests.get(FETCHNEWS_TOPHEADLINES_COUNTRY_API_KEY).json()
    fetch_display(fetchNews)   
    
def fetchNews_TopHeadlines_Sources(source, api_key): #Headlines just from a specific source, for example BBC News
    FETCHNEWS_TOPHEADLINES_SOURCES_API_KEY = "https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=" + api_key
    fetchNews = requests.get(FETCHNEWS_TOPHEADLINES_SOURCES_API_KEY).json()
    fetch_display(fetchNews)    
    
def fetchNews_Everything_Source(source, api_key, date = datetime.date.today(),): #Search for news articles that mention a specific topic or keyword
    FETCHNEWS_EVERYTHING_SOURCE_API_KEY = "https://newsapi.org/v2/everything?q=" + source + "&from=" + date + "&sortBy=popularity&apiKey=" + api_key
    fetchNews = requests.get(FETCHNEWS_EVERYTHING_SOURCE_API_KEY).json()
    fetch_display(fetchNews)  
        

#Super rudimentry display, only tempory to ensure API works as expected
print("----------------------------------------------------------------------")
print("News for today in GB")   #Needs fancy title, use another param to have appropriate matching title
print("----------------------------------------------------------------------")

print("Options are: 1 = Top headlines in your country || 2 = Top headlines from a given source || 3 = Search for specific source or articles using keyword")
user_option = input("What news would you like today? ")

if(user_option == '1'):
    fetchNews_TopHeadlines_Country('gb', user_api)
elif(user_option == '2'):
    fetchNews_TopHeadlines_Sources('gb', user_api)
elif(user_option == '3'):
    fetchNews_Everything_Source('gb', user_api)
else:
    print("Error, wrong option provided.")
    
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")