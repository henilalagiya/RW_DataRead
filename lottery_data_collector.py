import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--new-instance')
chrome_options.add_argument('--user-data-dir=/tmp/chrome-profile')
driver = webdriver.Chrome(options=chrome_options)
time.sleep(1)


driver.get('https://www.royalwin1.com/lottery-bet/SELF_MONEY_TREE')

time.sleep(3)

last_draw_number = driver.find_element(
    By.XPATH, "//*[@id='root']/div/div[4]/div[1]/div/div/div[1]/div[2]/p[1]/span[2]/em")

time.sleep(2)

last_result = driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[4]/div[1]/div/div/div[1]/div[2]/p[2]/span[7]")

time.sleep(1)

time.sleep(1)
if int(last_result.text) > 10:
    actualValue_largeSmall = 'LARGE'
else:
    actualValue_largeSmall = 'SMALL'

if (int(last_result.text) % 2) == 0:
    actualValue_oddEven = 'EVEN'
else:
    actualValue_oddEven = 'ODD'


file = open('17April2023MoneyTree.txt', mode='a')
file.write("\n" + str(last_draw_number.text) + " " + str(last_result.text) + " - " + actualValue_largeSmall + " " + actualValue_oddEven )
file.close()


driver.get('https://www.royalwin1.com/lottery-bet/SELF_STAIR')   

time.sleep(3)

last_draw_number = driver.find_element(
    By.XPATH, "//*[@id='root']/div/div[4]/div[1]/div/div/div[1]/div[2]/p[1]/span[2]/em")

time.sleep(2)


last_result_AB = driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[4]/div[1]/div/div/div[1]/div[2]/p[2]/span[1]")
        
time.sleep(1)

last_result_CD = driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[4]/div[1]/div/div/div[1]/div[2]/p[2]/span[2]")
        
time.sleep(1)

file = open('17April2023Ladder.txt', mode='a')
file.write("\n" + str(last_draw_number.text) + " - " + str(last_result_AB.text) + " " + str(last_result_CD.text))
file.close()
