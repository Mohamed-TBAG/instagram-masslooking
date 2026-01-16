import Login
import Grabber
import Story_id

lg = Login
gr = Grabber
st = Story_id
dict = lg.Login_starter(password='zxdzxd123',username='zxdh.p1') # equal  {'logged':'True','cookies':v['cook'],'requests_session':r,'head':v['head']}
if dict['logged']=='True':
    print('Yes')
    cookies_dict = dict['cookies']
    requ = dict['requests_session']
    head = dict['head']
    grab = gr.Grabber_starter(cook=cookies_dict,req=requ) # equal {'grabbed':'True','ids':self.ides_list,'users':self.user_username,'requests_session':self.req,'cookies':self.cook}
    if grab['grabbed'] == 'True':
        print('grabbed')
        print()
        idss= grab ['ids']
        users=grab['users']
        req2=grab['requests_session']
        cook2=grab['cookies']
        tray = st.starter(cook=cook2,req=req2,head=head,users=users,ids=idss)
    else:
        print('no')
else:
    print('No')
