import time
from . decorators import transfer


@transfer
def test_transfer_between_owned(driver):
    # driver.find_element_by_id("kz.homecredit.ibank:id/mnuTransfers").click()
    # time.sleep(5)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Между своими счетами")'
    ).click()
    time.sleep(2)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Счет списания")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Текущий счет")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("На счёт")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Дебетная карта")'
    ).click()

    path = (
        '/hierarchy/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.view.ViewGroup/android.widget.FrameLayout/'
        'android.widget.RelativeLayout/android.widget.RelativeLayout/'
        'android.widget.ScrollView/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.LinearLayout[3]/android.widget.LinearLayout/'
        'android.widget.EditText'
    )
    driver.find_element_by_xpath(path).send_keys("50")
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/payButton"
    ).click()
    time.sleep(3)
    element = driver.find_element_by_id(
        'kz.homecredit.ibank:id/title')
    text = element.text
    assert text == "Транзакция успешно обработана"
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/button1"
    ).click()
    driver.find_element_by_accessibility_id(
        "Перейти вверх"
    ).click()


@transfer
def test_transfer_between_owned_deposit(driver):
    # driver.find_element_by_id("kz.homecredit.ibank:id/mnuTransfers").click()
    # time.sleep(5)
    print(1)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Между своими счетами")'
    ).click()
    time.sleep(2)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Счет списания")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Текущий счет")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("На счёт")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Депозит")'
    ).click()

    path = (
        '/hierarchy/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.view.ViewGroup/android.widget.FrameLayout/'
        'android.widget.RelativeLayout/android.widget.RelativeLayout/'
        'android.widget.ScrollView/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.LinearLayout[3]/android.widget.LinearLayout/'
        'android.widget.EditText'
    )
    driver.find_element_by_xpath(path).send_keys("50")
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/payButton"
    ).click()
    time.sleep(3)
    element = driver.find_element_by_id(
        'kz.homecredit.ibank:id/title')
    text = element.text
    assert text == "Транзакция успешно обработана"
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/button1"
    ).click()
    driver.find_element_by_accessibility_id(
        "Перейти вверх"
    ).click()


@transfer
def test_transfer_between_owned_deposit_to_account(driver):
    # driver.find_element_by_id("kz.homecredit.ibank:id/mnuTransfers").click()
    # time.sleep(5)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Между своими счетами")'
    ).click()
    time.sleep(2)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Счет списания")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Депозит")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("На счёт")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Текущий счет")'
    ).click()

    path = (
        '/hierarchy/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.view.ViewGroup/android.widget.FrameLayout/'
        'android.widget.RelativeLayout/android.widget.RelativeLayout/'
        'android.widget.ScrollView/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.LinearLayout[3]/android.widget.LinearLayout/'
        'android.widget.EditText'
    )
    driver.find_element_by_xpath(path).send_keys("50")
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/payButton"
    ).click()
    time.sleep(3)
    element = driver.find_element_by_id(
        'kz.homecredit.ibank:id/title')
    text = element.text
    assert text == "Транзакция успешно обработана"
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/button1"
    ).click()
    driver.find_element_by_accessibility_id(
        "Перейти вверх"
    ).click()


@transfer
def test_transfer_between_owned_deposit_to_cart(driver):
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Между своими счетами")'
    ).click()
    time.sleep(2)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Счет списания")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Депозит")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("На счёт")'
    ).click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("Дебетная карта")'
    ).click()

    path = (
        '/hierarchy/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.view.ViewGroup/android.widget.FrameLayout/'
        'android.widget.RelativeLayout/android.widget.RelativeLayout/'
        'android.widget.ScrollView/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.LinearLayout[3]/android.widget.LinearLayout/'
        'android.widget.EditText'
    )
    driver.find_element_by_xpath(path).send_keys("50")
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/payButton"
    ).click()
    time.sleep(3)
    element = driver.find_element_by_id(
        'kz.homecredit.ibank:id/title')
    text = element.text
    assert text == "Транзакция успешно обработана"
    driver.find_element_by_id(
        "kz.homecredit.ibank:id/button1"
    ).click()
    driver.find_element_by_accessibility_id(
        "Перейти вверх"
    ).click()
