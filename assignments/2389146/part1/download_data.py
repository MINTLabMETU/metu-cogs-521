import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
sources = ['https://www.bikeforums.net/road-cycling/470422-introduction-road-cycling-forum-references-newbie-questions-answered-here.html',
           'https://www.bikeforums.net/general-cycling-discussion/1094784-why-mountain-bikes-so-popular.html',
           'https://www.bikeforums.net/mountain-biking/1178636-27-5-dead.html',
           'https://www.bikeforums.net/mountain-biking/422-v-brakes-vs-cantilevers.html',
           'https://www.bikeforums.net/folding-bikes/83711-swift-folders.html',
           'https://www.bikeforums.net/folding-bikes/1051531-helix-update.html',
           'https://www.bikeforums.net/folding-bikes/122760-downtube-folding-bike.html',
           'https://www.bikeforums.net/folding-bikes/473415-birdy-thread.html',
           'https://www.bikeforums.net/mountain-biking/94609-chris-king-components-worth-cash.html',
           'https://www.bikeforums.net/mountain-biking/1191028-26ers.html',
           'https://www.bikeforums.net/folding-bikes/1061112-expanded-tern-recall.html']

last_height = 0
for i, source in enumerate(sources):
    print(source)
    driver.get(source)

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

    file = open(f'data/{i}.html', 'w')
    file.write(driver.page_source)
    file.close()

driver.close()