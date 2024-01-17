import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "14.0",  # optional
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appPackage": "com.google.android.contacts",
        "appActivity": "com.google.android.apps.contacts.editor.ContactEditorActivity"
    }
}
OPTIONS = AppiumOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)

try:
    wait = WebDriverWait(driver, 10)
    phone_num = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.widget.EditText[@text="Phone" and @class="android.widget.EditText"]')
    ))
    phone_num.click()

    print(f"Keyboard is Shown: {driver.is_keyboard_shown()}")
    # driver.execute_script("mobile: isKeyboardShown")

    # 1 234 567 8900    ----   Phone Number
    driver.press_keycode(8)     # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_1
    driver.press_keycode(9)     # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_2
    driver.press_keycode(10)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_3
    driver.press_keycode(11)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_4
    driver.press_keycode(12)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_5
    driver.press_keycode(13)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_6
    driver.press_keycode(14)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_7
    driver.press_keycode(15)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_8
    driver.press_keycode(16)    # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_9
    driver.press_keycode(7)     # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_0
    driver.press_keycode(7)     # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_0

    driver.hide_keyboard()
    # driver.execute_script("mobile: hideKeyboard")

    print(f"Keyboard is Shown: {driver.is_keyboard_shown()}")
    # driver.execute_script("mobile: isKeyboardShown")

    save_btn = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.google.android.contacts:id/toolbar_button']")
    ))
    save_btn.click()

    saved_num = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.google.android.contacts:id/large_title']")
    ))
    assert "8900" in saved_num.text
    # assert "8900" in driver.page_source

    driver.long_press_keycode(24)  # 24 is the keycode for Volume Up
    time.sleep(1)   # for demo purposes only
    driver.long_press_keycode(25)  # 25 is the keycode for Volume Down

except Exception as e:
    print(f"Error: {e}")
finally:
    if driver:
        driver.quit()