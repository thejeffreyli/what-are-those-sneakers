from selenium import webdriver
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io

# Resource: https://www.youtube.com/watch?v=7KhuEsq-I8o
# Resource: https://medium.com/@nithishreddy0627/a-beginners-guide-to-image-scraping-with-python-and-selenium-38ec419be5ff

# TODO: init driver on your local
driver_path = "./chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)

def scrape_images(query, num_images, save_path):
    '''
    Parameters
    ----------
    query : string
        DESCRIPTION.
    num_images : TYPE
        DESCRIPTION.
    save_path : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    '''
    
    # create a search query on Google images 
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"

    # open the Google Images search page using Selenium 
    driver.get(search_url)

    # scroll down to load more images
    for _ in range(num_images // 50):
        driver.execute_script("window.scrollBy(0,10000)")

    # wait for the images to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.Q4LuWd")))

    # get image elements
    img_elements = driver.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")

    if not os.path.exists(save_path):
        # make directory if it does not already exist 
        os.makedirs(save_path)

    # loop through the first num_images images
    for i, img_element in enumerate(img_elements[:num_images]):
        try:
            # click on each image to open it
            img_element.click()

            # Wait for the opened image to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.sFlh5c.pT0Scc.iPVvYb')))

            # get the URL of the image
            img_url_element = driver.find_element(By.CSS_SELECTOR, 'img.sFlh5c.pT0Scc.iPVvYb')
            img_url = img_url_element.get_attribute("src")

            img_content = requests.get(img_url).content
            # get the bytes IO of the image
            img_file = io.BytesIO(img_content)    
            
            # open image using Pillow
            image = Image.open(img_file)
             
            # issue with reading certain files
            # https://stackoverflow.com/questions/48248405/cannot-write-mode-rgba-as-jpeg
            if ('png' in img_url) or ('webp' in img_url):
                image = image.convert('RGB')    

            # save the image as a jpg
            img_name = f"{query}_{i+1}.jpg"
            img_path = os.path.join(save_path, img_name)
            with open(img_path, 'wb') as file:
                image.save(file)    
            print(f"Image {i+1} downloaded successfully")

        except Exception as e:
            pass
            # print(f"Failed to download image {i+1}: {str(e)}")

###############################################################################

# queries: stockx name, sku, ebay

query = "Jordan 1 Retro High Court Purple"
num_images = 300
save_path = "./images/555088-500"
scrape_images(query, num_images, save_path)

# close the browser
driver.quit()