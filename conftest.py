import pytest
from appium import webdriver
import os
# import time


@pytest.fixture(scope='session')
def driver():
    desired_cap = {}
    desired_cap["deviceName"] = "1283b2ca"
    desired_cap["platformName"] = "Android"
    desired_cap["app"] = os.path.abspath(
        os.path.abspath
        ("/home/nazira/test_new_project/hck-2.1.58_final.apk")
    )
    desired_cap["appPackage"] = "kz.homecredit.ibank"
    desired_cap["appActivity"] = (
        "cz.bsc.mb.activities.prelogin.SplashScreenActivity"
    )
    desired_cap["newCommandTimeout"] = 6000
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    return driver
    # driver.quit()
    # driver.set_page_load_timeout(6000)


# def main_page(driver):
# #     driver.
# def transfer(globals):
#     def back_transfer(driver):
#         driver.find_element_by_id(
#             "kz.homecredit.ibank:id/mnuTransfers").click()
#         time.sleep(5)
#     return back_transfer
