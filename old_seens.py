import requests
from time import sleep
from datetime import datetime
import sys

req = requests.Session()

def set_cookies():  #جلب الكوكيز الاوليه قبل تسجيل الدخول
    url1      = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
    cook1 = req.get(url1)
    try:
        global mid,csrf,ig_did
        csrf =   cook1.cookies.get_dict()['csrftoken']  
        mid =    cook1.cookies.get_dict()['mid']
        ig_did = cook1.cookies.get_dict()['ig_did']
        return True 
    except:
        print('error set_cookies')
        return False

def send_login(u,s):
    try:
        head = {
            "accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "i.instagram.com",
            "Connection": "keep-alive",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
            "x-ig-app-id":"5607738976007515",
            "origin":  "https://www.instagram.com",
            "Cookie":f"csrftoken={csrf}; ig_nrcb=1; mid={mid}; ig_did={ig_did}; sessionid={s}",
            "x-csrftoken": csrf
            }
        data = {"username": u,"optIntoOneTap": "true","queryParams": "{}",
                "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:AbC@12!112"}
        login_url      = "https://i.instagram.com/api/v1/web/accounts/login/ajax/"
        log_req = req.post(url=login_url,headers=head,data=data)
        if log_req.json()['authenticated']==True:
            shbts = log_req.cookies.get_dict()['shbts']
            shbid = log_req.cookies.get_dict()['shbid']
            rur = log_req.cookies.get_dict()['rur']
            ds_user_id = log_req.cookies.get_dict()['ds_user_id']
            global cookies
            cookies = f'csrftoken={csrf}; shbts={shbts}; shbid={shbid}; rur={rur}; ds_user_id={ds_user_id}; sessionid={s}; mid={mid}; ig_did={ig_did}; ig_nrcb=1'
            return True
        else: 
            return False
    except Exception as e:
        print(e)
        return False


def get_reels(myid):
     url_reels =  f'https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={myid}'
     reels_data = f"reel_ids={myid}"
     reels_head = {
                    'accept': '*/*',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate',
                    'x-ig-app-id':'5607738976007515',
                    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                    'Cookie':cookies,
                    'x-csrftoken': csrf,
                    'origin':  'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/'}
     req_reels= req.get(url=url_reels , headers=reels_head , data=reels_data)
     return req_reels.json()

     

def check_reels(json_data,myid):
     try:
        json_data['reels'][f"{myid}"]
        return True
     except:
        return False
    

def seener(story,id,taken_at):
    try:
        head4 = {
            'accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
            'Cookie':cookies,
            'x-csrftoken': csrf,
            'x-ig-app-id':'5607738976007515',
            'origin':  'https://www.instagram.com'}
        url6 = "https://www.instagram.com/api/v1/stories/reel/seen"
        seend_data = f"reelMediaId={story}&reelMediaOwnerId={id}&reelId={id}&reelMediaTakenAt={taken_at}&viewSeenAt={taken_at}"
        seen = req.post(url=url6,headers=head4,data=seend_data)
        print(seen.text)
        if seen.status_code == 200:return True
        else:
            return False
    except Exception as SeEr:
        print(SeEr);return False


all_users = [55136743743,51843545585,18306755049,4311753311]        
cookies_done = set_cookies()
if cookies_done==True:
    username = "lolo_brbro"
    ses = "58879943895:pp8I32kjQrwA1b:26:AYc4fPEnnaYMVlpab6kxrneTqeBg0j1KwX8LRaUJkw"
    loginn = send_login(u=username,s=ses)
    if loginn==True:
        for user_id in all_users:
            reels_json = get_reels(myid=user_id)
            cheker = check_reels(json_data=reels_json,myid=user_id)
            if cheker==True:
                story_id = reels_json['reels'][f"{user_id}"]['items'][0]['pk']
                taken_at = story_id = reels_json['reels'][f"{user_id}"]['items'][0]['taken_at']
                seener(id=user_id,story=story_id,taken_at=taken_at)
                sleep(2)
            else:
                continue
    else:
        print('error with "loginn"')
else:
    sys.exit(0)








































