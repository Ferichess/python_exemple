import undetected_chromedriver as uc
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi undetected-chromedriver
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

# Buka halaman YouTube
driver.get("https://www.youtube.com")
time.sleep(5)  # Tunggu halaman YouTube untuk termuat

# Load cookies dari file JSON
with open("cookies.json", "r") as cookiesfile:
    cookies = json.load(cookiesfile)

# Perbaiki domain cookie dan tambahkan ke driver
for cookie in cookies:
    # Cetak cookie yang sedang ditambahkan untuk debugging
    print(f"Trying to add cookie: {cookie}")
    cookie["domain"] = ".youtube.com"  # Pastikan domainnya .youtube.com
    try:
        driver.add_cookie(cookie)
        print(f"Added cookie: {cookie['name']}")
    except Exception as e:
        print(f"Error adding cookie {cookie['name']}: {e}")

# Refresh halaman untuk menerapkan cookies
driver.refresh()

# Tunggu beberapa saat untuk memastikan login
time.sleep(10)

# Cek apakah elemen avatar YouTube muncul
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button#avatar-btn"))
    )
    print("Berhasil login ke YouTube!")
except Exception as e:
    print(f"Gagal login: {e}")

# Tutup browser setelah selesai
time.sleep(10)
driver.quit()
