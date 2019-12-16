import time


def test_login(driver):
    path = (
        "/hierarchy/android.widget.FrameLayout/"
        "android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.RelativeLayout/android.widget.RelativeLayout/"
        "android.widget.RelativeLayout/android.widget.RelativeLayout/"
        "android.widget.ScrollView/android.widget.LinearLayout/"
        "android.widget.RelativeLayout/android.widget.LinearLayout/"
        "android.widget.EditText"
    )
    driver.find_element_by_xpath(path).send_keys("7071119966")
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/customButton").click()
    driver.implicitly_wait(30)
    path2 = (
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
        "android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.FrameLayout/android.widget.RelativeLayout/"
        "android.widget.RelativeLayout/android.widget.RelativeLayout/"
        "android.widget.RelativeLayout/android.widget.ScrollView/"
        "android.widget.LinearLayout/android.widget.LinearLayout[1]/"
        "android.widget.RelativeLayout/android.widget.RelativeLayout/"
        "android.widget.LinearLayout/android.widget.LinearLayout/"
        "android.widget.EditText"
    )
    driver.find_element_by_xpath(path2).send_keys("123QWEasd")
    driver.find_element_by_id("kz.homecredit.ibank:id/customButton").click()
    time.sleep(7)


def test_scroll(driver):
    user_scroll = (
        'new UiScrollable(new UiSelector().scrollable(true).'
        'instance(0)).scrollIntoView(new UiSelector().'
        'text("Открыть текущий счет").instance(0))'
    )
    driver.find_element_by_android_uiautomator(user_scroll)
    time.sleep(5)
