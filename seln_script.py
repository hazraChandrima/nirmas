# a python script that automatically takes screenshots of instagram profile and its posts(images only)
# with the help of Selenium Webdriver (Chromedriver)

import chromedriver_autoinstaller # this ensures that the version of chromedriver is compatible with that of chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
from colorama import init, Fore, Style
import time
import os

init()

def print_colored(text, color, bold=False):
    style = Style.BRIGHT if bold else ""
    print(f"{style}{color}{text}{Style.RESET_ALL}")


# Instagram credentials, asking input from user
USERNAME = input(f"{Fore.GREEN}Enter the instagram username of the account: {Style.RESET_ALL}")
PASSWORD = input(f"{Fore.GREEN}Enter the instagram password: {Style.RESET_ALL}")


chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)



# automated logging into instagram account
def login():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)

    if "Login" in driver.title:
        raise Exception("Login failed")



# saving all the screenshots in a folder named "./screenshots/"
def take_profile_screenshot(save_path):
    profile_url = f"https://www.instagram.com/{USERNAME}/"
    driver.get(profile_url)
    time.sleep(5)

    screenshot_path = os.path.join(save_path, "profile_screenshot.png")
    driver.save_screenshot(screenshot_path)
    print_colored(f"Profile screenshot saved to {screenshot_path}", Fore.LIGHTMAGENTA_EX)




# taking screenshots of all image posts
def take_post_screenshots(save_path):
    post_links = set()
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        posts = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
        for post in posts:
            post_links.add(post.get_attribute('href'))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    for index, post_url in enumerate(post_links):
        driver.get(post_url)
        time.sleep(3)
        screenshot_path = os.path.join(save_path, f"post_screenshot_{index + 1}.png")
        driver.save_screenshot(screenshot_path)
        print_colored(f"Screenshot taken for {post_url} saved to {screenshot_path}", Fore.LIGHTYELLOW_EX)




def main():
    print_colored("Instagram Posts Screenshot Capture Tool", Fore.CYAN, bold=True)
    print_colored("======================================", Fore.CYAN)

    login()

    save_path = "./screenshots"
    os.makedirs(save_path, exist_ok=True)

    take_profile_screenshot(save_path)
    take_post_screenshots(save_path)

    driver.quit()


if __name__ == "__main__":
    main()

