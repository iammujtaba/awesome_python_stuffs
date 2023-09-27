# Importing necessary libraries
import requests                 # for handling requests to web pages
from bs4 import BeautifulSoup   # for scraping the web page content
import nltk                     # natural language toolkit, for text processing
from nltk.corpus import stopwords # for getting common words like 'the', 'and', 'in' etc. in English
from collections import Counter  # for counting occurrences of each distinct word

# Uncomment these lines if you are running this code for the first time. It will download necessary data for nltk.
# nltk.download("punkt") # downloads list of punctuation characters
# nltk.download("stopwords") # downloads list of common words ('the', 'and', 'is' etc.) in various languages

# Function to get page content using BeautifulSoup
def get_page_content(url):
    response = requests.get(url) # send a GET request to the url
    # check if request was successful
    if response.status_code != 200:
        print(f'Unable to get content from {url} received status code {response.status_code}')
        return None
    soup = BeautifulSoup(response.text, 'html.parser') # parse the page contents
    return soup.getText() # return only the text, omitting HTML tags and scripts

# Function to find common topics in the given text
def find_common_topics(text, num_topics = 3):
    stop_words = set(stopwords.words('english'))  # get the list of English stop words
    tokenized = nltk.word_tokenize(text)    # tokenize the text i.e., break it down into individual words
    cleaned_text = [word for word in tokenized if word.isalnum() and word not in stop_words] 
    # count the frequency of each word in the text (ignoring stop words)
    common_terms = Counter(cleaned_text).most_common(num_topics) 
    # return the 'num_topics' most common words
    return [term[0] for term in common_terms]

# Function to get common topics from a list of urls
def get_common_topics_from_url(urls:list=None, num_topics:int=3):
    # default value for the urls parameter is a list of three specified URLs
    urls = urls or ["http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster",
            "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/",
            "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"]
    # iterate through each URL in the list
    for url in urls:
        text = get_page_content(url) # get the text content of the page
        if not text:       # If unable to retrieve content, continue to the next URL 
            continue
        # call find_common_topics() to get the most common terms/topics in the page's text
        topics = find_common_topics(text,num_topics=num_topics)
        print(f'URL: {url}\nCommon Topics : {topics}') # print the results

get_common_topics_from_url(None,num_topics=10)

'''
DOCS:
To set up the collection of millions of URLs and make sure everything runs smoothly, we need a solid plan. Here's how we can do it:

Step 1: Distributed Setup

First off, we need a team of web crawlers. These are like our digital agents that go out and fetch web pages. We don't want just one; we need several of them working together. Tools like Apache Nutch or Scrapy can help us with that.

We'll also need a way to keep track of all the URLs we want to visit. Think of it like a to-do list for our crawlers. A message queue system, such as RabbitMQ or Apache Kafka, can help us manage this list.

Lastly, we've got to think about where we'll store all the data we collect. Consider using distributed options like Hadoop HDFS, Amazon S3, or NoSQL databases like Cassandra or MongoDB.

Step 2: Keeping Things Reliable

We can't afford to have things break down when we're dealing with millions of URLs. Here's how we ensure reliability:

Error Handling: Our crawlers need to be tough. They should handle issues like network errors or timeouts gracefully. If something goes wrong, we should give it another shot to avoid losing data.

Monitoring and Logs: We need to keep an eye on things. Good logging and monitoring systems will help us track what's happening and catch any problems early on.

Checkpoints: To be extra safe, let's save our progress from time to time. That way, if something crashes, we won't have to start from scratch.

Step 3: Making it Fast

Speed is the name of the game. We want to collect as many URLs as possible in the shortest time. Here's how we do it:

Parallelism: More crawlers mean more speed. We should run lots of them at the same time. But don't overdo it; we should adjust based on our available resources.

Prioritization: Not all URLs are equal. We should focus on the important ones first. For example, new content or high-traffic websites should get priority.

Rate Limiting: Let's not overwhelm the websites we're visiting. We should be polite and not request too much too quickly.

Caching: Save what we've already collected. That way, we don't have to fetch the same stuff over and over.

Step 4: Handling a Growing Load

As we gather more and more URLs, we need to be ready to scale up. Here's how we make it happen:

Add More Machines: If we need more power, just add more machines to the crawler team. We can even make it automatic with auto-scaling.

Load Balancing: We want to spread the work evenly. Load balancing helps distribute tasks fairly among our crawlers.

Data Storage: Our data storage should grow with us. Choose solutions that can expand horizontally as we collect more data.

That's the big picture. But we also need to think about processing the data, checking for duplicates, staying ethical, and staying secure. It's a complex operation, but with the right plan and continuous monitoring, we can make it work.
'''