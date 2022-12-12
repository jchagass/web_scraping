from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Receber o site e executar no navegador

url = "https://www.google.com"
link = input("Digite o site: ")
driver = webdriver.Chrome(executable_path=r"C:\Users\Karaveia\Documents\chromedriver")



driver.get(url)
driver.maximize_window()


driver.find_element("name", "q").send_keys(link + Keys.RETURN)

driver.find_element(By.CSS_SELECTOR, ".yuRUbf a").click()

class getUrl():

    get_url = driver.current_url
    print ("sua url:", get_url, " \n")



res = requests.get(getUrl.get_url)
html_page = res.text

soup = BeautifulSoup(html_page, 'html.parser')
soup.prettify()


file = open("html.txt","w", encoding='utf-8')
file.write(html_page)
file.close()

sleep(2)
driver.quit()