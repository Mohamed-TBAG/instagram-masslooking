from datetime import datetime
import json
from PyQt5.QtWidgets import *
from datetime import datetime
from time import sleep
import string
from typing import List
import random
'''
fjty.ksmk.bakw
gg66778899

big.blackdik
p66778899

hdvsgsgctvta
p66778899

kajcjeicj
p66778899

mohamedalhabbo


'''
cookies_dict = {}
def login(user,password,se,self):#Done
    time = int(datetime.now().timestamp())
    ajaxlink = 'https://i.instagram.com/api/v1/web/accounts/login/ajax/'
    ajaxdata = se.get(ajaxlink)
    ajax_cookies = ajaxdata.cookies.get_dict()
    try:
        ajax_csrf = ajax_cookies['csrftoken']
    except:
        letters = string.ascii_lowercase
        ajax_csrf = ''.join(random.choice(letters) for i in range(8))

    loin_head = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)","X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/","x-csrftoken": ajax_csrf}
    login_data = {'username': str(user),'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{str(password)}','queryParams': {},'optIntoOneTap': 'false','trustedDeviceRecords':{}}
    loginpost = se.post(ajaxlink,headers=loin_head,data=login_data)
    loginjson = json.loads(loginpost.text)
    login_cookies = loginpost.cookies.get_dict()
    try:
        login_csrf = login_cookies['csrftoken']#ajax respone DONE 
    except:
        login_csrf = ajax_csrf 
    try:
        if loginjson["authenticated"]==True:
            QMessageBox.information(self,'Done','Loged in `FS`')#logid in DONE
            print(loginjson)
            self.tabWidget.setCurrentIndex(1)
            self.pushButton.setVisible(True)
            self.pushButton_2.setVisible(True)
            cookies_dict.clear()
            cookies_dict.update(login_cookies)
        else:
            QMessageBox.warning(self,'Error','✗ Login Failed! `FS`')
            print(loginjson)
    except KeyError:#if cannot find authenticated so it's tow factor
        try:
            if loginjson["two_factor_required"]:
                #turn on and off lines and buttons
                self.lineEdit.setVisible(False)#user
                self.lineEdit_2.setVisible(False)#pass
                self.pushButton_4.setVisible(False)#login button
                self.lineEdit_4.setVisible(True)#code line
                self.pushButton_7.setVisible(True)#tow fac
                QMessageBox.information(self,'wait','Login needs \n two factor code')
                def tow_fac():
                    '''
                    works only if two factor button cliced
                    '''
                    #"cookie": 'ig_did=' + iig_did + '; ig_nrcb=' + iig_nrcb + '; csrftoken=' + ccsrf + '; mid=' + mmid,
                    otp = self.lineEdit_4.text()
                    ccsrf = login_cookies['csrftoken']
                    twofactor_url = 'https://www.instagram.com/accounts/login/ajax/two_factor/'
                    twofactor_payload = {
                    'username': user,'verificationCode': otp,
                    'identifier': loginjson["two_factor_info"]["two_factor_identifier"],
                    'queryParams': {}
                    }
                    twofactor_header = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "application/x-www-form-urlencoded",

                    "origin": "https://www.instagram.com",
                    "referer": "https://www.instagram.com/accounts/login/two_factor?next=%2F",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
                    "x-csrftoken": ccsrf,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "0",
                    "x-instagram-ajax": "00c4537694a4",
                    "x-requested-with": "XMLHttpRequest"
                    }
                    #post after getting two factor code
                    twofacpost = se.post(twofactor_url,headers=twofactor_header,data=twofactor_payload)
                    two_cookies = twofacpost.cookies.get_dict()
                    twofac_json = json.loads(twofacpost.text)
# * ******* * * * ****************************************************************************************************
                    try:
                        if twofac_json['status'] == 'ok':#if two factor code is true so you logged in
                            QMessageBox.information(self,'Done','Loged in x')
                            self.tabWidget.setCurrentIndex(1)
                            self.pushButton.setVisible(True)
                            self.pushButton_2.setVisible(True)
                            cookies_dict.clear()
                            cookies_dict.update(two_cookies)
# * ******* * * * ****************************************************************************************************
                        elif twofac_json['message'] == 'Please check the security code and try again.':#two factor code is wrong
                            QMessageBox.warning(self,'Error','✗ the code is wrong!')
                    except:# تظهر اذا ما لكا ستاتس او مسج بهالحالة
                        try:#حل مشكلة السكيور الذي ياتي بعد التحقق بخطوتين حصرا
                            if loginjson["message"] == "checkpoint_required":
                                #"cookie": 'ig_did=' + ig_did + '; ig_nrcb=' + ig_nrcb + '; csrftoken=' + login_csrf + '; mid=' + mid,
                                self.lineEdit.setVisible(False)#user
                                self.lineEdit_2.setVisible(False)#pass
                                self.pushButton_4.setVisible(False)#login button
                                self.lineEdit_4.setVisible(False)#two fac code line
                                self.pushButton_7.setVisible(False)#tow fac button
                                self.lineEdit_5.setVisible(True)#Secure code line
                                self.pushButton_8.setVisible(True)#Secure button
                                checkpoint_url = 'https://www.instagram.com' + loginjson['checkpoint_url']
                                header = {
                                "accept": "*/*",
                                "accept-encoding": "gzip, deflate, br",
                                "accept-language": "en-US,en;q=0.9",
                                "content-type": "application/x-www-form-urlencoded",
                                "origin": "https://www.instagram.com",

                                "referer": 'https://instagram.com' + loginjson['checkpoint_url'],
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
                                "x-csrftoken": login_csrf,
                                "x-ig-app-id": "936619743392459",
                                "x-ig-www-claim": "0",
                                "x-instagram-ajax": "e8e20d8ba618",
                                "x-requested-with": "XMLHttpRequest"
                                }
                                secure_code = self.lineEdit_5.text()
                                if json.loads(se.post(checkpoint_url, headers=header, data={'security_code': secure_code}).text)['type'] == 'CHALLENGE_REDIRECTION':#resopne of sending secure code
                                    #means login again cuz no more two factor or secure code
                                    login_again = se.post(ajaxlink,headers=loin_head,data=login_data)
                                    again_cookies = login_again.cookies.get_dict()
                                    QMessageBox.information(self,'Done','Loged in y')
