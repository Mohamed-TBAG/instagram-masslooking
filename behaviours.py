from asyncio import to_thread, sleep, create_task
from time import sleep as Tsleep
from random import randint, choice, uniform
from logging import info, INFO, basicConfig, error
from utils import FACTOR2
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

basicConfig(filename='masslooking.log', level=INFO, format='%(asctime)s - %(message)s')
BoolianChoices = [True, False, False, False, False, False,
             False, False, False, True, False, False, False]
random_hashtags = ["instagram", "women", "man", "memes", "anime",
                   "apple", "apple", "samsung", "jokes", "العراق", "السعودية",
                   "مصر", "usa", "realmadrid", "love", "food", "ميمز",
                   "سوريا", "gym", "اكسبلور", "تصميم", "cars", "لايك",
                   "viral", "fyp"]
random_accounts = [
    "realmadrid", "433", "sharqiyatv", "fhedan_s", "mzajeat", "wasted",
    "9gag", "koora_k", "brfootball", "kolaliraq", "themadridviews",
    "celebrities_iqmag", "bocoob", "ziyad.matti", "hard.images",
    "truthuncovered_", "uuub", "offdatmemes", "1001.stream", "naltaki1"]
next_button = "_aaqg"
first_post_classname = """_aagw"""
instagram_url = "https://www.instagram.com/"

def RandFloat(x,y):
    return FACTOR2*uniform(x, y)
def DoOrNot(start,end):
    return choice(BoolianChoices[start:end])
def MySleep(x, y):
    Tsleep(RandFloat(x, y))

class VirtualMouse:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def move_random(self):
        # Move to random position in viewport
        width = self.driver.execute_script("return window.innerWidth")
        height = self.driver.execute_script("return window.innerHeight")
        x = randint(0, width)
        y = randint(0, height)
        try:
            self.actions.move_by_offset(x, y).perform()
            # Reset offset to avoid accumulation errors or out of bounds
            self.actions.reset_actions()
        except:
            pass # Ignore movement errors

    def scroll(self, amount):
        self.driver.execute_script(f"window.scrollBy(0, {amount})")

    def click(self):
        try:
            self.actions.click().perform()
        except:
            pass

    def click_element(self, element):
        try:
            self.actions.move_to_element(element).click().perform()
        except:
            try:
                element.click()
            except:
                pass

class behaviour1:
    """open instagram home page and react with the posts there"""
    def __init__(self, sele):
        self.driver = sele.driver
        self.stop_event = sele.stop_event
        self.mouse = VirtualMouse(self.driver)

    async def mouse_move(self):
        if DoOrNot(0,3):
            await to_thread(self.mouse.move_random)
        if DoOrNot(0,3):
            size_to_scroll = randint(100, 1000)
            await to_thread(self.mouse.scroll, size_to_scroll)
            if size_to_scroll < 300:
                MySleep(0, 1.5)
            elif size_to_scroll > 300 < 600:
                MySleep(1.5, 5.5)
            else:
                MySleep(5.5, 9.2)
        if DoOrNot(0,3):
            # Try to find a like button and click it
            try:
                like_buttons = self.driver.find_elements(By.CSS_SELECTOR, "svg[aria-label='Like']")
                if like_buttons:
                    btn = choice(like_buttons)
                    await to_thread(self.mouse.click_element, btn)
            except:
                pass

    async def run(self):
        await to_thread(self.driver.get, instagram_url)
        while not self.stop_event.is_set():
            self.driver.switch_to.window(self.driver.window_handles[0])
            current_url = self.driver.current_url
            if instagram_url not in current_url:
                await to_thread(self.driver.get, instagram_url)
            await self.mouse_move()

class behaviour2:
    """open reels page and scroll it it"""
    def __init__(self, sele):
        self.driver = sele.driver
        self.stop_event = sele.stop_event
        self.mouse = VirtualMouse(self.driver)

    async def mouse_move(self):
        # scroll into next
        if DoOrNot(0,3):
            # Reels usually scroll by full height or arrow keys
            await to_thread(self.mouse.scroll, randint(100, 500))
            MySleep(0, 15.6)
        else:
            MySleep(0, 3.3)
        # random mouse movs
        if DoOrNot(0,3):
            await to_thread(self.mouse.move_random)
        
        # press like
        if DoOrNot(0,8):
            try:
                like_buttons = self.driver.find_elements(By.CSS_SELECTOR, "svg[aria-label='Like']")
                if like_buttons:
                    # Reels might have multiple, pick visible one
                    btn = like_buttons[0] 
                    await to_thread(self.mouse.click_element, btn)
            except:
                pass

    async def run(self):
        await to_thread(self.driver.get, instagram_url+"reels/")
        while not self.stop_event.is_set():
            self.driver.switch_to.window(self.driver.window_handles[0])
            current_url = self.driver.current_url
            if instagram_url not in current_url:
                await to_thread(self.driver.get, instagram_url+"reels/")
            await self.mouse_move()

