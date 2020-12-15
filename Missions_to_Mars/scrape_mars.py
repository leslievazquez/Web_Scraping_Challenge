#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies 
import os 
import pymongo
import pandas as pd 
import requests
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Step 1: Scraping 

def scrape():
    
    mars_dict = {}
    
    # NASA Mars News
    # Open Browser
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)

    time.sleep(1) 
   
    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve the latest element that contains news title and news paragraph
    news_title = soup.find_all("div", class_ = "content_title")[1].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    
    # Print article info 
    print('news_title')
    print('news_p')
    
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p
    
    #--------------------
    
    #JPL Mars Space Images: Featured Image
    # Open Browser
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    
    time.sleep(1)
    
    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Navigate the site and find the image url for current Featured Mars Image 
    featured_image = soup.find("a",class_="button fancybox").get("data-fancybox-href")

    # Print addresss
    featured_image_url="https://www.jpl.nasa.gov"+featured_image
    print(featured_image_url)
    
    mars_dict["featured_image_url"] = featured_image_url

    #--------------------------------
    
    # Mars Facts
    # Open browser
    url3 = 'https://space-facts.com/mars/'
    browser.visit(url3)
    
    time.sleep(1)
    
    # Use Pandas to "read_html" to parse the URL
    table = pd.read_html(url3)

    # Use Pandas to "read_html" to parse the URL
    table = pd.read_html(url3)[0]

    # Convert table to html
    table = table.to_html(classes="table")
    print(table)
    
    mars_dict["table"] = table
    
    
    #---------------------------------------
    
    # Mars Hemispheres
    
    # Open Browser 
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    
    time.sleep(1)

    # Store the dictionary in a list
    hemi_list = []

    # for-loop for four hemispheres
    for i in range(4):
    
        # click on the html for the image - now at the next page
        browser.find_by_tag('h3')[i].click()
    
        # HTML Object 
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, "html.parser")
    
        # get image source link for full-resoultion photo
        image = soup.find('img', class_='wide-image')['src']
    
        # construct url from original page to full-resolution image photo
        img_url = 'https://astrogeology.usgs.gov' + image
        
        # find title of hemisphere photo at the photo page 
        title = soup.find('h2', class_= 'title').text
    
        # add the title and its corresponding image to a dictionary
        hemi_dict = {'Title': title, 'Image_URL': img_url}
    
        # append the dictionary to the list
        hemi_list.append(hemi_dict)
    
    # print the list of dictionaries
    for i in (hemi_list):
        print (i)
        
    print(hemi_list)
        
    mars_dict["hemi_list"] = hemi_list
    

    
    # Close the browser after scraping
    browser.quit()
    
    # Return results
    return mars_dict


# In[ ]:




