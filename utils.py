FACTOR = 0.8
FACTOR2 = 0.1
import os

login_info = {
    "username": os.getenv("INSTAGRAM_USERNAME", "hdvsgsgctvta"), # Fallback to hardcoded for now, but recommend env var
    "password": os.getenv("INSTAGRAM_PASSWORD", "pp66778899")
}

accouts_with_usernames = {
    # "64260258127":"onlysakara0",
    # "1085949299":"falafel.iraqia",
    # "10145626786":"kolaliraq",
    # "1176007323":"so_nice11",
    "61723332116":"the.lady5",
    # "61723332116":"aya.bast"

}
random_hashtags = ["instagram", "women", "man", "memes", "anime",
                   "apple", "apple", "samsung", "jokes", "العراق", "السعودية",
                   "مصر", "usa", "realmadrid", "love", "food", "ميمز",
                   "سوريا", "gym", "اكسبلور", "تصميم", "cars", "لايك",
                   "viral", "fyp"]
behaviour_accounts = [
    "realmadrid", "433", "sharqiyatv", "fhedan_s", "mzajeat", "wasted",
    "9gag", "brfootball", "kolaliraq", "themadridviews",
    "celebrities_iqmag", "bocoob", "ziyad.matti", "hard.images",
    "truthuncovered_", "uuub", "offdatmemes", "1001.stream", "naltaki1"]
BoolianChoices = [True, False, False, False, False, False,
             False, False, False, True, False, False, False]
do_or_not = [True, False, False, False]
next_button = "_aaqg"
first_post_classname = """_aagw"""
instagram_url = "https://www.instagram.com/"
qraphql_url = instagram_url+"api/graphql"
query_url = instagram_url+"graphql/query"
friendships_url = instagram_url+"api/v1/friendships/{}/followers/?count=25&search_surface=follow_list_page&max_id={}"
comments_url = instagram_url+"/api/v1/media/{}/comments/?can_support_threading=true&permalink_enabled=false"
likers_url = instagram_url+"/api/v1/media/{}/likers/"
def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

DB_LOCATION = 'user_max_id.db'
USERS_TXT_LOCATION = 'users.txt'
CREATE_TABLE1_Q = '''CREATE TABLE IF NOT EXISTS user_max_id (user_id TEXT PRIMARY KEY, max_id TEXT)'''
CREATE_TABLE2_Q = '''CREATE TABLE IF NOT EXISTS PostsScraper (user_id TEXT PRIMARY KEY, max_id TEXT)'''
CREATE_TABLE3_Q = '''CREATE TABLE IF NOT EXISTS Posts (user_id TEXT, shortcode TEXT, likesscraped BOOLEAN DEFAULT 0, commentsscraped BOOLEAN DEFAULT 0, PRIMARY KEY (user_id, shortcode))'''
SELECT_MAXID_Q = 'SELECT max_id FROM user_max_id WHERE user_id = ?'
SELECT_POST_Q = 'SELECT shortcode FROM Posts WHERE commentsscraped = 0 AND user_id = ?'
SELECT_POST2_Q = 'SELECT shortcode FROM Posts WHERE likesscraped = 0 AND user_id = ?'
INSERT_SHORT_CODE_Q = 'INSERT OR IGNORE INTO Posts (user_id, shortcode) VALUES (?, ?)'
SELECT_LAST_MAXID_Q = 'SELECT max_id FROM PostsScraper WHERE user_id = ?'
INSERT_MAXID_Q = 'INSERT OR REPLACE INTO user_max_id (user_id, max_id) VALUES (?, ?)'
INSERT_MAXID2_Q = 'INSERT OR REPLACE INTO PostsScraper (user_id, max_id) VALUES (?, ?)'
SET_COMMENTS_SCRAPED = "UPDATE Posts SET commentsscraped = 1 WHERE user_id = ? AND shortcode = ?"
SET_LIKES_SCRAPED = "UPDATE Posts SET likesscraped = 1 WHERE user_id = ? AND shortcode = ?"
stats_output_message = "time = {} || stories = {} || accounts = {} || stories grabs = {} || accounts grabs = {} || comments grabs = {} || likes grabs = {} || errors = {}"
HEAD1 = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'x-ig-app-id':'5607738976007515','accept': '*/*',
    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'i.instagram.com','Connection': 'keep-alive',
    'origin':  'https://www.instagram.com'
    }  
HEAD2 = {
    "Sec-Ch-Ua": '";Not A Brand";v="99", "Chromium";v="94"',
    "X-Ig-App-Id": '',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Fb-Friendly-Name": "PolarisStoriesV3ReelPageStandaloneQuery",
    "X-Fb-Lsd": "",
    "Sec-Ch-Ua-Platform-Version": '"10.0.0"',
    "x-bloks-version-id": '',
    "X-Asbd-Id": '359341',
    "Content-Type": "application/x-www-form-urlencoded",
    "Sec-Ch-Prefers-Color-Scheme": "dark",
    "Sec-Ch-Ua-Model": "",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept": "*/*",
    "Origin": "https://www.instagram.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": instagram_url,
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
    }

allowed_params = ["av", "__d", "__user", "__a", "__req", "__hs", "dpr",
                          "__ccg", "__rev", "__s", "__hsi", "__dyn", "__csr",
                          "__comet_req", "fb_dtsg", "jazoest", "lsd", "__spin_r",
                          "__spin_b", "__spin_t", "__hsdp", "__hblp", "__crn"]
SEEN_PAYLOAD = {
    'doc_id': '8056053547846061',
    'fb_api_req_friendly_name':'PolarisStoriesV3SeenMutation',
    'fb_api_caller_class': 'RelayModern',
    
    }
GRABBER_PAYLOAD = {
    'doc_id': '9342251469147045',
    'fb_api_req_friendly_name':'PolarisStoriesV3ReelPageStandaloneQuery',
    'fb_api_caller_class': 'RelayModern'
    }
POSTS_GRABBER_PAYLOAD = {
    'fb_api_req_friendly_name': 'PolarisProfilePostsQuery',
    'fb_api_caller_class': 'RelayModern',
    "doc_id":"9333503846778781"
    }

POSTS_GRABBER_VARIABLES = {
        "before":None,
        "data":{
            "count":12,
            "latest_reel_media":True},
        "first":12,
        "last":None,
        "__relay_internal__pv__PolarisIsLoggedInrelayprovider":True,
        "__relay_internal__pv__PolarisShareSheetV3relayprovider":True
        }