#*****************************************
                                    print(again_cookies)
                                    cookies_dict.clear()
                                    cookies_dict.update(again_cookies)
                                else:#means an error ouccord after two fac and secure code
                                    QMessageBox.warning(self,'Error','✗ Login Failed! z')
                                    quit()
                                    #login field for many reasons
                        except:
                            QMessageBox.warning(self,'Error','✗ Login Failed! c')
                            QApplication.processEvents()

                            quit()
                self.pushButton_7.clicked.connect(tow_fac)
        except KeyError:
            try:
                #"cookie": 'ig_did=' + ig_did + '; ig_nrcb=' + ig_nrcb + '; csrftoken=' + login_csrf + '; mid=' + mid,
                if loginjson["message"] == "checkpoint_required":#secure direct
                    QApplication.processEvents()
                    checkpoint_url = 'https://www.instagram.com' + loginjson['checkpoint_url']
                    header = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://www.instagram.com",
                    "referer": 'https://instagram.com' + loginjson['checkpoint_url'],
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
                    "x-csrftoken": login_csrf,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "0",
                    "x-instagram-ajax": "e8e20d8ba618",
                    "x-requested-with": "XMLHttpRequest"
                    }
                    asking = se.post(checkpoint_url,headers=header,data={'choice': '1'}).text #send the code to email or phone 
                    json_ask = json.loads(asking)['extraData']['content'][1]['text'] + ' > '
                    QMessageBox.information(self,'Wait!',str(json_ask))
                    self.lineEdit.setVisible(False)#user
                    self.lineEdit_2.setVisible(False)#pass
                    self.pushButton_4.setVisible(False)#login button
                    self.lineEdit_4.setVisible(False)#two fac code line
                    self.pushButton_7.setVisible(False)#tow fac button
                    self.lineEdit_5.setVisible(True)#Secure code line
                    self.pushButton_8.setVisible(True)#Secure button
                    #set try
                    def checkpoint():
                        secure_code2 = self.lineEdit_5.text()

                        challange_send = se.post(checkpoint_url, headers=header, data={'security_code': secure_code2} )
                        challange_json = json.loads(challange_send.text)
                        challange_cook = challange_send.cookies.get_dict()
                        print(challange_json)
                        try:
                            if challange_json['type'] == 'CHALLENGE_REDIRECTION':#resopne of sending secure code
                                again_head = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)","X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/","x-csrftoken": challange_cook['csrftoken']}
                                login_again = se.post(ajaxlink,headers=again_head,data=login_data)#ReLogin after ByPass Secure
                                again_json = (login_again.text)
                                again_cookies2 = login_again.cookies.get_dict()
                                try:
                                    if json.loads(again_json)["authenticated"]==True:
                                        QMessageBox.information(self,'Done','Loged in `CH`')
                                        self.tabWidget.setCurrentIndex(1)
                                        self.pushButton.setVisible(True)
                                        self.pushButton_2.setVisible(True)
                                        print(again_cookies2)
                                        cookies_dict.clear()
                                        cookies_dict.update(again_cookies2)
                                    else:
                                        QMessageBox.warning(self,'Error','✗ Login Failed! `FK`')
                                        print(again_json)
                                        quit()
                                except KeyError as kk:
                                    QMessageBox.warning(self,'Error',str(kk))
                                    print(again_json)
                            else:
                                QMessageBox.warning(self,'Error','✗ Login Failed! \n Secure Error')
                                quit()
                        except Exception as Ch:
                            QMessageBox.warning(self,'ErCH',str(Ch))
                    self.pushButton_8.clicked.connect(checkpoint)
            except Exception as err:
                QMessageBox.warning(self,'Error',str(err))
                QApplication.processEvents()
                quit()


def grabber_v1(se,self):
    '''
     1 session
     2 cookies dictunary
     3 self = the main calss
     return list of fowllowers ids
    '''

    ides_list = []
    page = self.lineEdit_3.text() #username from text edit
    csrf = cookies_dict['csrftoken']
    idurl = f"https://www.instagram.com/{page}/?__a=1&__d=dis" #get all info about the page
    try:
        try:
            uid = se.get(idurl)
            account_json = json.loads(uid.text)
            id = account_json["graphql"]["user"]["id"]#get page id
            #followers_count = int(account_json["graphql"]["user"]["edge_followed_by"]["count"])#get pae followers coun
        except:
            QMessageBox.information(self,'Error','user error')
            print(uid.text)
        limit = int(self.lineEdit_6.text()) #max users to grab
        users_count = 24 #start from that number of user list in insta databases
        #getting first end_cursor
        end_ucrsor_url = f'https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={id}&first=12&after='
        end_ucrsor_data = {'query_id':'17851374694183129', 'id':str(id), 'first':'1', 'after':''}
        end_curso_headers = {
        "accept": "'text/html,application/xhtml+xml,application/xml;q=0.9','image/avif,image/webp','image/apng','*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'",
        "accept-encoding": "'gzip', 'deflate', 'br'",
        "accept-language": "'en-GB','en-US;q=0.9','en;q=0.8','ar;q=0.7'",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }
        end_ucrsor_get = se.get(end_ucrsor_url,headers=end_curso_headers,data=end_ucrsor_data).json()
        end_curso = []
        try:
            first_end_cursor = end_ucrsor_get["data"]["user"]["edge_followed_by"]["page_info"]["end_cursor"]
            end_curso.append(first_end_cursor)
        except Exception as er3:
            QMessageBox.information(self,'Er`END`',str(er3))
            print(end_ucrsor_get)
        def stop_grabbing():#to stop grabber
            limit = users_count
        self.pushButton_9.clicked.connect(stop_grabbing)#stop grabbing button
        while limit > users_count:
            followers_url = f'https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={id}&first=12&after={str(end_curso[0])}'
            followers_data = {'query_id':'17851374694183129' , 'id':str(id) , 'first':str(users_count) , 'after':str(end_curso[0])}
            followers_headers = {
            'referer': f'https://www.instagram.com/{page}/followers/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '464',
            'x-asbd-id': '198387',
            'x-csrftoken': str(csrf),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3U9SgkUz2nZg_Jx4m0AQA2dLs7aqjooR_FknrkUz-uknd6',
            'x-requested-with': 'XMLHttpRequest'
            }
            users_count+=12
            self.lcdNumber.display(users_count)
            friendships = se.get(followers_url,headers=followers_headers,cookies=cookies_dict,data=followers_data,allow_redirects=True)
            friendships_json = json.loads(friendships.text)
            try:
                next_end_cursor = friendships_json["data"]["user"]["edge_followed_by"]["page_info"]["end_cursor"]
                end_curso.clear()
                end_curso.append(next_end_cursor)
                all_users_info = friendships_json["data"]["user"]["edge_followed_by"]["edges"]
                for user in all_users_info:
                    user_id = user['node']['id']
                    ides_list.append(user_id)
                    print(user_id)
            except Exception as er5:
                QMessageBox.information(self,'Err`CU`',str(er5))
                print(friendships_json)
    except Exception as e1:
        QMessageBox.information(self,'Err`AL`','Account Blocked')
    return ides_list


