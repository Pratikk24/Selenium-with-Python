from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://claim-portal-bajaj-dev.qa.i3systems.in/")

user_name=driver.find_element_by_name("username")
print(user_name.is_displayed())
print(user_name.is_enabled())


pwd_name=driver.find_element_by_name("password")
print(pwd_name.is_displayed())
print(pwd_name.is_enabled())

user_name.send_keys("admin")
pwd_name.send_keys("!3$y$+eMs")

login=driver.find_element_by_css_selector("input[value=LOGIN]")
login.click()
