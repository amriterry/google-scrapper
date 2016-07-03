from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

def scrapeGoogle(query):
    driver_path = './drivers/phantomjs' # Use another driver for linux or windows os respectively
    url = 'https://www.google.com'

    browser = webdriver.PhantomJS(executable_path = driver_path) # Use another driver for linux or windows os respectively
    browser.get(url)

    element = browser.find_element_by_name('q')
    element.send_keys(query + " site:wikipedia.com")
    element.send_keys(Keys.RETURN)

    try:
        WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"g"))
        )

        results = browser.find_elements_by_class_name('g')

        if(results is not None):
            for result in results:
                result_link = result.find_element_by_tag_name('a')

                link = result_link.get_attribute("href")

                print(generateLink(result_link.text,link))

                break
        else:
            element.send_keys(query)
            element.send_keys(Keys.RETURN)

            try:
                WebDriverWait(browser,10).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"g"))
                )

                results = browser.find_elements_by_class_name('g')

                if(results is not None):
                    for i in range(0,3):
                        result_link = result.find_element_by_tag_name('a')

                        link = result_link.get_attribute("href")

                        print(generateLink(result_link.text,link))
                else:
                    printf("No results found")
            except TimeoutException:
                print("Connection timed out")
    except TimeoutException:
        print("Connection timed out")
    finally:
        browser.quit()

def generateLink(title,href):
    return "<a href=\""+href+"\">"+title+"</a>"

scrapeGoogle("Kathmandu University Boys Hostel")
