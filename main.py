from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# create webdriver object
browser = webdriver.Chrome()
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
profile_path = "/Users/gunjanrelan/Library/Application Support/Google/Chrome/Profile 10"
profile_name = "Profile 10"
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument(f"--profile-directory={profile_name}")
browser = webdriver.Chrome(service=service, options=options)


browser.get("https://www.swiggy.com")
sign_in_link = browser.find_element(By.CLASS_NAME, "_5-C04")
time.sleep(2)
sign_in_link.click()
time.sleep(2)
mobile_link = browser.find_element(By.XPATH, '//*[@id="mobile"]')
mobile_link.send_keys("8295939353")
log_in_link = browser.find_element(By.XPATH, '//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/form/div[2]/a')
log_in_link.submit()
otp_value = input("Enter OTP: ")
otp_link = browser.find_element(By.XPATH ,'//*[@id="otp"]')
otp_link.send_keys(otp_value)
time.sleep(5)
submit_link = browser.find_element(By.XPATH, '//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[2]/a')
submit_link.submit()



time.sleep(10)