class behaviour3:
    "search for a hashtag and scroll into its posts"
    def __init__(self, sele):
        self.driver = sele.driver
        self.stop_event = sele.stop_event
        self.mouse = VirtualMouse(self.driver)

    async def mouse_move(self):
        # random mouse move
        if DoOrNot(0,3):
            await to_thread(self.mouse.move_random)
        
        # like post
        if DoOrNot(0,8):
             try:
                like_buttons = self.driver.find_elements(By.CSS_SELECTOR, "svg[aria-label='Like']")
                if like_buttons:
                    btn = choice(like_buttons)
                    await to_thread(self.mouse.click_element, btn)
             except:
                pass

        # scroll
        if DoOrNot(0,3):
            size_to_scroll = randint(100, 1000)
            await to_thread(self.mouse.scroll, size_to_scroll)

        # go to next post (simulated by clicking first post then arrow keys usually, but here we just scroll)
        if DoOrNot(0,3):
             MySleep(1, 9.7)
             # Try to find next arrow if in modal
             try:
                 next_btns = self.driver.find_elements(By.CSS_SELECTOR, "svg[aria-label='Next']")
                 if next_btns:
                     await to_thread(self.mouse.click_element, next_btns[0])
             except:
                 pass
        else:
            MySleep(0, 4.8)

    async def run(self):
        hashtag = choice(random_hashtags)
        await to_thread(self.driver.get, instagram_url+"explore/search/keyword/?q=%23"+hashtag)
        await sleep(20)
        # Click first post to open modal
        try:
            posts = self.driver.find_elements(By.CLASS_NAME, "_aagw")
            if posts:
                await to_thread(self.mouse.click_element, posts[0])
        except:
            pass
        
        await sleep(5)
        while not self.stop_event.is_set():
            self.driver.switch_to.window(self.driver.window_handles[0])
            current_url = self.driver.current_url
            if instagram_url not in current_url:
                await to_thread(self.driver.get, instagram_url+"explore/search/keyword/?q=%23"+hashtag)
            await self.mouse_move()

class behaviour4:
    """open an account and scroll into its posts"""
    def __init__(self, sele):
        self.driver = sele.driver
        self.stop_event = sele.stop_event
        self.mouse = VirtualMouse(self.driver)

    async def mouse_move(self):
        # random mouse move
        if DoOrNot(0,3):
            await to_thread(self.mouse.move_random)
        
        # like
        if DoOrNot(0,5):
             try:
                like_buttons = self.driver.find_elements(By.CSS_SELECTOR, "svg[aria-label='Like']")
                if like_buttons:
                    btn = choice(like_buttons)
                    await to_thread(self.mouse.click_element, btn)
             except:
                pass

        if DoOrNot(0,3):
            size_to_scroll = randint(100, 1000)
            await to_thread(self.mouse.scroll, size_to_scroll)

        # go to next post
        if DoOrNot(0,3):
            MySleep(1, 9.6)
            try:
                 next_btns = self.driver.find_elements(By.CSS_SELECTOR, "svg[aria-label='Next']")
                 if next_btns:
                     await to_thread(self.mouse.click_element, next_btns[0])
            except:
                 pass
        else:
            MySleep(0, 4.3)

    async def run(self):
        account_to_react_with = await to_thread(choice, random_accounts)
        await to_thread(self.driver.get, instagram_url+account_to_react_with)
        await sleep(20)
        # Click first post
        try:
            posts = self.driver.find_elements(By.CLASS_NAME, "_aagw")
            if posts:
                await to_thread(self.mouse.click_element, posts[0])
        except:
            pass
        await sleep(5)
        while not self.stop_event.is_set():
            self.driver.switch_to.window(self.driver.window_handles[0])
            current_url = self.driver.current_url
            if instagram_url not in current_url:
                await to_thread(self.driver.get, instagram_url+account_to_react_with)
            await self.mouse_move()

class behaviours_selector:
    def __init__(self, sele_class):
        self.sele_class = sele_class
        self.counter = 0

    async def run(self):
        task1 = None
        task2 = None
        while True:
            # Window size is now handled by driver options
            if task1:
                task1.cancel()
            if task2:
                task2.cancel()
            bot = choice([behaviour1, behaviour2, behaviour3, behaviour4])
            bot = bot(self.sele_class)
            self.counter += 1
            time_to_change = randint(250, 350)
            info(f"time to change behaviour: {time_to_change}")
            task1 = create_task(bot.run())
            task2 = create_task(sleep(time_to_change))
            await task2
            if self.counter % 4 == 0:
                time_to_change = randint(300, 700)
                info(f"behaviours sleeps for {time_to_change}")
                self.sele_class.stop_event.set()
                await sleep(time_to_change)
                self.sele_class.stop_event.clear()