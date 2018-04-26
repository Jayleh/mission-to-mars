
# Troubleshooting scrape functions


```python
# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
import pymongo
```


```python
# def init_browser
def init_browser():
    # Chromedriver path
    executable_path = {'executable_path': 'webdriver/chromedriver.exe'}
    
    return Browser('chrome', **executable_path, headless=False)
```

# NASA Mars News


```python
with init_browser() as browser:
    
    # Mars exploration program url
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    
    # Maximize window
    browser.driver.maximize_window()
    
    # Latest news container
    news_container = browser.find_by_css('div[class="list_text"]').first
    
    # Grab news title
    news_title = news_container.find_by_css("a").text.strip()
    
    # Grab news title description
    news_p = news_container.find_by_css('div[class="article_teaser_body"]').text.strip()
    print(news_title)
    print(news_p)
```

    NASA Engineers Dream Big with Small Spacecraft
    The first CubeSat mission to deep space will launch in May.
    

# JPL Mars Space Images - Featured Image


```python
# Creat browser instance with context manager
with init_browser() as browser:
    
    # Visit JPL Mars space images url
    mars_imgs_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_imgs_url)
    
    # Maximize window
    browser.driver.maximize_window()
    
    # Latest image container xpath and click
    browser.find_by_xpath("//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div").click()

    # Retrieve featured image url
    featured_img_url = browser.find_by_css('img[class="fancybox-image"]')["src"]
    print(featured_img_url)
```

    https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA22377_hires.jpg
    

# Mars Weather


```python
# Mars weather twitter account url
mars_weather_url = "https://twitter.com/marswxreport?lang=en"

# Retrieve page with the requests module
response = requests.get(mars_weather_url)

# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')
```


```python
# Retrieve all tweets
results = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
```


```python
# Grab latest Mars weather
for result in results:
    
    # Grab tweet
    mars_weather = result.get_text().strip()
    
    # Only get the first tweet that has Mars weather
    if mars_weather[:3] == "Sol":
        print(mars_weather)        
        break
```

    Sol 2026 (April 18, 2018), Sunny, high -6C/21F, low -73C/-99F, pressure at 7.19 hPa, daylight 05:26-17:21
    

# Mars Facts


```python
# Mars facts url
mars_facts_url = "https://space-facts.com/mars/"

# Read html to get tables
tables = pd.read_html(mars_facts_url)
tables
```




    [                      0                              1
     0  Equatorial Diameter:                       6,792 km
     1       Polar Diameter:                       6,752 km
     2                 Mass:  6.42 x 10^23 kg (10.7% Earth)
     3                Moons:            2 (Phobos & Deimos)
     4       Orbit Distance:       227,943,824 km (1.52 AU)
     5         Orbit Period:           687 days (1.9 years)
     6  Surface Temperature:                  -153 to 20 °C
     7         First Record:              2nd millennium BC
     8          Recorded By:           Egyptian astronomers]




```python
# Grab mars facts table and create df
df = tables[0]
df.columns = ["Description", "Value"]

# Set description as index
df = df.set_index(["Description"])
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Value</th>
    </tr>
    <tr>
      <th>Description</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Equatorial Diameter:</th>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>Polar Diameter:</th>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>Mass:</th>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>Moons:</th>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>Orbit Distance:</th>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>Orbit Period:</th>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>Surface Temperature:</th>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>First Record:</th>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>Recorded By:</th>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Convert to html string
html_table = df.to_html()

# Strip newlines
html_table = html_table.replace('\n', '')
html_table
```




    '<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Value</th>    </tr>    <tr>      <th>Description</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.42 x 10^23 kg (10.7% Earth)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.52 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-153 to 20 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'



# Mars Hemispheres


```python
# List to hold hemisphere titles and urls
hemisphere_image_urls = []

# Creat browser instance with context manager
with init_browser() as browser:
    
    # Visit Mars hemispheres url
    mars_hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemis_url)
    
    # Maximize window
    browser.driver.maximize_window()
    
    # Find all image thumbnail imgs for loop
    thumbnails = len(browser.find_by_css('img[class="thumb"]'))
    
    for i in range(thumbnails):
            
        # Click image thumbnail
        browser.find_by_css('img[class="thumb"]')[i].click()
        
        # Dictionary to hold image title and url
        hemis = {}
        
        # Retrieve image title and add to dicitonary
        title = browser.find_by_css('h2[class="title"]').first.text.strip()
        hemis["title"] = title
    
        # Retrieve full resolution image url and add to dicitonary
        img_url = browser.find_by_css('img[class="wide-image"]')["src"]
        hemis["image_url"] = img_url
        
        # Append dictionary to hemis image urls list
        hemisphere_image_urls.append(hemis)
        
        # Go back to mars hemis url
        browser.back()

print(hemisphere_image_urls)
```

    [{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]
    
