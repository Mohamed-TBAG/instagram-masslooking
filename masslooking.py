import asyncio
import time
from requests import Session
from re import findall
from random import randint, uniform, choice
from json import dumps as json_dumps
from datetime import datetime, timedelta
from sqlite3 import connect, IntegrityError
from sys import exit
from logging import info as LogInfo, error as LogError
from utils import *
conn = connect(DB_LOCATION)
c = conn.cursor()
c.execute(CREATE_TABLE1_Q)
conn.commit()
c.execute(CREATE_TABLE2_Q)
conn.commit()
c.execute(CREATE_TABLE3_Q)
conn.commit()
class masslooking:
    def __init__(self, driver, sele_class, user_agent):
        self.driver = driver
        self.sele_class = sele_class
        self.user_agent = user_agent
        self.requests = Session()
        self.start_time = time.time()
        self.stories_count = 0
        self.accounts_have_count = 0
        self.stories_grabs = 0
        self.errors = 0
        self.account_grabber_count = 0
        self.posts_grabber_count = 0
        self.comments_grabber_count = 0
        self.likes_grabber_count = 0
        self.grabbers = [self.users_grabber, self.likes_grabber, self.comments_grabber]#

    async def get_graph_data(self):
        try:
            query_dict = {}
            html = str(self.driver.page_source)
            try:
                av = findall(r'{"accessToken":"","actorID":"(.*?)",', html)[0]
                __hsi = findall(r'''qplTimingsServerJS",null,null,\["(.*?)",''', html)[0]
                fb_dtsg = findall(r',{"token":"(.*?)"},', html)[0]
                __spin_t = findall(r'","__spin_t":(.*?),', html)[0]
                lsd = findall(r'\["LSD",\[\],{"token":"(.*?)"}', html)[0]
                jazoest = findall(r'&jazoest=(.*?)",', html)[0]
                app_id = findall(r'"appId":"(.*?)"', html)[0]
                bloks_version = findall(r'"versioningID":"(.*?)"', html)[0]
                query_dict.update({'av': av, '__hsi': __hsi, 'fb_dtsg': fb_dtsg,
                '__spin_t': __spin_t, 'lsd': lsd, 'jazoest': jazoest, "X-Ig-App-Id": app_id, "bloks_version": bloks_version, 'server_timestamps': True})
            except IndexError as htmlerror:
                LogError(f'an query missing from html or the page is not correct\n{htmlerror}\n')
                raise IndexError("Failed to extract graph data from HTML. Instagram structure might have changed.")
            except Exception as e:
                LogError(f"Unexpected error in get_graph_data: {e}")
                raise e
            har_log:list = self.sele_class.mob_client.har["log"]["entries"]
            har_log.reverse()
            for entry in har_log:
                query = entry["request"]
                if (query["url"] != qraphql_url) or (query["method"] != "POST") or (not query.get("postData")):
                    continue
                try:
                    postData = query["postData"]["params"]
                except :
                    continue
                string_data = str(postData)
                fields = ["__dyn" in string_data , "__d" in string_data , "__csr" in string_data]
                if all(fields):
                    for dic in postData:
                        if dic["name"] not in allowed_params:
                            continue
                        query_dict.update({dic['name']: dic['value']})
                    break
            return query_dict
        except IndexError as graph_err:
            LogError(f'graph data error: {graph_err}')
            raise IndexError
        
    async def get_headers(self):
        cookies_string = ""
        Csrftoken = ''
        for coc in self.driver.get_cookies():
            if coc["name"] == "csrftoken":
                Csrftoken = coc["value"]
            cookies_string += (coc["name"]+"="+coc["value"]+"; ")
        cookies_string = cookies_string[:len(cookies_string)-2]
        self.headers1 = HEAD1
        self.headers1.update({
            "Cookie": cookies_string,
            "X-Csrftoken": Csrftoken,
            "user-agent": self.user_agent
            })
        self.headers2 = HEAD2
        self.headers2.update({
            "Cookie": cookies_string,
            "X-Csrftoken": Csrftoken,
            "User-Agent": self.user_agent
            })

    async def stories_grabber(self, headers, payload, ids_list):
        payload.update(GRABBER_PAYLOAD)
        payload['variables'] = json_dumps({"reel_ids_arr": ids_list})
        response = await asyncio.to_thread(self.requests.post, url=query_url, headers=headers, data=payload)
        self.stories_grabs += 1
        try:
            reels_list = response.json(
            )["data"]["xdt_api__v1__feed__reels_media"]["reels_media"]
        except Exception as xx:
            LogError(f"\nreels items request got an error : {xx}\n")
            LogError(f"response text : {response.text}")
            reels_list = False
        return reels_list

    async def users_grabber(self, user_id):
        ids = []
        c.execute(SELECT_MAXID_Q, (user_id,))
        result = c.fetchone()
        if result:
            max_id = result[0]
        else:
            max_id = 0
        LogInfo(f"grabber max_id = {max_id}")
        url = friendships_url.format(user_id, max_id)
        response = await asyncio.to_thread(self.requests.get, url=url, headers=self.headers1)
        self.account_grabber_count+=1
        try:
            page_size = response.json().get('page_size')
            max_id2 = response.json().get('next_max_id')
            if max_id2:
                c.execute(INSERT_MAXID_Q, (user_id, max_id2))
                conn.commit()
            elif page_size:
                if page_size == 0 or page_size == "0":
                    LogInfo("page size is 0, returning empty list")
                    return ids
                else:
                    if not str(max_id).isdigit():
                        size, oldmax = max_id.split("|")
                        size = int(size)
                        size+= page_size
                        max_id = f"{size}|{oldmax}"
                    else:
                        max_id = int(max_id)
                        max_id+= page_size
                        max_id = str(max_id)
                c.execute(INSERT_MAXID_Q, (user_id, max_id))
                conn.commit()
        except Exception as e:
            self.errors += 1
            LogError(f"Error in getting page_size: {e}")
            return []
        try:
            followers = response.json()['users']
            for user in followers:
                if user["is_private"]:
                    continue
                if user["latest_reel_media"] != 0:
                    ids.append(str(user['pk']))
        except Exception as e:
            self.errors+=1
            LogError(f"grabber error = {e}\nresponse is : {response.text}")
        return ids
    
    async def posts_grabber(self, user_id):
        await self.get_headers()
        payload = await self.get_graph_data()
        payload.update(POSTS_GRABBER_PAYLOAD)
        user_name = accouts_with_usernames.get(str(user_id))
        self.headers2.update(
            {"X-Ig-App-Id": payload["X-Ig-App-Id"],
            "X-Fb-Lsd": payload["lsd"],
            "x-bloks-version-id": payload["bloks_version"],
            "Referer": instagram_url+user_name+"/",
            "X-Fb-Friendly-Name": "PolarisProfilePostsQuery",
            "X-Root-Field-Name": "xdt_api__v1__feed__user_timeline_graphql_connection",
            })
        c.execute(SELECT_LAST_MAXID_Q, (user_id,))
        last_posts_max_id = c.fetchone()
        variables = POSTS_GRABBER_VARIABLES
        variables["username"] = user_name
        if last_posts_max_id:
            variables["after"] = last_posts_max_id[0]
        payload.update({"variables": json_dumps(variables)})
        response = await asyncio.to_thread(self.requests.post, url=query_url, headers=self.headers2, data=payload)
        self.posts_grabber_count+=1
        posts = response.json().get("data", {}).get("xdt_api__v1__feed__user_timeline_graphql_connection", {}).get("edges", [])
        for post in posts:
            shortcode = post["node"]["pk"]
            try:
                c.execute(INSERT_SHORT_CODE_Q, (user_id, shortcode))
                conn.commit()
            except IntegrityError:
                LogError(f"Post with shortcode {shortcode} already exists for user {user_id}")
        end_cursor = response.json().get("data", {}).get("xdt_api__v1__feed__user_timeline_graphql_connection", {}).get("page_info", {}).get("end_cursor")
        c.execute(INSERT_MAXID2_Q, (user_id, end_cursor))
        conn.commit()
        LogInfo(f"12 posts scraped for user {user_id}")
        return

    async def likes_grabber(self, user_id):
        c.execute(SELECT_POST2_Q, (user_id,))
        shortcode = c.fetchone()
        if not shortcode:
            try:
                LogInfo(f"no posts grabbed for user {user_id}, grabbing now")
                await self.posts_grabber(user_id) 
                await asyncio.sleep(FACTOR*uniform(0.4, 0.8))
                return await self.likes_grabber(user_id)
            except Exception as PostsGrabberExeption:
                self.errors += 1
                LogError(f"AN ERROR in posts grabbing from likes func : {PostsGrabberExeption}")
                return []
        else:
            try:
                users_ids = []
                shortcode = shortcode[0]
                response = await asyncio.to_thread(self.requests.get, url=likers_url.format(shortcode), headers=self.headers2)
                self.likes_grabber_count += 1
                for user in response.json().get("users", []):
                    if user["is_private"]:continue
                    if user["latest_reel_media"] == 0:continue
                    users_ids.append(str(user["pk"]))
            except Exception as LikesGrabber:
                LogError(f"Error in grabbing likes for user {user_id} and shortcode {shortcode}: {LikesGrabber}")
                self.errors += 1
                return
            LogInfo(f"likes grabbed for user {user_id} count {len(users_ids)}")
            c.execute(SET_LIKES_SCRAPED, (user_id,shortcode))
            conn.commit()
            await asyncio.sleep(FACTOR*uniform(1, 2.2))
            return users_ids

    async def comments_grabber(self, user_id):
        c.execute(SELECT_POST_Q, (user_id,))
        shortcode = c.fetchone()
        if not shortcode:
            try:
                LogInfo("no posts grabbed for user grabbing now")
                await self.posts_grabber(user_id) 
                return await self.comments_grabber(user_id)
            except Exception as PostsGrabberExeption:
                self.errors += 1
                LogError(f"AN ERROR in posts grabbing : {PostsGrabberExeption}")
                return []
        else:
            users_ids = []
            shortcode = shortcode[0]
            url = comments_url.format(shortcode)
            min_id = ""
            try:
                for _ in range(1, randint(2, 4)):
                    response = await asyncio.to_thread(self.requests.get, url=url + f"&min_id={min_id}", headers=self.headers2)
                    self.comments_grabber_count += 1
                    comments = response.json().get("comments", [])
                    for comment in comments:
                        if comment["user"]["is_private"]:
                            continue
                        if comment["user"]["latest_reel_media"] == 0:
                            continue
                        users_ids.append(str(comment["user"]["pk"]))
                    min_id = response.json().get("next_min_id")
                    if not min_id:
                        # with open("commentsresponse.txt", "w", encoding="utf8") as commentsresponse:
                        #     commentsresponse.write(response.text)
                        LogError("Could'nt find min_id, breaking the loop")
                        break
                    await asyncio.sleep(FACTOR*uniform(1, 2.2)) 
            except Exception as CommentsGrabber:
                LogError(f"Error in grabbing comments for user {user_id} and shortcode {shortcode}: {CommentsGrabber}")
                self.errors += 1
                return
            c.execute(SET_COMMENTS_SCRAPED, (user_id, shortcode))
            conn.commit()
            LogInfo(f"comments grabbed for user {user_id} count {len(users_ids)}")
            return users_ids

    async def run(self):
        self.accout_to_grab_from = choice(list(accouts_with_usernames.keys()))
        await self.get_headers()
        self.grabber = choice(self.grabbers)
        while self.errors<10:
            try:

                if self.sele_class.stop_event.is_set():
                    slp = randint(333, 444)
                    LogInfo(f"masslooking sleeps for {slp}")
                    time.sleep(FACTOR*slp)
                    self.accout_to_grab_from = choice(list(accouts_with_usernames.keys()))
                    LogInfo(f"grabbing from {self.accout_to_grab_from}")
                if choice(do_or_not[:3]):
                    self.accout_to_grab_from = choice(list(accouts_with_usernames.keys()))
                    LogInfo(f"grabbing from {self.accout_to_grab_from}")
                try:
                    payload = await self.get_graph_data()
                except:
                    LogError("graph data at exeption of 'get_graph_data' error")
                    self.errors+=1
                    await asyncio.to_thread(self.driver.get, instagram_url)
                    continue
                account_grabbed = []
                while len(account_grabbed)<18 and self.errors<10:
                    grabber_response = await self.grabber(self.accout_to_grab_from)
                    await asyncio.sleep(FACTOR*uniform(1, 2)) 
                    if grabber_response:
                        account_grabbed.extend(grabber_response)
                if self.errors>10:
                    LogError("\nErrors are more than 10, exiting\n")
                    exit(0)
                try:
                    users_file = open(USERS_TXT_LOCATION, "a+")
                    for idd in account_grabbed:
                        users_file.write(str(idd) + "\n")
                    users_file.close()
                except:
                    LogError("error in writing users to file")
                    pass
                LogInfo(f"ids_list length = {len(account_grabbed)}")
                await self.get_headers()
                self.headers2.update(
                    {"X-Ig-App-Id": payload["X-Ig-App-Id"],
                    "X-Fb-Lsd": payload["lsd"],
                    "x-bloks-version-id": payload["bloks_version"]})
                payload.pop("bloks_version")
                payload.pop("X-Ig-App-Id")
                reel_ids = await self.stories_grabber(self.headers2, payload, account_grabbed)
                LogInfo(f"reel_ids edges length = {len(reel_ids)}")
                for edge in reel_ids:
                    self.accounts_have_count += 1
                    reelMediaOwnerId = edge["id"]
                    items = edge["items"]
                    if choice(do_or_not[:3]):
                        items.reverse()
                    if choice(do_or_not):
                        if choice(do_or_not):
                            continue
                    for j, item in enumerate(items):
                        await self.seen(item, payload, reelMediaOwnerId)
                        LogInfo(stats_output_message.format(timedelta(seconds=int(time.time()-self.start_time)), self.stories_count, self.accounts_have_count, self.stories_grabs, self.account_grabber_count, self.comments_grabber_count, self.likes_grabber_count, self.errors))
                        if (j >= 2) and choice([True, False]):
                            break
                LogInfo("grabber changing")
                self.grabber = choice(self.grabbers)
            except Exception as exp:
                LogError(f"masslooking function error = {exp}")
                self.errors += 1
                await asyncio.sleep(FACTOR*5)
                continue

    async def seen(self, item, payload, reelMediaOwnerId):
        payload.update(SEEN_PAYLOAD)
        payload.update({
            "variables":json_dumps({
                "reelId": f"{reelMediaOwnerId}",
                "reelMediaId": f"{item["pk"]}",
                "reelMediaOwnerId": f"{reelMediaOwnerId}",
                "reelMediaTakenAt": item["taken_at"],
                "viewSeenAt": int(datetime.now().timestamp())})})
        await asyncio.sleep(FACTOR*uniform(0.5, 1))
        response = await asyncio.to_thread(self.requests.post, url=query_url, headers=self.headers2, data=payload)
        await asyncio.sleep(FACTOR*uniform(2, 5))
        response_text = response.text
        if ('"status":"ok"' in response_text) and ('XDTEmptyRecord' in response_text) and ('xdt_api__v1__stories__reel__seen' in response_text):
            self.stories_count += 1
        else:
            self.errors += 1
            LogError(f"\nerror in eel__seen\n{response_text}\n")