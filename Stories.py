from datetime import datetime;from time import sleep
class DStory:
    def __init__(self,cook,req,head,ids):
        self.req = req;self.ids = ids
        self.accounts = 0;self.seens = 0;self.requests = 0;self.nost = 0;self.errors = 0
        try:
            self.cook = cook
            self.csrftoken = self.cook['csrftoken']
            self.sessionid = self.cook['sessionid']
            self.rur = self.cook['rur']
            self.ds_user_id = self.cook['ds_user_id']
            self.shbid = self.cook['shbid']
            self.shbts = self.cook['shbts']
            self.mid = self.cook['mid']
            self.ig_did = self.cook['ig_did']
            self.ig_nrcb = '1'
        except: print('you have a missing cookies. please fix it and try again');return False
        self.head = head;self.asbd = head['asbd'];self.APPID = head['APPID'];self.ajax = head['ajax']
        def ask():
            try:
                self.sleep =  int(input('Enter sleep between accounts : '))
                self.sleep2 = int(input('Enter sleep between stories : '))
                while self.sleep >= 2 and self.sleep2 >= 2 :    return True
                else:   print('\nthe sleep cannot be less than ( 2 )\n');return False      
            except: print('\nEnter a vaild number\n');return False
        while ask() == False:   ask()
        else:   self.max = int(input('enter max stories per account : '));print()
        if self.sleep>2:self.sleep=2
        if self.sleep2>2:self.sleep2=2
    def get_ids(self):
            f = 0;s = 1;t = 2;l = 3;g = 4;h = 5;j = 6;k = 7
            users_count = int(len(self.ids)/8)
            start_time = datetime.now()
            for sequence in range(0,users_count):
                fid = self.ids[f];sid = self.ids[s];tid = self.ids[t];lid = self.ids[l];gid = self.ids[g];hid = self.ids[h];jid = self.ids[j];kid = self.ids[k]
                f+=8;s+=8;t+=8;l+=8;g+=8;h+=8;j+=8;k+=8
                fitm = False;sitm = False;titm = False;litm = False;gitm = False;hitm = False;jitm = False;kitm = False
                try:
                    with open("user.txt", "r") as ff:
                        lines = ff.readlines()
                    with open("user.txt", "w") as ff:
                        for line in lines:
                            g = line.strip("\n")
                            if g != f"{fid}" and g != f"{sid}" and g != f"{tid}" and g != f"{lid}" and g != f"{gid}" and g != f"{hid}" and g != f"{jid}" and g != f"{kid}": ff.write(line)
                        ff.close()
                except: pass
                try:
                    try:
                        tray_head = {
                            'accept': '*/*',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Accept-Encoding': 'gzip, deflate',
                            'Host': 'i.instagram.com',
                            'Connection': 'keep-alive',
                            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                            'Cookie':f'csrftoken={self.csrftoken}; rur={self.rur}; ds_user_id={self.ds_user_id}; sessionid={self.sessionid}; ig_nrcb={self.ig_nrcb}; shbid={self.shbid}; shbts={self.shbts}; mid={self.mid}; ig_did={self.ig_did};',
                            'x-asbd-id':self.asbd,
                            'x-csrftoken': self.csrftoken,
                            'x-ig-app-id':self.APPID,
                            'x-instagram-ajax':self.ajax,
                            'origin':  'https://www.instagram.com',
                            'referer': f'https://www.instagram.com/',
                            }
                        tray_url = f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={str(fid)}&reel_ids={str(sid)}&reel_ids={str(tid)}&reel_ids={str(lid)}&reel_ids={str(gid)}&reel_ids={str(hid)}&reel_ids={str(jid)}&reel_ids={str(kid)}"
                        tray_respone = self.req.get(tray_url,headers=tray_head,data=  f"reel_ids={str(fid)}&reel_ids={str(sid)}&reel_ids={str(tid)}&reel_ids={str(lid)}&reel_ids={str(gid)}&reel_ids={str(hid)}&reel_ids={str(jid)}&reel_ids={str(kid)}");self.requests+=1
                    except: print('Error setting Stories data');return False
                    def seener(stories,user):
                        try:
                            self.accounts +=1;stories_count = len(stories)
                            if stories_count >=self.max:
                                stories_count = self.max
                            for story in range(0,stories_count):
                                if self.errors == 20:   break
                                try:
                                    seen_head = {
                                        'accept': '*/*',
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Accept-Encoding': 'gzip, deflate',
                                        'Host': 'i.instagram.com',
                                        'Connection': 'keep-alive',
                                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                                        'Cookie':f'csrftoken={self.csrftoken}; rur={self.rur}; ds_user_id={self.ds_user_id}; sessionid={self.sessionid}; ig_nrcb={self.ig_nrcb}; shbid={self.shbid}; shbts={self.shbts}; mid={self.mid}; ig_did={self.ig_did};',
                                        'x-asbd-id':self.asbd,
                                        'x-csrftoken': self.csrftoken,
                                        'x-ig-app-id':self.APPID,
                                        'x-instagram-ajax':self.ajax,
                                        'origin':  'https://www.instagram.com',
                                        'referer': f'https://www.instagram.com/stories/{user}/{stories[story]["pk"]}/',
                                        }
                                except: print('data set error');continue
                                ء(0.20);plug = 23*self.sleep2;taken_at_respone = str(int(stories[story]['taken_at'])+plug)
                                response = self.req.post("https://i.instagram.com/api/v1/stories/reel/seen",data=f"reelMediaId={stories[story]['pk']}&reelMediaOwnerId={stories[story]['user']['pk']}&reelId={stories[story]['user']['pk']}&reelMediaTakenAt={stories[story]['taken_at']}&viewSeenAt={taken_at_respone}",headers=seen_head)
                                try:
                                    self.took = datetime.now() - start_time
                                    if response.json()["status"] =="ok":
                                        self.seens+=1
                                        print({ "seen Count".upper():str(self.seens),"Time":f"{self.took}",'Requests':self.requests,'Errors':self.errors,"user":user,'account':self.accounts})
                                        seen_info = open('seen_info.txt','w+')
                                        seen_info.write(f'[Accounts with stories : {self.accounts} ] , [Accounts without stories : {self.nost} ] , [stories seen : {self.seens}] , [Errors : {self.errors}] , [Requests : {self.requests}] , [Time : {self.took}]')
                                        seen_info.close();ء(self.sleep2)
                                    else:
                                        self.errors+=1
                                        print({"status":"NOOO","Time":f"{self.took}","Errors":{self.errors}})
                                        print(response.json())
                                    if self.seens == 1000 or self.seens == 200  or self.seens == 3000  or self.seens == 4000 or self.seens == 5000 or self.seens == 6000 or self.seens == 7000 or self.seens == 8000 or self.seens == 9000 or self.seens == 10000:
                                        self.seens+=1;print('sleeping 200 second');ء(200)
                                    if self.requests == 100 or self.requests == 200 or self.requests == 300 or self.requests == 400 or self.requests == 500 or self.requests == 600 or self.requests == 700 or self.requests == 800 or self.requests == 900 or self.requests == 1000 :
                                        self.requests+=1;print('sleeping 100 second');ء(100)
                                    if self.accounts == 300 or self.accounts == 600 or self.accounts == 900 or self.accounts == 1200 or self.accounts == 1500 or self.accounts == 1800 or self.accounts == 2100 or self.accounts == 2400 or self.accounts == 2700 or self.accounts == 3000 or self.accounts == 3300:
                                        self.accounts+=1;print('sleeping 100 second'); ء(100)
                                except Exception as status: print('error status '+ str(status))
                            return True
                        except Exception as se: print(f'seen error\n{se}');return False
                    try:
                        if tray_respone.json()["reels"][fid]["items"] == {}:
                            fitm = False;self.nost+=1
                        elif tray_respone.json()["reels"][fid]["items"][0]:
                             fitm = True
                        else:   fitm = False;self.nost+=1
                    except: self.nost+=1;fitm = False
                    try:
                        if tray_respone.json()["reels"][sid]["items"] == {}:
                            sitm = False;self.nost+=1
                        elif tray_respone.json()["reels"][sid]["items"][0]:
                             sitm = True
                        else:   sitm = False;self.nost+=1
                    except: self.nost+=1;sitm = False
                    try:
                        if tray_respone.json()["reels"][tid]["items"] == {}:
                            titm = False; self.nost+=1
                        elif tray_respone.json()["reels"][tid]["items"][0]:
                             titm = True
                        else:   titm = False;self.nost+=1
                    except: self.nost+=1;titm = False
                    try:
                        if tray_respone.json()["reels"][lid]["items"] == {}:
                            litm = False;self.nost+=1
                        elif tray_respone.json()["reels"][lid]["items"][0]:
                             litm = True
                        else:   litm = False;self.nost+=1
                    except: self.nost+=1;litm = False
                    try:
                        if tray_respone.json()["reels"][gid]["items"] == {}:
                            gitm = False;self.nost+=1
                        elif tray_respone.json()["reels"][gid]["items"][0]:
                             gitm = True
                        else:   gitm = False;self.nost+=1
                    except: self.nost+=1;gitm = False
                    try:
                        if tray_respone.json()["reels"][hid]["items"] == {}:
                            hitm = False;self.nost+=1
                        elif tray_respone.json()["reels"][hid]["items"][0]:
                             hitm = True
                        else:   hitm = False;self.nost+=1
                    except: self.nost+=1; hitm = False
                    try:
                        if tray_respone.json()["reels"][jid]["items"] == {}:
                            jitm = False;self.nost+=1
                        elif tray_respone.json()["reels"][jid]["items"][0]:
                             jitm = True
                        else:   jitm = False; self.nost+=1
                    except: self.nost+=1;jitm = False
                    try:
                        if tray_respone.json()["reels"][kid]["items"] == {}:
                            kitm = False;self.nost+=1
                        elif tray_respone.json()["reels"][kid]["items"][0]:
                             kitm = True
                        else:   kitm = False;self.nost+=1
                    except: self.nost+=1;kitm = False
                    if fitm:
                         fitems = tray_respone.json()["reels"][fid]["items"]
                         useruser = tray_respone.json()["reels"][fid]['user']['username']
                         if seener(fitems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                    if sitm:
                         stiems = tray_respone.json()["reels"][sid]["items"]
                         useruser = tray_respone.json()["reels"][sid]['user']['username']
                         if seener(stiems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                    if titm:
                         ttiems = tray_respone.json()["reels"][tid]["items"]
                         useruser = tray_respone.json()["reels"][tid]['user']['username']
                         if seener(ttiems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                    if litm:
                         ltiems = tray_respone.json()["reels"][lid]["items"]
                         useruser = tray_respone.json()["reels"][lid]['user']['username']
                         if seener(ltiems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                    if gitm:
                         gtiems = tray_respone.json()["reels"][gid]["items"]
                         useruser = tray_respone.json()["reels"][gid]['user']['username']
                         if seener(gtiems,useruser) == True:    sleep(self.sleep)
                         else:   self.errors+=1
                    if hitm:
                         htiems = tray_respone.json()["reels"][hid]["items"]
                         useruser = tray_respone.json()["reels"][hid]['user']['username']
                         if seener(htiems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                    if jitm:
                         jtiems = tray_respone.json()["reels"][jid]["items"]
                         useruser = tray_respone.json()["reels"][jid]['user']['username']
                         if seener(jtiems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                    if kitm:
                         ktiems = tray_respone.json()["reels"][kid]["items"]
                         useruser = tray_respone.json()["reels"][kid]['user']['username']
                         if seener(ktiems,useruser) == True:    sleep(self.sleep)
                         else:  self.errors+=1
                except Exception as tray_er:
                    if tray_er is ConnectionAbortedError:   self.get_ids()
                    else:   print('\nthe tray_er error  \n'+str(tray_er));return False
            print(f'[Accounts with stories : {self.accounts} ] , [Accounts without stories : {self.nost} ] , [stories seen : {self.seens}] , [Errors : {self.errors}] , [Time : {self.took}]')
            return True
    def end(self):
        if self.get_ids() == True:  return True
        else:   return False
def starter(cook,req,head,ids):
    print('DStory Started')
    t = DStory(cook=cook,req=req,head=head,ids=ids).end()
    if t == True:   print('finished')
    else:   print('wrong')
def ء(ف):   sleep(ف)