def story_id_grabber(users,se,self):
    '''
     1 list of users ids
     2 cookies dictunary
     3 se=requests.Session the live session
     4 self = the main calss
     no return
     DONE
    '''
    time = int(datetime.now().timestamp())
    csrf = cookies_dict['csrftoken']
    user_count = len(users[0])-1
    seen_counter = 0
    errors_counter = 0
    try:
        for user in range(0,user_count):
            reel_ids_header = {
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-asbd-id': '198387',
            'x-csrftoken': str(csrf),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR138DLpld0LEwpFvvo7XfnJefyH4qGbHU_VOAXBC4linQVa',
            'x-requested-with': 'XMLHttpRequest'
            }
            reel_ids_data = {'reel_ids':str(users[0][user])}
            reel_ids_url = f'https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={users[0][user]}'
            reel_ids_get = se.get(reel_ids_url,headers=reel_ids_header,data=reel_ids_data,cookies=cookies_dict,allow_redirects=True).json()
            if reel_ids_get == {}:
                continue
            else:
                try:
                    if reel_ids_get["reels"] == {}:
                        continue
                    else:
                        items = reel_ids_get["reels"][users[0][user]]["items"]
                        items_count = len(items)-1
                        for item in range (0,items_count):
                            stid = items[item]["pk"]
                            seen_data = {'reelMediaId':str(stid),'reelMediaOwnerId':str(users[0][user]),'reelId':str(users[0][user]),'reelMediaTakenAt':str(time),'viewSeenAt':str(time)}
                            seen_headers = {'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
                                'content-type': 'application/x-www-form-urlencoded',
                                'origin': 'https://www.instagram.com',
                                'sec-ch-prefers-color-scheme': 'dark',
                                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                                'x-asbd-id': '198387',
                                'x-csrftoken': str(csrf),
                                'x-ig-app-id': '936619743392459',
                                'x-requested-with': 'XMLHttpRequest'}
                            seen_url = 'https://www.instagram.com/api/v1/stories/reel/seen'
                            seen_post = se.post(seen_url,headers=seen_headers,data=seen_data,allow_redirects=True).json()
                            try:
                                if seen_post["status"]=="ok":
                                    print('\n seen')
                                    seen_counter+=1
                                    self.lcdNumber_2.display(seen_counter)
                                    QApplication.processEvents()
                                else:
                                    errors_counter +=1
                                    self.lcdNumber_3.display(errors_counter)
                                    QApplication.processEvents()
                            except Exception as seenERR:
                                QMessageBox.information(self,'Er`SE`',str(seenERR))
                except Exception as erIT:
                    QMessageBox.information(self,'Err`IT`',str(erIT))
    except Exception as errW:
        QMessageBox.information(self,'Err`WR`',str(errW))
