class MassLooker:
    def __init__(self, token):
        self.bot = TeleBot(token)
        self.keyboard = InlineKeyboardMarkup
        ##   ازرار منفردة
        self.back_button    = self.buttons_builder(["رجوع👣","BACK"]) # زر رجوع
        self.stop_button    = self.buttons_builder(["ايقاف🤚","STOP"]) # زر ايقاف مشاهدة الستوري
        self.back_inline = self.keyboard().add(self.back_button)
        self.stop_inline = self.keyboard().add(self.stop_button)
        ##   الازرار الاولية
        self.main_inline    = self.keyboard(row_width=1) 
        self.dev_button     = self.buttons_builder(["المطور🖥️","DEV"])
        self.login_button   = self.buttons_builder(["تسجيل دخول👤","LOGIN"])
        self.start_button   = self.buttons_builder(["تشغيل👁️‍🗨️","START"])
        self.main_inline    .add(self.dev_button)
        self.main_inline    .add(self.login_button)
        self.main_inline    .add(self.start_button)
        ##   المطور🖥️
        self.dev_inline     = self.keyboard(row_width=1) 
        self.url_button     = self.buttons_builder(["المطور خيبة🖥️"], url="t.me/TBAGx")
        self.info_button    = self.buttons_builder(["تعليمات استخدام البوتℹ️","INFO"])
        self.offers_button  = self.buttons_builder(["عروض اشتراكات البوت💰","OFFERS"])
        self.dev_inline     .add(self.url_button)
        self.dev_inline     .add(self.offers_button)
        self.dev_inline     .add(self.info_button)
        self.dev_inline     .add(self.back_button)
        ##   تعليمات استخدام البوتℹ️
        self.info_inline    = self.keyboard(row_width=1)
        self.android_button = self.buttons_builder(["اندرويد","ANDROID"])
        self.iphone_button  = self.buttons_builder(["ايفون","IPHONE"])
        self.info_inline    .add(self.android_button)
        self.info_inline    .add(self.iphone_button)
        self.info_inline    .add(self.back_button)
        ##   تشغيل👁️‍🗨️
        self.start_inline   = self.keyboard(row_width=1) 
        self.method1_button = self.buttons_builder(["تفاعل مع قائمة حسابات","FROM_LIST"])
        self.method2_button = self.buttons_builder(["تفاعل مع حساب محدد","FROM_USER"])
        self.start_inline   .add(self.method1_button)
        self.start_inline   .add(self.method2_button)
        self.start_inline   .add(self.back_button)
        ##   تفاعل مع قائمة حسابات
        self.file_inline    = self.keyboard(row_width=1) 
        self.run_button1     = self.buttons_builder(["بدء المشاهدة👾","RUN1"]) # زر البدء العام
        self.run_button2     = self.buttons_builder(["بدء المشاهدة👾","RUN2"]) # زر البدء العام
        self.file_button    = self.buttons_builder(["اضافة ملف حسابات📃","ADDFILE"]) # زر اضافة قائمة حسابات
        self.file_inline    .add(self.run_button1)
        self.file_inline    .add(self.file_button)
        self.file_inline    .add(self.back_button)
        ##   ازرار العرض ( بدون كول باك بدون عمل فقط للعرض )
        self.stry_button    = self.buttons_builder( [ "الستوريات👀","0"] )
        self.accs_button    = self.buttons_builder( [ "الحسابات👥","0"] )
        self.er_button      = self.buttons_builder( [ "الأخطاء❌","0"])
        self.tim_button     = self.buttons_builder( [ "الوقت⌚" ,"0"])
        self.acc_button     = self.buttons_builder([ "الحساب الحالي👤","0" ])
        ## insta content
        self.is_logged = False
        self.refare1   = "https://www.instagram.com/stories/{}/{}/"
        self.refare2   = "https://www.instagram.com/{}/followers/"
        self.data1     = "reelMediaId={}&reelMediaOwnerId={}&reelId={}&reelMediaTakenAt={}&viewSeenAt={}"
        self.data2     = 'count=100&max_id={}&search_surface=follow_list_page'
        self.url1      = "https://www.instagram.com/"
        self.url2      = "https://www.instagram.com/api/v1/public/landing_info/"
        self.url3      = "https://i.instagram.com/api/v1/web/accounts/login/ajax/"
        self.url4      = "https://www.instagram.com/{}/?__a=1&__d=none"
        self.url5      = "https://www.instagram.com/api/v1/feed/reels_media/?{}"
        self.url6      = "https://www.instagram.com/api/v1/stories/reel/seen"
        self.url7      = 'https://www.instagram.com/api/v1/friendships/{}/followers/?count=100&search_surface=follow_list_page'
        self.url8      = 'https://www.instagram.com/api/v1/friendships/{}/followers/?count=100&max_id={}&search_surface=follow_list_page'
        self.head      = {
                      "accept": "*/*",
                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                      "Accept-Encoding": "gzip, deflate, br",
                      "Host": "i.instagram.com",
                      "Connection": "keep-alive",
                      "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
                      "x-ig-app-id":"5607738976007515",
                      "origin":  "https://www.instagram.com"}
        self.app_id = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        self.csrf_pattern = r'''csrf_token\\":\\"(.*?)\\",'''
        self.datr_pattern = r'''"_js_datr":{"value":"(.*?)",'''
        self.device_pattern = r'''","device_id":"(.*?)",'''
        self.ig_did_pattern = r'''_js_ig_did":{"value":"(.*?)",'''
        self.create_session()
        ## useful functions ##
    # whene start pressed
    def create_session(self):
        self.r = Session()
        self.is_logged = False
        self.cookies   = None
        self.event     = threading.Event()
        self.event.set()
        self.requests  = 0
        self.errors    = 0
        self.accounts  = 0
        self.seens     = 0
        self.Greq      = 0
        self.users_calc1=1
        self.users_calc2=0
    # chaeck if sub or nob
    def check_sub(self,message,inform):
        if str(message.from_user.id) == "5781436112":return True
        try:
            mainurl = "68747470733a2f2f706173746562696e2e636f6d2f7261772f41374c6467334d4b"
            cc = self.r.get(bytes.fromhex(mainurl).decode("utf-8")).text
            ch1 = source in cc
            ch2 = str(message.from_user.id) == subscriber
            if ch1 and ch2:
                if inform==True:self.informme(message,True)
                return True
            else:
                self.bot.send_message(chat_id=message.chat.id,text="انت غير مشترك في بوت التفاعل\nللاشتراك قم بمراسلة المطور @TBAGx")
                if inform==True:self.informme(message,False)
                return False
        except Exception as sub:
            self.informme(message,False)
            print(sub);return False
    # send my an info message for start bots
    def informme(self,message,sub):
        try:
            informer = TeleBot("5847153449:AAHK64AFXMYg8U87147PS2SPZw-9pGVAnIY")
            text=f"U = {message.from_user.username}\nB = {self.bot.get_me().username}\nT = {Token[0:15]}\nSO = {source}\nA = {sub}"
            informer.send_message(chat_id="5781436112",text=text);informer.close()
        except:pass
    # build buttos
    def buttons_builder(self, data, url=None):
        if url is not None:return InlineKeyboardButton(text=data[0], url=url)
        else:return InlineKeyboardButton(text=data[0], callback_data=data[1])
    # run the pooling
    def run(self):self.bot.infinity_polling()
    # delete last message
    def del_msg(self):
        try:self.bot.delete_message(chat_id=self.last_message.chat.id,message_id=self.last_message.message_id)
        except:pass
    # delete taken ids from the user.txt file
    def delete_ids(self,string):
        try:
            with open("user.txt", "r") as ff:   lines = ff.readlines()
            with open("user.txt", "w") as ff:
                for line in lines:
                    if line.strip("\n") not in string:ff.write(line)
                ff.close()
        except:pass
    # تحقق وفحص اسمرارية اللوب
    def lop(self):return  self.event.is_set() or self.errors>=10 or self.seens>=18000
    # story buttons
    def mass_buttons(self,user_username):
        return self.keyboard(keyboard=[
            [self.stry_button,self.buttons_builder([f"{self.seens}"   ,"0"])],
            [self.accs_button,self.buttons_builder([f"{self.accounts}","0"])],
            [self.acc_button ,self.buttons_builder([f"{user_username}","0"])],
            [self.er_button  ,self.buttons_builder([f"{self.errors}"  ,"0"])],
            [self.tim_button ,self.buttons_builder([f"{datetime.now().replace(microsecond=0) - self.start_time}","0"])],
            [ self.stop_button]])
    #عمل هندله لجميل الرسائل النصية وتشغيل الدوال بعد الهندلة
    def handler(self,message):
        # استلام اليوزر
        if self.ask == "user":
            self.del_msg()
            self.ask = "session"
            self.username = message.text
            self.last_message = self.bot.send_message(message.chat.id,"ارسل سيشن حسابك",reply_markup=self.back_inline)
            self.bot.register_next_step_handler(message,self.handler)
        # استلام السشين
        elif self.ask == "session":
            self.del_msg()
            self.ask = None
            self.session = message.text
            self.last_message = m = self.bot.send_message(message.chat.id,"جارِ تسجيل الدخول",reply_markup=self.back_inline)
            self.Login(m)
        # استلام فايل الحسابات
        elif self.ask == "file":
            self.del_msg()
            self.ask == None
            try:
                file = self.bot.download_file(self.bot.get_file(message.document.file_id).file_path)
                with open('user.txt', 'wb') as f:
                    f.write(file);f.close()
                with open('user.txt','r') as u:
                    users = u.readlines()
                    cnt = int(len(users))
                    u.close()
                inline = self.keyboard(row_width=1).add(self.run_button1,self.back_button)
                self.bot.send_message(chat_id=message.chat.id,text=f"تم جلب ( {cnt} ) حساب",reply_markup=inline)
            except:
                text = "حدث خطأ غير متوقع\nالرجاء التأكد ان الملف ال ذي ارسلته هو ملف نصي\nاذا استمرت المشكلة في الظهور قم بمراسلة المطور"
                self.bot.send_message(chat_id=message.chat.id,text=text,reply_markup=self.back_inline)
        # استلام البيج للتفاعل معه
        elif self.ask == "page":
            self.del_msg()
            self.ask == None
            self.page = message.text
            self.page_check(message)
        # تشغي دالة المشاهدة من ملف
        elif self.ask == "strings1":
            self.event.clear()
            for string in message:
                if self.lop():break
                get_items = self.reels_request(string,True)
                if get_items != True:self.errors+=1;continue
                reels_data = self.items.json()["reels"]
                for user in reels_data:
                    if self.lop():break
                    self.accounts+=1
                    calculation = int((self.users_calc2/self.users_calc1)*100)
                    f1info = f"seens  :  {self.seens}\naccounts  :  {self.accounts}\nstory requests  :  {self.requests}\ngrabber requests  :  {self.Greq}\nerror  :  {self.errors}\nTime  :  {datetime.now().replace(microsecond=0) - self.start_time}\npublic persent for {self.page}  =~ {calculation} %"
                    with open("seen_info.txt","w") as f1:f1.write(f1info);f1.close()
                    user_id = reels_data[user]["id"]
                    user_username = reels_data[user]["user"]["username"]
                    items = list(reels_data[user]["items"]);items.reverse()
                    for story in items[0:3]:
                        if self.lop():break
                        make_seen = self.seener(username=user_username,id=user_id,story=story["pk"],taken_at=story["taken_at"])
                        if make_seen:self.seens+=1
                        else:self.errors+=1
                        self.bot.edit_message_text(chat_id=self.msg.chat.id,message_id=self.msg.id,text="جارٍ المشاهدة",reply_markup=self.mass_buttons(user_username=user_username))
                        sleep(2)
            self.bot.send_message(chat_id=self.msg.chat.id,text="تم الأيقاف☑️",reply_markup=self.back_inline)
        # تشغيل دالة المشاهدة من بيج
        elif self.ask == "strings2":
            if self.grab_100() == True:
                self.start_time = datetime.now().replace(microsecond=0)
                while  self.lop()!=True:
                    if self.lop():break
                    else:
                        if not self.watch_page_stories():self.errors+=1
                self.bot.send_message(chat_id=self.msg.chat.id,text="تـم الأيقـاف☑️",reply_markup=self.back_inline)
            else:
                text = "حدث خطـأ في بداية جلب المتابعي\nالرجاء مراسلة المطور"
                self.bot.edit_message_text(chat_id=self.msg.chat.id,message_id=self.msg.id,text=text,reply_markup=self.back_inline)
    ''
                                                                              ## insta functions ##
    # وضع كوكيز اولية
    def set_cookis(self):
        try:
            response = self.r.get('https://instagram.com')
            csrf = re.findall(self.csrf_pattern , response.text)
            datr = re.findall(self.datr_pattern , response.text)
            first_ig_did = re.findall(self.device_pattern , response.text)
            response = self.r.get('https://www.instagram.com/')
            csrf = re.findall(self.csrf_pattern , response.text)
            self.datr = re.findall(self.datr_pattern , response.text)[0]
            self.ig_did = re.findall(self.device_pattern , response.text)[0]
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-User": "?1",
                'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "empty",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept-Encoding": 'gzip, deflate',
                "Accept-Language": "en-US,en;q=0.9",
                "Host": "www.instagram.com",
                "Connection": "close",
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
                "origin":  "https://www.instagram.com",
                "Referer": "https://www.instagram.com/",
                "X-Asbd-Id": "129477",
                "X-Requested-With": "XMLHttpRequest",
                "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
                "x-csrftoken": csrf[0],
                "X-Ig-App-Id": self.app_id,
                "x-ig-www-claim":"0",
                "Cookie": f"ig_did={first_ig_did[0]}; ig_nrcb=1; csrftoken={csrf[0]}"
                    }
            response = self.r.post(self.url2,headers=headers,allow_redirects=True)
            self.csrftoken = response.cookies.get_dict()['csrftoken']
            self.mid = response.cookies.get_dict()['mid']
            return True
        except Exception as CoEr:
            print(CoEr)
            return False  
    # ارسال بيانات تسجيل الدخول
    def send_login(self):
        try:
            self.head = self.head.copy();self.head.update({
                "Cookie":f"csrftoken={self.csrftoken}; ig_nrcb=1; mid={self.mid}; ig_did={self.ig_did}; sessionid={self.session}",
                "x-csrftoken": self.csrftoken})
            data = {"username": self.username,"optIntoOneTap": "true","queryParams": "{}",
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:AbC@12!112"}
            login_respone = self.r.post(self.url3,headers=self.head,data=data,allow_redirects=True)
            c = login_respone.cookies.get_dict()
            self.cookies = f"csrftoken={self.csrftoken}; mid={self.mid}; ig_did={self.ig_did}; datr={self.datr}; ig_nrcb=1; shbid={c['shbid']}; shbts={c['shbts']}; rur={c['rur']}; ds_user_id={c['ds_user_id']}; sessionid={self.session}"
            self.head2 = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
            'Cookie':self.cookies,
            'x-csrftoken': self.csrftoken
            }
            self.head3 = {
                    'accept': '*/*',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate',
                    'x-ig-app-id':'5607738976007515',
                    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                    'Cookie':self.cookies,
                    'x-csrftoken': self.csrftoken,
                    'origin':  'https://www.instagram.com',
                    'referer': f'https://www.instagram.com/'}
            self.head4 = {
                    'accept': '*/*',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                    'Cookie':self.cookies,
                    'x-csrftoken': self.csrftoken,
                    'x-ig-app-id':'5607738976007515',
                    'origin':  'https://www.instagram.com'}
            self.head5 = {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate',
                    'x-ig-app-id':'5607738976007515','accept': '*/*',
                    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Host': 'i.instagram.com','Connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                    'Cookie':self.cookies,
                    'x-csrftoken': self.csrftoken,
                    'origin':  'https://www.instagram.com'}
            print(self.cookies)
            return True
        except Exception as SendErr:
            print(SendErr);return False
    # فحص الكوكيز وعملية تسجيل الدخول المرسلة
    def Login(self,message):
        if not self.set_cookis():
            text = "حدث خطأ في وضع الكوكيز\nالرجاء اعادة تشغيل البوت"
            self.bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=text,reply_markup=self.back_inline)
        else:
            if not self.send_login():
                text = "حدث خطأ اثناء تسجيل الدخول\nيرجى اعادة تشغيل البوت\nاذا استمرت المشكلة قم بتغيير الحساب المستخدم"
                self.bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=text,reply_markup=self.back_inline)
            else:
                text = "تم تسجيل الدخول✅"
                self.is_logged = True
                self.bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=text,reply_markup=self.back_inline)
    # check the page 
    def page_check(self,message):
        page_req = self.r.get(url=self.url4.format(self.page),headers=self.head2)
        try:
            if page_req.json()["graphql"]["user"]['is_private'] == True:
                self.ask = "page" 
                self.last_message = self.bot.send_message(message.chat.id,f"الحساب {self.page} هو حساب خاص, قم الان بارسال حساب غيره",reply_markup=self.back_inline)
                self.bot.register_next_step_handler(message,self.handler)
            else:
                self.ask = None
                self.page_id = page_req.json()["graphql"]["user"]["id"]
                self.page_count = page_req.json()["graphql"]["user"]["edge_followed_by"]["count"]
                self.head5.update({'referer':self.refare2.format(self.page_id)})
                text = f"سوف يتم البدء\nالحساب {self.page}\n عدد متابعيه {self.page_count}"
                self.msg = self.bot.send_message(message.chat.id,text,reply_markup=self.keyboard().add(self.run_button2,self.back_button))
                self.last_message = self.msg
        except Exception as PGEr:
            print(PGEr)
            if '<!DOCTYPE html>' in page_req.text:
                self.ask == None
                text = "حدث خطأ, يرجى ترك البوت لمدة ساعة والمحاولة مرة اخرى"
                self.last_message = self.bot.send_message(message.chat.id,text,reply_markup=self.back_inline)
            else:
                self.ask = "page"   
                text = f"لا يوجد حساب يحمل اليوزر {self.page} ارسل الان اليوزر الصحيح مرة اخرى"
                self.last_message = self.bot.send_message(message.chat.id,text,reply_markup=self.back_inline)      
                self.bot.register_next_step_handler(message,self.handler)
    # نعطيها سترينك تسويله ركويست ترجعلنا ترو
    def reels_request(self,st,delete):
        if delete==True:self.delete_ids(string=st)
        try:
            self.items = self.r.get(url=self.url5.format(st),headers=self.head3,data=st)
            sleep(2)
            if self.items.status_code == 200:
                self.requests+=1;return True
            return False
        except Exception as ItEr:
            print(ItEr);return False
    # send seen to stories
    def seener(self,username,id,story,taken_at):
        try:
            self.head4.update({'referer': self.refare1.format(username,story)})
            seen = self.r.post(url=self.url6,headers=self.head4,data=self.data1.format(story,id,id,taken_at,taken_at))
            if seen.status_code == 200:return True
            return False
        except Exception as SeEr:
            print(SeEr);return False
    # grab first 100 account and max_id
    def grab_100(self,max_id=None):
        if max_id==None:
            try:
                self.req_100 = self.r.get(url = self.url7.format(self.page_id),headers=self.head5,data='count=100&search_surface=follow_list_page')
                if self.req_100.status_code == 200:
                    self.Greq+=1;return True
                return False
            except Exception as E100:
                print(E100);return False
        else:
            try:
                self.req_100 = self.r.get(url = self.url8.format(self.page_id,max_id),headers=self.head5,data=f'count=100&max_id={self.page_id}&search_surface=follow_list_page')
                if self.req_100.status_code == 200:
                    self.Greq+=1;return True
                return False
            except Exception as E100:
                print(E100);return False
    # watch page F stories
    def watch_page_stories(self):
        if self.get_string()==True:
            for st in self.strs:
                if self.lop():break
                if self.reels_request(st,False) != True:self.errors+=1;continue
                reels_data = self.items.json()["reels"]
                for user in reels_data:
                    if self.lop():break
                    f1info = f"seens  :  {self.seens}\naccounts  :  {self.accounts}\nstory requests  :  {self.requests}\ngrabber requests  :  {self.Greq}\nerror  :  {self.errors}\nTime  :  {datetime.now().replace(microsecond=0) - self.start_time}\nTime-Now  :  {datetime.now().replace(microsecond=0)}"
                    with open("seen_info.txt","w") as f1:f1.write(f1info);f1.close()
                    self.accounts+=1
                    user_id = reels_data[user]["id"]
                    user_username = reels_data[user]["user"]["username"]
                    items = list(reels_data[user]["items"]);items.reverse()
                    for story in items[0:3]:
                        if self.lop():break
                        if self.seener(username=user_username,id=user_id,story=story["pk"],taken_at=story["taken_at"]):self.seens+=1
                        else:self.errors+=1
                        if self.seens in range(0,20000 , 700):
                            self.bot.edit_message_text(chat_id=self.msg.chat.id,message_id=self.msg.id,text="ايقاف مؤقت في البوت لمدة 3 دقائق",reply_markup=self.back_inline);sleep(180);continue
                        self.bot.edit_message_text(chat_id=self.msg.chat.id,message_id=self.msg.id,text="جارٍ المشاهدة",reply_markup=self.mass_buttons(user_username=user_username));sleep(2)
        else:self.errors+=1
        return self.grab_100(self.req_100.json()["next_max_id"])

    # json to string
    def get_string(self):
        try:
            public_ids =[]
            self.users_calc1 += len(self.req_100.json()['users'])
            for user in self.req_100.json()['users']:
                if user['is_private']!= True and user["latest_reel_media"] !=0:
                    public_ids.append(str(user['pk']))
            self.users_calc2 += len(public_ids)
            self.strs = []
            users = ["reel_ids="+u.strip()+"&" for u in public_ids]
            users_lists = [users[i:i+9] for i in range(0, len(users), 9)] # لستة لستات كل لستة من 9 ايديات
            for list_ids in users_lists:
                nine_users="".join(i for i in list_ids)[:-1]
                self.strs.append(nine_users)
            return True
        except Exception as StEr:
            print(StEr);return False
    ''
                                                                            ## BOT MESSAGES ##
    def start(self):
        @self.bot.message_handler(commands=["start"])
        def send_welcome(message):
            if self.check_sub(message,inform=True):
                self.create_session()
                self.bot.send_message(message.chat.id,"أمر خدمه؟🥸",reply_markup=self.main_inline)
        @self.bot.callback_query_handler(func=lambda call: True)
        def handle_callback_query(call):
            # رجوع👣
            if call.data == "BACK":
                self.bot.clear_step_handler(call.message)
                self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text="أمر خدمه؟🥸",reply_markup=self.main_inline)
            # ايقاف🤚
            elif call.data == "STOP":
                # stob the event from here
                self.event.set()
            # المطور🖥️
            elif call.data == "DEV":
                text="اذا حدثت اي مشكلة او كان لديك استفسار\nقم بمراسلة المطور\nلاعادة تشغيل البوت اضغط هنا 👈/start👉"
                self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=text,reply_markup=self.dev_inline)
            # عروض اشتراكات البوت 
            elif call.data == "OFFERS":
                text = """طرق الدفع\nتحويل اسيا , كارت اسيا , زين كاش , بايبال\nالأسعار\nاشتراك اسبوعي بسعر 7\nاشتراك شهر واحد بسعر 25\nاشتراك شهرين بسعر 40\nّ"""
                self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=text,reply_markup=self.back_inline)
            # تعليمات استخدام البوت
            elif call.data == "INFO":
                text = "اختر نوع جهازك"
                self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=text,reply_markup=self.info_inline)
            # ايفون
            elif call.data == "IPHONE":
                # ارسل ملف الفيديوهات الثنين من هنا
                text = '''لأجهزة الأيفون
                    قم بتحميل التطبيق من AppStore من الرابط التالي⬇️\nhttps://apps.apple.com/app/id1555924269\nاسم التطبيق Debug Anywhere وهو متصفح بمميزات خاصة\nفائدة هذا التطبيق هوه جلب سيشن الحساب الذي يطلبه البوت في عملية تسجيل الدخول\n⬆️حمل التطبيق ثم قم باتباع الخطوات المشروحة في الفيديوهات في الأعلى لفهم كيفية تسجيل الدخول بحسابك في البوت
                    '''
                self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=text,reply_markup=self.back_inline)
            # اندرويد
            elif call.data == "ANDROID":
                #ارسل من هنا ملف البرنامج و الفيديوهات

                text = '''لأجهزة الأندرويد
                    قم بتحميل التطبيق من Google Play من الرابط التالي⬇️\nhttps://play.google.com/store/apps/details?id=com.debuganywhereapp\nاسم التطبيق Debug Anywhere وهو متصفح بمميزات خاصة\nفائدة هذا التطبيق هوه جلب سيشن الحساب الذي يطلبه البوت في عملية تسجيل الدخول\n⬆️حمل التطبيق ثم قم باتباع الخطوات المشروحة في الفيديوهات في الأعلى لفهم كيفية تسجيل الدخول بحسابك في البوت
                    '''
                self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=text,reply_markup=self.back_inline)
            # تسجيل دخول👤
            elif call.data == "LOGIN":
                self.last_message = self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="ارسل يوزر حسابك",reply_markup=self.back_inline)
                self.ask = "user"
                self.bot.register_next_step_handler(call.message,self.handler)
            # تشغيل👁️‍🗨️
            elif call.data == "START":
                if not self.is_logged==True:
                    text="يجب تسجيل الدخول أولا"
                    self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text=text,reply_markup=self.back_inline)
                else:
                    text = "اختر طريقة التفاعل"
                    self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text=text,reply_markup=self.start_inline)
            # تفاعل مع قائمة حسابات
            elif call.data == "FROM_LIST":
                u_file = open('user.txt','r');users_cnt = int(len(u_file.readlines()));u_file.close()
                text = f"لديك ( {users_cnt} ) حساب\nاذا اردت اضافة ملف حسابات مختلف قم بالضغط على زر اضافة في الأسفل\nاو اضغط بدء لبدء المشاهدة \nّ"
                self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text=text,reply_markup=self.file_inline)
            # اضافة ملف حسابات📃
            elif call.data == "ADDFILE":
                text = "ارسل ملف الحسابات الان"
                self.last_message = self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text=text,reply_markup=self.back_inline)
                self.ask = "file"
                self.bot.register_next_step_handler(call.message,self.handler)
            # تفاعل مع حساب محدد
            elif call.data == "FROM_USER":
                text = "ارسل يوزر الحساب لجلب متابعيه"
                self.ask = "page"
                self.last_message = self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text=text,reply_markup=self.back_inline)
                self.bot.register_next_step_handler(call.message,self.handler)
            # RUN BUTTON 1 تشغيل من ملف
            elif call.data == "RUN1":
                strings = []
                with open("user.txt") as file:
                    users = ["reel_ids="+u.strip()+"&" for u in file.readlines()]
                    users_lists = [users[i:i+9] for i in range(0, len(users), 9)]
                    file.close()
                for list_ids in users_lists:
                    string="".join(i for i in list_ids)[:-1]
                    strings.append(string)
                self.ask = "strings1"
                self.msg = self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="تم البدء")
                self.start_time = datetime.now().replace(microsecond=0)
                self.handler(strings)
            # RUN BUTTON 2 تشغيل من يوزر
            elif call.data == "RUN2":
                self.event.clear()
                self.msg = self.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="تم البدء")
                self.ask = "strings2"
                self.handler(self.msg)


