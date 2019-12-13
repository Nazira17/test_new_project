from appium import webdriver
import os
import time


desired_cap = {}
desired_cap["deviceName"] = "1283b2ca"
desired_cap["platformName"] = "Android"
desired_cap["app"] = os.path.abspath(
    os.path.abspath
    ("/home/nazira/test_project/hck-2.1.58_final.apk"))
desired_cap["appPackage"] = "kz.homecredit.ibank"
desired_cap["appActivity"] = "cz.bsc.mb.activities.prelogin.SplashScreenActivity"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
# driver.quit()
desired_cap["newCommandTimeout"] = 6000
# driver.set_page_load_timeout(6000)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText"
search_element = driver.find_element_by_xpath(path)
search_element.send_keys("7071119966")
button_send = driver.find_element_by_id("kz.homecredit.ibank:id/customButton")
button_send.click()
driver.implicitly_wait(30)
path2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText"
search_element_password = driver.find_element_by_xpath(path2)
search_element_password.send_keys("123QWEasd")
button_send = driver.find_element_by_id("kz.homecredit.ibank:id/customButton")
button_send.click()
time.sleep(10)
print(2)



user_scroll = 'new UiScrollable(new UiSelector().scrollable(true).' + 'instance(0)).scrollIntoView(new UiSelector().text("Открыть текущий счет").instance(0))'
user = driver.find_element_by_android_uiautomator(user_scroll)
