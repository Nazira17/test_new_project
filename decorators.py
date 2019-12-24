import time


def transfer(func):
    def wrapper(driver, *args, **kwargs):
        driver.find_element_by_id(
            "kz.homecredit.ibank:id/mnuTransfers").click()
        time.sleep(5)
        func(driver)
    return wrapper
