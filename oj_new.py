from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path=r'C:\driver\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.ojcommerce.com/')
driver.implicitly_wait(10)
driver.execute_script('window.scrollTo(0,800)')
for i in range(1,12):
    try:
        # product=driver.find_element_by_xpath(f'//*[@id="homePage"]/section[2]/div/a['+str(i)+']/h4').text
        product=driver.find_element_by_xpath(f'//*[@id="homePage"]/section[2]/div/a[{i}]/h4').text
    except:
        product = driver.execute_script(f'return document.querySelector("#homePage > section.popCatHolder > div > a:nth-child({i}) > h4")').text
    print(product)
