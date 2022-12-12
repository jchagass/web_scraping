from selenium import webdriver

#coletar a url atual

driver = webdriver.Chrome(executable_path=r"C:\Users\Karaveia\Documents\chromedriver")

class getUrl():

    get_url = driver.current_url
    print ("sua url:", get_url)