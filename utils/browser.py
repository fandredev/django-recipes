from selenium import webdriver


def make_chrome_browser(*options):
    import os

    instance_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            instance_options.add_argument(option)

    if os.environ.get("SELENIUM_HEADLESS") == "1":
        instance_options.add_argument("--headless")

    driver = webdriver.Chrome(options=instance_options)
    driver.implicitly_wait(0.5)
    return driver


if __name__ == "__main__":
    browser = make_chrome_browser("--headless")
    browser.get("http://www.google.com")
    browser.quit()