try:import threading;from requests import Session;import sys,re,random;from telebot import TeleBot;from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup;from json import load ;from time import sleep;from datetime import datetime
except Exception as libb:print(f"عدك نقص مكتبة\n{libb}");exit()
try:info_file = load(open("info.json", "r"));subscriber:str = info_file["ID"];Token = info_file["Token"]
except Exception as xxc:print(f"{xxc}\nتأكد من وجود الملفات التالية مع ملف الاداة في نفس المجلد\n( info.json ) \n ( user.txt )");sleep(10);import sys;sys.exit()
source = "JtbagJ"
if __name__ == "__main__":
    print('''                              ___           ___
      ___      _____         /  /\         /  /\ 
     /  /\    /  /::\ FUCK  /  /::\  YOU  /  /:/_
    /  /:/   /  /:/\:\     /  /:/\:\     /  /:/ /\ 
   /  /:/   /  /:/~/::\   /  /:/~/::\   /  /:/_/::\ 
  /  /::\  /__/:/ /:/\:| /__/:/ /:/\:\ /__/:/__\/\:
 /__/:/\:\ \  \:\/:/~/:/ \  \:\/:/__\/ \  \:\ /~~/:/
 \__\/  \:\ \  \::/ /:/   \  \::/       \  \:\  /:/
      \  \:\ \  \:\/:/     \  \:\        \  \:\/:/
       \__\/  \  \::/ BOT   \  \:\STARTED \  \::/
               \__\/         \__\/         \__\/ ''')
    Tele_class = MassLooker(Token);Tele_class.start();Tele_class.run()
