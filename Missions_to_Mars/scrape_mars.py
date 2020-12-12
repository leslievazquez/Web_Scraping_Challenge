#!/usr/bin/env python
# coding: utf-8

# # Step 1: Web Scraping 
# 

# In[5]:


# Import Dependencies 
import pandas as pd
import requests
import time
import pymongo
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
from selenium import webdriver


# In[6]:


def init_browser():
    # NOTE: Replace with your path to chromedriver
    executable_path = {"executable_path": "C:\Users\vazql\Desktop\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# ## NASA Mars News
# 
# * Scrape the NASA Mars News Site and collect the latest:
#     * News Title
#     * Paragraph Text 
# * Assign the text to variables that you can reference later.

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}


# In[7]:

def scrape():
    browser = init_browser()
    
    # Open Browser- Visit Nasa news url through splinter module
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    
      
    # In[11]:
    
    
    # HTML Object
    html = browser.html
    
    # Parse HTML Results with BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    
    
    # In[16]:
    
    
    # Scrape and collect the latest news title
    news_title = soup.find("div", class_ = "content_title").text
    
    #print(f"Latest News Title: {news_title}")
    
    
    # In[ ]:
    
    
    # Assign the news title to variable news_title
    #news_title = "Mars Now"
    
    
    # In[18]:
    
    
    # Retrieve the latest element that contains news paragraph
    news_p = soup.find("div", class_ = "article_teaser_body").text
    
    # Display scrapped data paragraph text
    #print(f"Paragraph:\n{news_p}")
    
    
    # In[19]:
    
    
    # Assign the news paragraph to variable news_p
   # news_p = "The symbols, mottos, and small objects added to the agency's newest Mars rover serve a variety of purposes, from functional to decorative."
    
    
    # ## JPL Mars Space Images - Featured Image
    # 
    # * Visit the url for JPL Featured Space Image [Here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    # 
    # * Use splinter to navigate the site & find the image url for the current Featured Mars Image 
    # * assign the url string to a variable called `featured_image_url`.
    # 
    # * Make sure to find the image url to the full size `.jpg` image.
    # 
    # * Make sure to save a complete url string for this image.
    
    # In[26]:
    
    
    # Open Browser - Visit Mars Space Images through splinter module
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    
    
    # In[27]:
    
    
    # Click 'Full Image' Button on main page
    browser.links.find_by_partial_text('FULL IMAGE').click()
    
    
    # In[28]:
    
    
    time.sleep(1)
    
    # Click 'more info' button to get to image page
    browser.links.find_by_partial_text('more info').click()
    
    
    # In[29]:
    
    
    # HTML Object
    html = browser.html
    
    # Parse HTML Results with BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    
    
    # In[30]:
    
    
    # Store results from image in new page to search for image source
    img_url = soup.select_one('figure.lede a img').get('src')
    img_url
    
    
    # In[31]:
    
    
    # Set a new variable to use base url
    base_url = 'https://www.jpl.nasa.gov'
    
    #Concatenate main_url & img_url to create an Absolute URL
    featured_image_url = (base_url + img_url)
    featured_image_url
    
    
    # In[32]:
    
    
    # Assign the url to variable featured_image_url
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18245_hires.jpg'
    
    
    # ### Featured Image:
    
    # <img src ='https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18245_hires.jpg'>
    
    # ## Mars Facts 
    # 
    # * Visit the Mars Facts webpage [Here](https://space-facts.com/mars/)
    # 
    # * Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # 
    # * Use Pandas to convert the data to a HTML table string.
    
    # In[36]:
    
    
    # Use Pandas to scrape data
    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)
    tables
    
    
    # In[37]:
    
    
    # Take first table for Mars Facts
    df = tables[0]
    df
    
    
    # In[38]:
    
    
    # Convert table to html
    mars_fact_table = df.to_html()
    
    mars_fact_table.replace('\n', '')
    
    
    # In[39]:
    
    
    df.to_html('mars_fact_table.html', index = False)
    
    
    # ## Mars Hemispheres
    # * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
    # 
    # * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # 
    # * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
    # 
    # * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    
    # In[40]:
    
    
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    
    
    # In[41]:
    
    
    # Get a list of All the Hemispheres
    links = browser.find_by_css("a.product-item h3")
    
    # Create empty list for hemispheres urls
    hemisphere_image_urls = []
    
    # Loop through the items 
    for x in range(len(links)):
    
        # Create empty dictionary to store the links
        hemisphere_dict = {}
    
        try: 
            # Find element on each loop to avoid a stale element exception
            browser.find_by_css("a.product-item h3")[x].click()
    
            # Assign the HTML content of the page to a variable & Parse HTML with BeautifulSoup
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            
            # Get Hemisphere Title
            hemisphere_dict["title"] = browser.find_by_css("h2.title").text
            
            # Get Hemisphere Image
            hemisphere_dict["img_url"] = browser.links.find_by_partial_text("Sample").first["href"]
    
    
            # Append the retrieved info into a list of dictionaries
            hemisphere_image_urls.append(hemisphere_dict)
    
            
            # Navigate Back to original page with all the hemispheres
            browser.back()
    
        except:
              print("Scraping Complete, Nothing Found")
                
    hemisphere_image_urls 
    
    
    # In[ ]:
    
    
    browser.quit()
    
    # Return results
    return(mars_data_dict)
    
    
