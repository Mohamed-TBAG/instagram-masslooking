import os,sys,logging
from requests import Session
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
logging.basicConfig(filename='masslooking.log', level=logging.INFO)
logger = logging.getLogger()
PATH = os.path.abspath(__file__) + r"\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = PATH
username_field_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_field_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
view_button_class_name = 'xy80clv'
next_button_class_name = "_ac0d"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--proxy-server=http://localhost:8080")
#chrome_options.add_argument("--allow-running-insecure-content")
close_button_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/section/div[3]/div'
driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=chrome_options) # on servers
wait = WebDriverWait(driver, 2)
driver.implicitly_wait(2)
user = "mohamedbrbro"
passw = "pp66778899"
session = '38830911865:dB6c644ZlhZD3B:8:AYde7KWEY7Q2eyqr-7r0v17HF7-BySTE8gGV2lVqVg'
stories_count = 1 # how mnay stories to watch per aCCOUNT
users_list = []
class FlushStreamHandler(logging.StreamHandler):
    def flush(self):
        sys.stdout.flush()
logger.addHandler(FlushStreamHandler(stream=sys.stdout))
class stories_masslooker:
    def __init__(self):
        self.stories_counter = 0
        self.accounts_counter = 0
        self.errors = 0
        self.r = Session()
        self.reels_media_url = "https://www.instagram.com/api/v1/feed/reels_media/?{}"
        self.strings = []
        with open("users.txt") as file:
            users = ["reel_ids="+u.strip()+"&" for u in file.readlines()]
            users_lists = [users[i:i+9] for i in range(0, len(users), 9)]
            file.close()
        for list_ids in users_lists:
            string="".join(i for i in list_ids)[:-1]
            self.strings.append(string)
    def login(self,username, password):
        driver.get("https://www.instagram.com/")
        cookie = {
            'domain': '.instagram.com',
            'httpOnly': True,
            'name': 'sessionid',
            'path': '/',
            'secure': True,
            'value': session}
        driver.add_cookie(cookie)
        driver.get("https://www.instagram.com/accounts/login/")
        try:
            self.cookies = {}
            for dictt in driver.get_cookies():
                self.cookies.update({dictt["name"]:dictt["value"]})
            if "sessionid" in str(driver.get_cookies()):
                csrf = self.cookies["csrftoken"]
                self.cookies = f"csrftoken={self.cookies['csrftoken']}; mid={self.cookies['mid']}; ig_did={self.cookies['ig_did']}; datr={self.cookies['datr']}; ig_nrcb=1; shbid={self.cookies['shbid']}; shbts={self.cookies['shbts']}; rur={self.cookies['rur']}; ds_user_id={self.cookies['ds_user_id']}; sessionid={self.cookies['sessionid']}"
                self.head = {
                    'accept': '*/*',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate',
                    'x-ig-app-id':'5607738976007515',
                    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                    'Cookie':self.cookies,
                    'x-csrftoken': csrf,
                    'origin':  'https://www.instagram.com',
                    'referer': f'https://www.instagram.com/'}
                input()
                return "logged_in"
            else:
                return "not_logged_in"
        except Exception as login_error:
            logger.error("unknown error in login : {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            return f"unknown error in login : {login_error}"
    def loggerr(self,typee,text):
        if typee == 'error':
            t = "{} : {} : counters : accounts = {} ; stories = {} ; errors = {}"
            logger.error(t.format(text,datetime.now().strftime("%Y-%m-%d %H:%M:%S") , mass_class.accounts_counter ,  mass_class.stories_counter , self.errors))
        elif typee == 'info':
            t = "{} : {} : counters : accounts = {} ; stories = {} ; errors = {}"
            logger.info (t.format(text,datetime.now().strftime("%Y-%m-%d %H:%M:%S") , mass_class.accounts_counter ,  mass_class.stories_counter , self.errors))
    def flusher(self):
        for handler in logger.handlers:
            handler.flush()
    def reels_request(self,st):
        try:
            self.items = self.r.get(url=self.reels_media_url.format(st),headers=self.head,data=st)
            if self.items.status_code == 200:return True
            return False
        except Exception as ItEr:
            print(ItEr);return False
    def watch_story(self,username,story_id):
        self.accounts_counter+=1
        stories_url = f"https://www.instagram.com/stories/{username}/{story_id}/"
        driver.get(stories_url)
        if "story" in str(driver.title) or "Stories" in str(driver.title):
            try:
                view_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, view_button_class_name)))
                view_button.click()
                sleep(1.2)
                self.loggerr("info","SEEN")
                return
            except:
                self.loggerr("error","view_button_not_found")
                return
            return
        return
    def stories_mass(self):
        for story_string in self.strings:
            get_stories = self.reels_request(story_string)
            if get_stories == False:
                self.errors+=1
                self.loggerr("error","story_request_faild")
                continue
            else:
                reels_data = self.items.json()["reels"]
                for user in reels_data:
                    user_username = reels_data[user]["user"]["username"]
                    items = list(reels_data[user]["items"])
                    for story in items[0:stories_count]:
                        self.watch_story(username=user_username,story_id=story["pk"])
mass_class = stories_masslooker()
login_func = mass_class.login(user, passw)
if login_func == 'logged_in':
    watching_func = mass_class.stories_mass()
else:
    print(login_func)
