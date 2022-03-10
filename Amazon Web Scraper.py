import workbook as workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")


driver.maximize_window()
driver.get("https://www.amazon.fr")
driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[contains(@id, 'search')]").send_keys("Apple phones")
driver.find_element(By.XPATH, "//input[@value='Go']").click()
driver.find_element(By.XPATH, "//span[text()='Apple']").click()
phone_names = driver.find_elements(By.XPATH, "//span[contains(@class,' a-color-base a-text-normal')]")
prices = driver.find_elements(By.XPATH, "//span[contains(@class,'price-whole')]")

phone_list=[]
price_list=[]


for phone in phone_names:
    phone_list.append(phone.text)

print("*"*38)

for price in prices:
    price_list.append(price.text)

definitive_list = zip(phone_list, price_list)

print("Part 1")

wb=workbook()
wb['Sheet'].title= 'Apple Iphone Data'
sh1= wb.active
sh1.append(['Name', 'Price'])
for x in list(definitive_list):
    sh1.append(x)

wb.save("Final_records.xlsx")

print("Part 2")



