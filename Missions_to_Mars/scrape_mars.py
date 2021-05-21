import os
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

def scrape():

    #Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    mars = {}



    url = 'https://redplanetscience.com/'
    browser.visit(url)



    html = browser.html
    soup = bs(html, 'html.parser')


    # Create news title and paragraph variables
    news_title = soup.find('div', class_='content_title').text
    news_paragraph = soup.find('div', class_='article_teaser_body').text

    mars['news_title'] = news_title
    mars['news_paragraph'] = news_paragraph


    #Display lastest title and paragraph
    print(f'Latest Article: {news_title} \nDescription: {news_paragraph}')


    #URL for featured image
    url = 'https://spaceimages-mars.com'
    browser.visit(url)



    html = browser.html
    soup = bs(html, 'html.parser')



    #Scrape featured image
    image_url = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = print(f'https://spaceimages-mars.com/{image_url}')
    featured_image_url

    mars['featured_image_url'] = featured_image_url


    #Scraping Mars Facts

    #URL
    url = 'https://galaxyfacts-mars.com'
    all_about_mars = pd.read_html(url)
    all_about_mars


    type(all_about_mars)


    mars_facts = all_about_mars[0]
    mars_facts

    mars_facts = mars_facts.rename(columns=mars_facts.iloc[0]).drop(mars_facts.index[0])
    mars_facts


    mars_facts_table = mars_facts.rename(columns={'Mars - Earth Comparison': 'Facts'})
    mars_facts_table


    mars_table = mars_facts_table[['Facts','Mars']].reset_index(drop=True)
    mars_table



    mars_t_html = mars_table.to_html()
    mars['mars_t_html'] = mars_t_html


    # Scraping Mars Hemisphere Images and Titles

    #Cerberus Hemisphere
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_h1_title = soup.find('h2', class_='title').text

    mars_h1 = soup.find('img', class_='wide-image')['src']
    mars_h1_img = 'https://spaceimages-mars.com/' + mars_h1 



    #Schiaparelli Hemisphere
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_h2_title = soup.find('h2', class_='title').text

    mars_h2 = soup.find('img', class_='wide-image')['src']
    mars_h2_img = 'https://spaceimages-mars.com/' + mars_h2 



    #Syrtis Major Hemisphere
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_h3_title = soup.find('h2', class_='title').text

    mars_h3 = soup.find('img', class_='wide-image')['src']
    mars_h3_img = 'https://spaceimages-mars.com/' + mars_h3 



    #Valles Marineris Hemisphere
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    browser.links.find_by_partial_text('Valles Marineris Hemisphere').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_h4_title = soup.find('h2', class_='title').text

    mars_h4 = soup.find('img', class_='wide-image')['src']
    mars_h4_img = 'https://spaceimages-mars.com/' + mars_h4 



    mars_hemispheres_imgs = [
        {"title": mars_h1_title, "img_url": mars_h1_img},
        {"title": mars_h2_title, "img_url": mars_h2_img},
        {"title": mars_h3_title, "img_url": mars_h3_img},
        {"title": mars_h4_title, "img_url": mars_h4_img}]
    
    mars_hemispheres_imgs

    mars['hemispheres'] = mars_hemispheres_imgs


    #Close Browser
    browser.quit()



    return mars






