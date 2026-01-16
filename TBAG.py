print('''


_________    _______       ________       _______     
/________/\ /_______/\     /_______/\     /______/\    
\__.::.__\/ \::: _  \ \    \::: _  \ \    \::::__\/__  
   \::\ \    \::(_)  \/_    \::(_)  \ \    \:\ /____/\ 
    \::\ \    \::  _  \ \    \:: __  \ \    \:\\_  _\/ 
     \::\ \    \::(_)  \ \    \:.\ \  \ \    \:\_\ \ \ 
      \__\/     \_______\/     \__\/\__\/     \_____\/ 
      
                TBAG MASSLOOKING TOOL V9
      
      
      ''');print();print()
try:    import json;import Login;import Stories;lg = Login;st = Stories
except: print('cannot import libraries or tool files')
try:
    username= json.load(open('data.json', 'r'))["username"]
    password= json.load(open('data.json', 'r'))["password"]
    session= json.load(open('data.json', 'r'))["session"]
except: print('cannot load login info')
dict = lg.Login_starter(password=password,username=username,session=session)
if dict['logged']=='True':
    cookies_dict = dict['cookies'];requ = dict['requests_session'];head = dict['head']
    users_file = open('userS.txt','r');users = users_file.readlines()
    cnt = int(len(users));allusers = []
    for user in range(0,cnt):
        u = users[user]
        if u != '' and u!= ' ' and u != '\n' and u != ' \n' and u != '\n ':
            if u != '' or u!= ' ' or u != '\n' or u != ' \n' or u != '\n ':
                try:    allusers.append(u.replace("\n", ""))
                except: continue
            else:   continue
        else:   continue
    users_file.close();print(f'grabbed ( {len(allusers)} )');print()
    idss  = allusers;users = allusers;req2  = requ;cook2 = cookies_dict
    tray  = st.starter(cook=cook2,req=req2,head=head,ids=idss)
else:   pass
