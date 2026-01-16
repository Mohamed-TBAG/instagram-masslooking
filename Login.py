import requests , random;from datetime import datetime;r = requests.Session();global cook;cook = None
class DLogin:
    def __init__(self,username,password,session):
        self.sesion = session;self.username : str = username;self.password : str = password
        self.otp = None;self.factor = None;self.final = None;self.cookies_done = None
        self.cookieslink = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
        self.loginlink   = 'https://i.instagram.com/api/v1/web/accounts/login/ajax/'
        self.twofactor   = 'https://www.instagram.com/accounts/login/ajax/two_factor/'
        self.asbd  = str("".join(random.choice('123456789') for i in range(6 )))
        self.APPID = str("".join(random.choice('123456789')for i in range(16)))
        self.ajax  = str("".join(random.choice('123456789') for i in range(10)))
        self.head = {'asbd':self.asbd,'APPID':self.APPID,'ajax':self.ajax}
    def cook(self):
        try:
            cookies_dict = r.get(self.cookieslink)
            self.csrf = cookies_dict.cookies.get_dict()['csrftoken']
            self.mid = cookies_dict.cookies.get_dict()['mid']
            self.ig_did = cookies_dict.cookies.get_dict()['ig_did']
            self.ig_nrcb = cookies_dict.cookies.get_dict()['ig_nrcb']
            self.main_cookies = cookies_dict.cookies            
            return True
        except: return False
    def seslogin(self):
        if self.cook():
            print('Session Logging in ...')
            try:
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
                    'Cookie':f'csrftoken={self.csrf}; ig_did={self.ig_did}; ig_nrcb={self.ig_nrcb}; mid={self.mid}; sessionid={self.sesion} ',
                    'x-csrftoken': self.csrf,
                    'x-asbd-id':self.asbd,
                    'x-ig-app-id':self.APPID,
                    'x-instagram-ajax':self.ajax
                    }
                login_data = {
                    'username': str(self.username),
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{str(self.password)}',
                    'optIntoOneTap': 'true',
                }
                login_respone = r.post(self.loginlink,headers=login_head,data=login_data,allow_redirects=True)
            except: print('error with setting Login data');return {'logged':'False'}
            try:
                if login_respone.json()["authenticated"] == True:
                    print(f'Login Successfuly as {self.username}')
                    print()
                    global_cookies1 = login_respone.cookies.get_dict()
                    cook = global_cookies1
                    cook.update({'sessionid':self.sesion,'mid':self.mid,'ig_did':self.ig_did,})
                    return {'logged':'True','cook':cook,'head':self.head}
                else:   print('Wrong password Or session');return {'logged':'False'}
            except:
                try:
                    if 'Sorry, your password was incorrect. Please double-check your password.' in  login_respone.text:
                       print('Wrong password `x`');return {'logged':'False'}
                    else:
                        if 'checkpoint_url'  in  login_respone.text:
                            print('check point')
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
                            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
                            'Cookie':f'csrftoken={self.csrf}; ig_did={self.ig_did}; ig_nrcb={self.ig_nrcb}; mid={self.mid}; sessionid={self.sesion} ',
                            'x-csrftoken': self.csrf,
                            'x-asbd-id':self.asbd,
                            'x-ig-app-id':self.APPID,
                            'x-instagram-ajax':self.ajax
                            }
                            asking = r.post(checkpoint_url,headers=header,data={'choice': '1'}) #send the code to email or phone 
                            if 'Select a valid choice.' in asking.text:
                                 asking = r.post(checkpoint_url,headers=header,data={'choice': '0'})
                            try:
                                print('\n'+asking.json()['extraData']['content'][1]['text'] + ' > ')
                                self.otp = input('enter the Secure code : ')
                                challange_send = r.post(checkpoint_url, headers=header, data={'security_code': self.otp} )
                                if 'CHALLENGE_REDIRECTION' in challange_send.text:#resopne of sending secure code
                                    print('code is correct')
                                    login_respone_secure = r.post(self.loginlink,headers=login_head,data=login_data)#login again
                                    self.main_cookies = login_respone_secure.cookies
                                    respone = login_respone_secure.json()
                                    try:
                                        if respone["authenticated"] == True:
                                            print('secure Logged in')
                                            global_cookies3 = login_respone_secure.cookies.get_dict()
                                            cook = global_cookies3
                                            cook.update({'sessionid':self.sesion})
                                            return {'logged':'True','cook':cook,'head':self.head}
                                        else:
                                            print("could not login after vefing code")
                                            return {'logged':'False'}
                                    except:
                                        print('\n An error with code config `F`')
                                        print('\nRestart the program')
                                        return {'logged':'False'}
                                elif 'Please check the code we sent you and try again.' in challange_send.text:
                                    print('the code wrong');return {'logged':'False'}
                                else:   print('An error happened');return {'logged':'False'}
                            except: print('\n An error with code config `x`');print('\nRestart the program');return {'logged':'False'}
                        else:#colud not find authinicated or password is wrong or check point required in respone
                            print('unknown error with the request 1: ');print(login_respone.text);return {'logged':'False'}
                except: print('unknown error with the request 2: ');print(login_respone.text);return {'logged':'False'}
        else:   print('error with setting cookies');return {'logged':'False'}
    def end(self):
        c = self.login()
        if c['logged'] == 'True':   return c
        else:   return {'logged':'False'}
    def ses(self):
        c = self.seslogin()
        if c['logged'] == 'True':   return c
        else:   return {'logged':'False'}
def Login_starter(username,password,session=None):
    if session is not None:
        print();print('DLogin Started')
        v = DLogin(username=username,password=password,session=session).ses()
        if v['logged'] == 'True':   return {'logged':'True','cookies':v['cook'],'requests_session':r,'head':v['head']}
        else:   return {'logged':'False'}
    elif session is None:
        print('DLogin Started')
        v = DLogin(username=username,password=password).end()
        if v['logged'] == 'True':   return {'logged':'True','cookies':v['cook'],'requests_session':r,'head':v['head']}
        else:   return {'logged':'False'}