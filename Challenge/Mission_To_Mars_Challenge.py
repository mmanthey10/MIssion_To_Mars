# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()

# This cell will grab the image urls

#Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

html = browser.html
img_soup = soup(html, 'html.parser')

#-- Get hrefs and run for loop to create html list --------#
href_results = img_soup('a', class_='itemLink')
href_list = []
x = 0

for x in range(9):
    href = href_results[x].get('href')
    href_list.append(href)
    x =+ 1

final_href_list = [href_list[0], href_list[2], href_list[4], href_list[6]]
print(final_href_list)

#---For Loop creates url and scrapes for jpg image, appends to list--#

results_list = []
y = 0

for y in range(4):
    url1 = final_href_list[y]
    scrape_url = url + url1
    print(scrape_url)
    browser.visit(scrape_url)
    html = browser.html
    img_soup = soup(html, 'html.parser')
    jpg_result = img_soup.find('img', class_='wide-image').get('src')
    results_list.append(jpg_result)
    y =+1
        
#print(results_list)

#--- For loop to create final list for jpg urls----------------#
final_url_list = []
z = 0

for z in range(4):
    base = 'https://marshemispheres.com/'
    mid = final_href_list[z] + "/"
    end = results_list[z]
    final_url = base + end
    final_url_list.append(final_url)
    z =+ 1

# This Cell will grab the titles of the images

url = 'https://marshemispheres.com/'
browser.visit(url)

html = browser.html
img_soup = soup(html, 'html.parser')

results_titles = img_soup.find_all('h3')
results_titles

titles_list = []
a = 0

for a in range(4):
    title = results_titles[a].get_text()
    titles_list.append(title)
    a =+ 1

# This cell will create the dictionary holding both the image url and image title.
cer_hemi = {'image url': final_url_list[0],
            'title': titles_list[0],
}
sch_hemi = {'image url': final_url_list[1],
            'title': titles_list[1],
}
syr_hemi = {'image url': final_url_list[2],
            'title': titles_list[2],
}
val_hemi = {'image url': final_url_list[3],
            'title': titles_list[3],
}

hemisphere_dict = [cer_hemi, sch_hemi, syr_hemi, val_hemi]
print(hemisphere_dict)

# 5. Quit the browser
browser.quit()

