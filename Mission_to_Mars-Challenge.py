#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


#driver=webdriver.chrome()
executable_path={'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup= soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


news_title=slide_elem.find('div', class_='content_title').get_text()
news_title


# In[6]:


news_p=slide_elem.find('div',class_='article_teaser_body').get_text()
news_p


# ###featured images

# In[7]:


url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


full_image_elem=browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[10]:


img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[11]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[12]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description','Mars','Earth']
df.set_index('description', inplace=True)
df


# In[13]:


df.to_html()


# ### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 
# Hemispheres

# In[14]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[15]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[16]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    
    hemispheres = {}
    
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[17]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[18]:


browser.quit()


# In[ ]:




