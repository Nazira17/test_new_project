import pytest
from appium import webdriver
import os


@pytest.fixture
def data():
    desired_cap = {}
    desired_cap["deviceName"] = "1283b2ca"
    desired_cap["platformName"] = "Android"
    desired_cap["app"] = os.path.abspath(
        os.path.abspath
        ("/home/nazira/test_project/hck-2.1.58_final.apk"))
    desired_cap["appPackage"] = "kz.homecredit.ibank"
    appactivity_path = "cz.bsc.mb.activities.prelogin.SplashScreenActivity"
    desired_cap["appActivity"] = appactivity_path
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    # driver.quit()
    desired_cap["newCommandTimeout"] = 6000
    # driver.set_page_load_timeout(6000)
    return driver, desired_cap
