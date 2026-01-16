from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from json import dump, load
from selenium.webdriver.common.keys import Keys
from asyncio import  Event
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
from time import sleep
from logging import info, warning, error
instagram_url = "https://www.instagram.com/"
class Selinum_driver:
    def __init__(self):
        self.stop_event = Event()
        warning("Starting server")
        __server = Server(".\\bmp\\bin\\browsermob-proxy.bat")
        __server.start()
        self.mob_client = __server.create_proxy(params={"trustAllServers": "true"})
        self.mob_client.new_har("instagram", options={"captureHeaders": True, "captureContent": True})
        options = webdriver.ChromeOptions()
        options.add_argument("--proxy-server={}".format(self.mob_client.proxy))
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-proxy-certificate-handler")
        options.add_argument("--disable-content-security-policy")
        options.add_argument("--headless=new")
        options.add_argument("--window-size=960,1080")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)
    def get_user_agent(self):
        return self.driver.execute_script("return navigator.userAgent;")
    def _login(self, username, password):
        self.driver.get(instagram_url + "accounts/login/")
        username_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        password_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open("cookies.json", "w") as file:
            dump(cookies, file, indent=4)
        info("Cookies saved successfully.")
    def load_cookies(self):
        try:
            with open("cookies.json", "r") as file:
                cookies = load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            info("Cookies loaded successfully.")
        except FileNotFoundError:
            info("No saved cookies found.")
    def check_login(self):
        self.driver.get(instagram_url)
        return bool(self.driver.get_cookie("sessionid"))
    def login(self, username=None, password=None):
        self.driver.get(instagram_url)
        self.load_cookies()
        if self.check_login():
            return
        if not (username and password):
            error("Username and password are required.")
            raise ValueError("Username and password are required.")
        try:
            self._login(username, password)
        except Exception as e:
            error(e)
            raise ValueError("Error in login, check your username and password, or the page is not loded correctly.")
        sleep(5)
        if self.check_login():
            self.save_cookies()
            return
        else:
            error("Login did not complete, check the info and the browser page.")
            raise ValueError("Login did not complete, check the info and the browser page.")