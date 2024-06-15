from appium import webdriver
import appium
from appium.webdriver.common.appiumby import AppiumBy
import io

# Set up Appium configuration for the mobile device
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": ".....",  #adb devices after enable developper options
    "appPackage": ".....",   
    "appActivity": ".....",
    "automationName": "UiAutomator2"
}

# Initialize the Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


#Steps to get the screen where your element to capture exists



#screenshot of element
element = driver.find_element(AppiumBy.XPATH, '.....')  #use appium inspector to locate the element  #xpath or id 
element.screenshot("elementScreenshot.png")


