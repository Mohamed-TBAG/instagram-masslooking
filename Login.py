import requests , random
from datetime import datetime
r = requests.Session()
global cook
cook = None
class DLogin:
    def __init__(self,username,password):
        self.username : str = username
        self.password : str = password
        self.otp = None
        self.factor = None
        self.final = None
        self.cookies_done = None
        self.cookieslink = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
        self.loginlink   = 'https://i.instagram.com/api/v1/web/accounts/login/ajax/'
        self.twofactor   = 'https://www.instagram.com/accounts/login/ajax/two_factor/'
        #self.securelink = 'https://www.instagram.com' + loginjson['checkpoint_url']
        self.asbd  = str("".join(random.choice('123456789') for i in range(6 )))
        self.APPID = str("".join(random.choice('123456789')for i in range(16)))
        self.ajax  = str("".join(random.choice('123456789') for i in range(10)))
        self.head = {'asbd':self.asbd,'APPID':self.APPID,'ajax':self.ajax}
    def cook(self):
        main_headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
        'x-asbd-id':self.asbd,
        'x-ig-app-id':self.APPID,
        'x-instagram-ajax':self.ajax
        }
        try:
            cookies_dict = r.get(self.cookieslink)
            self.csrf = cookies_dict.cookies.get_dict()['csrftoken']
            self.mid = cookies_dict.cookies.get_dict()['mid']
            self.ig_did = cookies_dict.cookies.get_dict()['ig_did']
            self.ig_nrcb = cookies_dict.cookies.get_dict()['ig_nrcb']
            self.main_cookies = cookies_dict.cookies
            return True
        except:
            return False
    def login(self):
        if self.cook():
            print('Logging in ...')
            login_head = {
                'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
                'Referer': 'https://www.instagram.com/',
                'accept':'*/*',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'sec-ch-ua':'"Chromium";v="105"',
                'sec-ch-ua-mobile':'?1',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-site',
                'Cookie':f'csrftoken={self.csrf}; ig_did={self.ig_did}; ig_nrcb={self.ig_nrcb}; mid={self.mid}',
                'x-csrftoken': self.csrf,
                'x-asbd-id':self.asbd,
                'x-ig-app-id':self.APPID,
                'x-instagram-ajax':self.ajax
                }
            login_data = {
                'username': str(self.username),
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{str(self.password)}',
                'optIntoOneTap': 'false',
            }
            login_respone = r.post(self.loginlink,headers=login_head,data=login_data,allow_redirects=True)
            try:
                if login_respone.json()["authenticated"] == True:
                    print(f'Login Successfuly as {self.username}')
                    global_cookies1 = login_respone.cookies.get_dict()
                    cook = global_cookies1
                    return {'logged':'True','cook':cook,'head':self.head}
                else:
                    print(login_respone.json())
                    return {'logged':'False'}
            except KeyError:#if cannot find authenticated so it's tow factor
                try:
                    if login_respone.json()["two_factor_required"]:
                        print('\nTow factor code required')
                        self.factor : str = input('\nEnter Tow-Factor Code : ')
                        twofactor_payload = {
                            'username': self.username,'verificationCode': self.factor,
                            'identifier': respone["two_factor_info"]["two_factor_identifier"],
                            }
                        twofactor_header = {
                            'accept':'*/*',
                            'accept-encoding':'gzip, deflate, br',
                            'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                            'sec-ch-ua':'"Chromium";v="105"',
                            'sec-ch-ua-mobile':'?1',
                            'sec-fetch-dest':'empty',
                            'sec-fetch-mode':'cors',
                            'sec-fetch-site':'same-site',
                            'Cookie':f'csrftoken={self.csrf}; ig_did={self.ig_did}; ig_nrcb={self.ig_nrcb}; mid={self.mid}',
                            'x-csrftoken': self.csrf,
                            'x-asbd-id':self.asbd,
                            'x-ig-app-id':self.APPID,
                            'x-instagram-ajax':self.ajax,
                            'origin': 'https://www.instagram.com',
                            'referer': 'https://www.instagram.com/accounts/login/two_factor?next=%2F',
                            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                            'x-ig-www-claim': '0',
                            }
                        twofacpost = r.post(self.twofactor,headers=twofactor_header,data=twofactor_payload,allow_redirects=True)
                        try:
                            twofac_json = twofacpost.json()
                            if twofac_json['status'] == 'ok':#if two factor code is true so you logged in
                                print('Logged in')
                                global_cookies2 = twofacpost.cookies.get_dict()
                                cook = global_cookies2
                                return {'logged':'True','cook':cook,'head':self.head}
                            elif twofac_json['message'] == 'Please check the security code and try again.':#two factor code is wrong
                                print('\nThe code is Incurrect !!!')
                                print(f'\nRestart the Program')
                                return {'logged':'False'}
                        except:#if Checkpoint after two factow
                            print('\nError After Sending Two factor code')
                            print(f'\nRestart the Program')
                    elif login_respone.json()["message"] == "checkpoint_required":#secure direct
                        checkpoint_url = 'https://www.instagram.com' + login_respone.json()['checkpoint_url']
                        header = {
                        'accept':'*/*',
                        'accept-encoding':'gzip, deflate, br',
                        'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                        'origin': 'https://www.instagram.com',
                        'referer': 'https://instagram.com' + login_respone.json()['checkpoint_url'],
                        'sec-fetch-dest':'empty',
                        'sec-fetch-mode':'cors',
                        'sec-fetch-site':'same-site',
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
                        'Cookie':f'csrftoken={self.csrf}; ig_did={self.ig_did}; ig_nrcb={self.ig_nrcb}; mid={self.mid}',
                        'x-csrftoken': self.csrf,
                        'x-asbd-id':self.asbd,
                        'x-ig-app-id':self.APPID,
                        'x-instagram-ajax':self.ajax,
                        }
                        asking = r.post(checkpoint_url,headers=header,data={'choice': '1'}).text #send the code to email or phone 
                        try:
                            print('\n'+asking.json()['extraData']['content'][1]['text'] + ' > ')
                            self.otp = input('enter the Secure code : ')
                            challange_send = r.post(checkpoint_url, headers=header, data={'security_code': self.otp} )
                            if challange_send.json()['type'] == 'CHALLENGE_REDIRECTION':#resopne of sending secure code
                                login_respone_secure = r.post(self.loginlink,headers=login_head,data=login_data)
                                self.main_cookies = login_respone_secure.cookies
                                respone = login_respone_secure.json()
                                try:
                                    if respone["authenticated"] == True:
                                        print('Logged in')
                                        global_cookies3 = login_respone_secure.cookies.get_dict()
                                        cook = global_cookies3
                                        return {'logged':'True','cook':cook,'head':self.head}
                                except:
                                    print('\n An error with code config `F`')
                                    print('\nRestart the program')
                                    return {'logged':'False'}
                            else:
                                    print('\nYour code is Wrong `x`')
                                    print('\nRestart the program')
                                    return {'logged':'False'}
                        except:
                            print('\n An error with code sending `L`')
                            print('\nRestart the program ')
                            return {'logged':'False'}
                except:#non of data found #error
                    print('\nError with Login respone'.upper())
                    print(f'\nRestart the Program'.upper())
                    return {'logged':'False'}
        else:
            print('Error with setting Cookies')
            return {'logged':'False'}
    def end(self):
        c = self.login()
        if c['logged'] == 'True':
            return c
        else:
            return {'logged':'False'}
def Login_starter(username,password):
    print('started')
    v = DLogin(username=username,password=password).end()
    if v['logged'] == 'True':
        return {'logged':'True','cookies':v['cook'],'requests_session':r,'head':v['head']}
    else:
        return {'logged':'False'}