import colorama
from user_agent import generate_user_agent
from time import sleep
class DStory:
    def __init__(self,cook,req,head,users,ids):
        self.sleep =  int(input('Enter accounts sleep : '))
        self.sleep2 = int(input('Enter story watch sleep : '))
        self.req = req
        self.users = users
        self.ids = ids
        #cookies
        self.cook = cook
        self.csrftoken = self.cook['csrftoken']
        self.sessionid = str(self.cook['sessionid'])
        self.rur = self.cook['rur']
        self.ds_user_id = self.cook['ds_user_id']
        #head
        self.head = head
        self.asbd = head['asbd']
        self.APPID = head['APPID']
        self.ajax = head['ajax']
    def get_ids(self):
            err =0
            seens = 0
            users_count = len(self.users)
            for sequence in range(0,users_count):
                try:
                    #self.users
                    #self.ids
                    iddd = self.ids[sequence]
                    usss = self.users[sequence]
                    tray_head = {
                        'accept': '*/*',
                        'Host': 'i.instagram.com',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                        'viewport-width': '464',
                        'x-asbd-id':self.asbd,
                        'x-csrftoken': self.csrftoken,
                        'x-ig-app-id':self.APPID,
                        'x-instagram-ajax':self.ajax,
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-ig-www-claim': 'hmac.AR3U9SgkUz2nZg_Jx4m0AQA2dLs7aqjooR_FknrkUz-ukjkF',
                        'origin': 'https://www.instagram.com',
                        'referer': 'https://www.instagram.com/',
                        'x-requested-with': 'XMLHttpRequest'
                        }
                    tray_url = f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={str(iddd)}"
                    tray_respone = self.req.get(tray_url,headers=tray_head,data={'reel_ids': iddd})
                    try:
                        if tray_respone.json()["reels"] == {}:
                            continue 
                    except:
                        err+=1
                        print(colorama.Fore.RED +f'\nerror {err} ')
                        continue
                    try:
                        itames = tray_respone.json()["reels"][iddd]["items"]
                    except:
                        err+=1
                        print(colorama.Fore.RED +f'\nerror {err} ')
                        continue
                    for itame in itames:
                        sleep(self.sleep2)
                        try:
                            #data={
                            #     "reelMediaId":itame['pk'],
                            #     "reelMediaOwnerId":iddd,
                            #     "reelId":iddd,
                            #     "reelMediaTakenAt":itame['taken_at'],
                            #     "viewSeenAt":itame['taken_at']
                            #     }
                            data = f"reelMediaId={itame['pk']}&reelMediaOwnerId={iddd}&reelId={iddd}&reelMediaTakenAt={itame['taken_at']}&viewSeenAt={itame['taken_at']}"
                        except:
                            print('data set error')
                        response = self.req.post("https://i.instagram.com/api/v1/stories/reel/seen",data=data,headers=tray_head)#memoryview: a bytes-like object is required, not 'str'
                        try:
                            if response.json()["status"] =="ok":
                                seens+=1
                                print({ "seen Count".upper():str(seens),"status":"ok","user":usss})
                            else:
                                print(colorama.Fore.RED +{"status":"NOOO","user":usss})
                        except Exception as status:
                            print(colorama.Fore.RED +'error status '+ str(status))
                    sleep(self.sleep)
                except Exception as tray_er:
                    print(colorama.Fore.RED +'\nthe tray_er error  \n'+str(tray_er))
                    return False
            return True
    def end(self):
        if self.get_ids() == True:
            print('Done')
            return True
        else:
            print('Error')
            return False
def starter(cook,req,head,users,ids):
    print('traying')
    t = DStory(cook=cook,req=req,head=head,users=users,ids=ids).end()
    if t == True:
        print('finished')
    else:
        print('wrong')
