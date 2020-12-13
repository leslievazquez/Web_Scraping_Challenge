<p align="center">
  <img width="1980" height="400" src="https://github.com/leslievazquez/Web_Scraping_Challenge/blob/main/Missions_to_Mars/images/mission_to_mars.png">
</p>

<h1 align ="center"><span>Web Scraping: Mars Data</span></h1>

The purpose of this project is to build a web application that scrapes four websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping
- Create a Jupyter Notebook file called `mission_to_mars.ipynb`. This file will be used to complete the web scraping and analysis tasks. 

### NASA Mars News
- Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the latest news' title and paragraph text. 

### JPL Mars Space Images - Featured Image
- Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
- Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
- Find the image url to the full size `.jpg` image.
- Save a complete url string for this image. 

### Mars Facts
- Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres
- Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
- Click each of the links to the hemispheres in order to find the image url to the full resolution image.
- Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
- Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
