from selenium import webdriver
import time

LOGIN_URL = 'https://auth.yell.com/sso/login?service=https%3A%2F%2Fwww.yell.com%2Freviews%2Fj_spring_cas_security_check'

# Login credentials
EMAIL = 'janedoe63244@gmail.com'
PASSWORD = 'at?c4a#$8_cALYT'

browser = webdriver.Firefox()

# Visit login page
browser.get(LOGIN_URL)

# Enter email and password
element = browser.find_element_by_id("username")
element.send_keys(EMAIL)
element = browser.find_element_by_id("password")
element.send_keys(PASSWORD)

# Wait for a second
time.sleep(1)

# Click login button
element = browser.find_element_by_id("login")
element.click()

time.sleep(1)

browser.get('https://www.yell.com/reviews/my')



