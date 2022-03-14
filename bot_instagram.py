from selenium import webdriver
import time


navegador = webdriver.Chrome("chromedriver.exe")

navegador.get("https://www.instagram.com/")
time.sleep(2)


navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("xxxxxxx")

navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("xxxxxxx")

navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)


navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)

navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(3)


navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()
time.sleep(3)

navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("mickmesquita")
time.sleep(3)

navegador.find_element_by_class_name('-qQT3').click()
time.sleep(3)

navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div').click()
time.sleep(3)

navegador.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("xxxxxxx")
time.sleep(3)

navegador.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
