import re,requests,random;from datetime import datetime
csrf_pattern = r'''csrf_token\\":\\"(.*?)\\",'''
datr_pattern = r'''"_js_datr":{"value":"(.*?)",'''
device_pattern = r'''","device_id":"(.*?)",'''
ig_did_pattern = r'''_js_ig_did":{"value":"(.*?)",'''
h1 = {
    'Host': 'www.instagram.com',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '""',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'

}
response = requests.get('https://www.instagram.com/',headers=h1)
csrf = re.findall(csrf_pattern, response.text)[0]
datr = re.findall(datr_pattern , response.text)[0]
first_ig_did = re.findall(ig_did_pattern , response.text)[0]
headers = {
    'Host': 'www.instagram.com',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': '0',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36',
    'Viewport-Width': '958',
    'Accept': '*/*',
    'Sec-Ch-Ua-Platform-Version': '""',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Asbd-Id': '129477',
    'X-Web-Device-Id': first_ig_did,
    'X-Csrftoken': csrf,
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua-Platform': '""',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
    }
url_landing = 'https://www.instagram.com/api/v1/public/landing_info/'
respone2 = requests.get(url=url_landing,headers=headers)
mid = respone2.cookies.get_dict()['mid']
login_header = {
    'Host': 'www.instagram.com',
    'Cookie': f'ig_nrcb=1; datr={datr}; mid={mid}; ig_did={first_ig_did}; csrftoken={csrf}',
    'Content-Length': '364',
    'X-Ig-Www-Claim': '0',
    'Sec-Ch-Ua-Platform-Version': '""',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Web-Device-Id': first_ig_did,
    'X-Csrftoken': csrf,
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua-Platform': '""',
    'X-Ig-App-Id': '936619743392459',
    'Sec-Ch-Ua-Mobile': '?0',
    #X-Instagram-Ajax: 1007660890
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36',
    'Viewport-Width': '958',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Asbd-Id': '129477',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': r'https://www.instagram.com/accounts/login/?next=%2F&source=desktop_nav',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
username = "mohamedbrbro"
password = "p66778899"
login_data = {"username": username,"optIntoOneTap": "true","queryParams": "{}",
    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:p66778899"}
login_url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
login_respone = requests.post(url=login_url,headers=login_header,data=login_data)
csrf = login_respone.cookies.get_dict()["csrftoken"]
rur = login_respone.cookies.get_dict()["rur"]
ds_user_id = login_respone.cookies.get_dict()["ds_user_id"]
session = login_respone.cookies.get_dict()["sessionid"]
ig_did = login_respone.cookies.get_dict()["ig_did"]
cookies = f'ig_nrcb=1; datr={datr}; mid={mid}; ig_did={ig_did}; csrftoken={csrf}; rur={rur}; ds_user_id={ds_user_id}; sessionid={session}'
login_header = {
    'Host': 'www.instagram.com',
    'Cookie': cookies,
    'Content-Length': '364',
    'X-Ig-Www-Claim': '0',
    'Sec-Ch-Ua-Platform-Version': '""',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Web-Device-Id': ig_did,
    'X-Csrftoken': csrf,
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua-Platform': '""',
    'X-Ig-App-Id': '936619743392459',
    'Sec-Ch-Ua-Mobile': '?0',
    #X-Instagram-Ajax: 1007660890
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36',
    'Viewport-Width': '958',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Asbd-Id': '129477',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/accounts/login/?next=%2F&source=desktop_nav',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
bz_url = "https://www.instagram.com/ajax/bz?__d=dis" 

bz_data = 'q=[{"app_id":"936619743392459","device_id":"'+str(ig_did)+'","frontend_env":"C2e","posts":[["ods:incr",{"key":"web.app_id.same.936619743392459.client.server"},'+str(datetime.now().timestamp())+',0]]}]&ts='+str(datetime.now().timestamp())
bz_respone = requests.post(url=bz_url,data=bz_data,headers=login_header)
shbid = bz_respone.cookies.get_dict()["shbid"]
shbts = bz_respone.cookies.get_dict()["shbts"]
cookies = f'ig_nrcb=1; datr={datr}; mid={mid}; ig_did={ig_did}; csrftoken={csrf}; rur={rur}; ds_user_id={ds_user_id}; sessionid={session}; shbid={shbid}; shbts={shbts}'

# loged in and time for seen
h2 = h1.copy();h2.update({"Cookie":cookies})
response_after = requests.get('https://www.instagram.com/',headers=h2)
# grabbing graph parameters
# unknow
# &__dyn=7xeUmwlEnwn8K2WnFw9-2i5U4e0yoW3q32360CEbo1nEhw2nVE4W0om78b87C0yE5ufz81s8hwGwQw9m1YwBgao6C0Mo5W3e9x-0z8-U2zxe2Gew9O22362W2K0zK5o4q3y1Sx_w4HwJwSyES1Twoob82cwMwrUdUbGwmk1xwmo6O0A8bU&
# &__csr=g8cbMDkjsldR8DSzRkLfkzp5H9Z6HFeQh4VOrRChdGUTy9US-GyAFqHGjuECswGcFaiXAhk9yXhb_G-az4dCxq8LU03_Dg0rqw1W2S18yy0MK8O0jUkwAzcE4y0qq0pe1mzU1lA2W17Am2R0cOA1Ayiiw46yi00rkE&

# &__s=:u377d3:dfz23d&    random
# &jazoest=26334& random



#doc_id = https://static.cdninstagram.com/rsrc.php/v3iFyD4/yi/l/makehaste_jhash/kJcrDt23An2anVzA6ibaF6yoJwpKQHMniosq8QdVLHB0K74iwRhj6xLFUnxwQHdw03zi78yvgqaUkuxuudF93H5csnjinQZZQ8Iv9GrDmZzO28fqguBN3umAE8Bl2bmn551VnHbqFYIgeTXxrrhwKACP4LurKmycjQgOh1R4nn_yIji6Fv958ldaDS-RPbTp2QkXwF9RU7CWkVXkSFo3QXoO4UR4AXhiUPWTERFl_vegNtnVKFtTQtSFFRT_fwIfbhesA0nxo6lf02xYjoMXrQNzQRHUuj5O9h0txBmGovV1VFko4xJzvsWqehdEtWwDQVEH-g-FDC.js?_nc_x=Ij3Wp8lg5Kz

_av_pattern = r'{"accessToken":"","actorID":"(.*?)",'
_hs_pattern = r',"haste_session":"(.*?)",'
_rev_pattern = r',\[{"consistency":{"rev":(.*?)},' 
_spin_r_pattern = r',"__spin_r":(.*?),"__spin_b'
_hsi_pattern = r'''qplTimingsServerJS",null,null,\["(.*?)",'''
_spin_t_pattern = r'","__spin_t":(.*?),'
_fb_pattern = r',{"token":"(.*?)"},'
_lsd_pattern = r'\["LSD",\[\],{"token":"(.*?)"}'
__av = re.findall(_av_pattern,response_after.text)[0]
__hs = re.findall(_hs_pattern,response_after.text)[0]
__rev = re.findall(_spin_r_pattern,response_after.text)[0] 
_spin_r = re.findall(_spin_r_pattern,response_after.text)[0]
_hsi = re.findall(_hsi_pattern,response_after.text)[0]
_spin_t = re.findall(_spin_t_pattern,response_after.text)[0]
fb = re.findall(_fb_pattern,response_after.text)[0]
lsd = re.findall(_lsd_pattern,response_after.text)[0]
#print(__av);print();print(__hs);print();print(__rev);print();print(_spin_r);print();print(_hsi);print();print(_spin_t);print();print(fb);print();print(lsd);
head1 = {
    'Host': 'www.instagram.com',
    'Cookie': cookies,
    'Content-Length': '1070',
    'X-Ig-App-Id': '936619743392459',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36',
    'Viewport-Width': '1920',
    'X-Fb-Friendly-Name': 'PolarisAPIReelSeenMutation',
    'X-Fb-Lsd': lsd,
    'Sec-Ch-Ua-Platform-Version': '""',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': csrf,
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua-Platform': '""',
    'Accept': '*/*',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
paylod = f'av={__av}&__d=www&__user=0&__a=1&__req=p&__hs={__hs}&dpr=1&__ccg=GOOD&__rev={__rev}&__s=%3Aap8eoz%3Avy6pvf&__hsi={_hsi}&__dyn=0&__csr=0&__comet_req=7&fb_dtsg={fb}&jazoest=26457&lsd={lsd}&__spin_r={_spin_r}&__spin_b=trunk&__spin_t={_spin_t}&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisAPIReelSeenMutation&variables=%7B%22reelId%22%3A%2245504629732%22%2C%22reelMediaId%22%3A%223125049456935510454%22%2C%22reelMediaOwnerId%22%3A%2245504629732%22%2C%22reelMediaTakenAt%22%3A1686754941%2C%22viewSeenAt%22%3A1686829308%7D&server_timestamps=true&doc_id=23911865525071060'
url = 'https://www.instagram.com/api/graphql'
x=0
while True:
    req = requests.post(url=url,headers=head1,data=paylod)
    print(req.text)
    if x==100:break
    else:x+=1



# h1 = {
#                 'Host': 'www.instagram.com',
#                 'Sec-Ch-Ua-Mobile': '?0',
#                 'Sec-Ch-Ua-Platform': '""',
#                 'Upgrade-Insecure-Requests': '1',
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#                 'Sec-Fetch-Site': 'none',
#                 'Sec-Fetch-Mode': 'navigate',
#                 'Sec-Fetch-User': '?1',
#                 'Sec-Fetch-Dest': 'document',
#                 'Accept-Encoding': 'gzip, deflate',
#                 'Accept-Language': 'en-US,en;q=0.9',
#                 'Connection': 'close',
#                 "Cookie":self.cookies
#                 }
#             response_after = self.r.get('https://www.instagram.com/',headers=h1)
#             _av_pattern = r'{"accessToken":"","actorID":"(.*?)",'
#             _hs_pattern = r',"haste_session":"(.*?)",'
#             _rev_pattern = r',\[{"consistency":{"rev":(.*?)},' 
#             _spin_r_pattern = r',"__spin_r":(.*?),"__spin_b'
#             _hsi_pattern = r'''qplTimingsServerJS",null,null,\["(.*?)",'''
#             _spin_t_pattern = r'","__spin_t":(.*?),'
#             _fb_pattern = r',{"token":"(.*?)"},'
#             _lsd_pattern = r'\["LSD",\[\],{"token":"(.*?)"}'
#             self.__av = re.findall(_av_pattern,referer_respone.text)[0]
#             self.__hs = re.findall(_hs_pattern,referer_respone.text)[0]
#             self.__rev = re.findall(_spin_r_pattern,referer_respone.text)[0] 
#             self._spin_r = re.findall(_spin_r_pattern,referer_respone.text)[0]
#             self._hsi = re.findall(_hsi_pattern,referer_respone.text)[0]
#             self._spin_t = re.findall(_spin_t_pattern,referer_respone.text)[0]
#             self.fb = re.findall(_fb_pattern,referer_respone.text)[0]
#             self.lsd = re.findall(_lsd_pattern,referer_respone.text)[0]
referer_respone