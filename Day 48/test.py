from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

# Keep Firefox browser open after program finishes
firefox_options = Options()
firefox_options.set_preference("detach", True)

# Create and configure the Firefox webdriver
driver = webdriver.Firefox(options=firefox_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes the browser
    # driver.quit()
    driver.close()


test_eight_components()
