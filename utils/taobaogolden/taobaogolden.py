#coding=utf-8
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
  

hostUrl = "https://login.taobao.com/member/login.jhtml" 
#此处不明白，不知道下载cookie主机地址，因此使用登录界面地址
 
tbLoginUrl = "https://login.taobao.com/member/login.jhtml"
 
tbGetGoldenUrl = "http://api.taojinbi.taobao.com/json/sign_in_everyday.htm?checkCode=null&_tb_token_=%s&callback=jsonp91"
 
#cookie 自动处理器
cj = cookielib.LWPCookieJar() #LWPCookieJar提供可读写操作的cookie文件,存储cookie对象
cookieSupport= urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
urllib2.install_opener(opener)
 
#打开登陆页面
taobao = urllib2.urlopen(tbLoginUrl)
curl = taobao.geturl()
print curl
 
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
    'Referer' : 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Ftaojinbi.taobao.com%2Findex.htm%3Fspm%3D1.7274553.754897561.d6.Wg8aBc'
}
 
username = "cdts_change"
password = "86ma09ri10o" #你的用户名和密码

postData = {
    'CtrlVersion': '1,0,0,7',  
    'TPL_password':password,  
    'TPL_redirect_url':'',  
    'TPL_username':username,  
    #'_tb_token_':'I262PYW48um', 
    'action':'Authenticator',  
    'callback':'jsonp312',  
    'css_style':'',  
    'event_submit_do_login':'anything',  
    'fc':2,  
    'from':'tb',  
    'from_encoding':'',  
    'guf':'',  
    'gvfdcname':'',  
    'isIgnore':'',  
    'llnick':'',  
    'loginType':3,  
    'longLogin':0,  
    'minipara' :'',  
    'minititle':'',  
    'need_sign':'',  
    'need_user_id':'',  
    'not_duplite_str':'',  
    'popid':'',  
    'poy':'',  
    'pstrong':'',  
    'sign':'',  
    'style':'default',  
    'support':'000001',  
    'tid':''         
}

#登录主函数
def loginToTaobao():
    #cookie 自动处理器
    global checkCodeUrl
    cookiejar = cookielib.LWPCookieJar()#LWPCookieJar提供可读写操作的cookie文件,存储cookie对象
    cookieSupport= urllib2.HTTPCookieProcessor(cookiejar)
    opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    #打开登陆页面
    taobao = urllib2.urlopen(tbLoginUrl)
    resp = taobao.read().decode("gbk")
    #提取验证码地址
    pattern = r'img id="J_StandardCode_m" src="https://s.tbcdn.cn/apps/login/static/img/blank.gif" data-src="(\S*)"'
    checkCodeUrlList = re.findall(pattern, resp)
    checkCodeUrl = checkCodeUrlList[0]
    print "checkCodeUrl:", checkCodeUrl
    #此时直接发送post数据包登录
    while True:
        result = sendPostData(tbLoginUrl, postData, headers)
        if result:
            break;
        if checkCodeUrl != "":
            getCheckCode(checkCodeUrl)
     
def sendPostData(url, data, header):
    print "+"*20+"sendPostData"+"+"*20
    data = urllib.urlencode(data)      
    request = urllib2.Request(url, data, header)
    response = urllib2.urlopen(request)
    #url = response.geturl()
    text = response.read().decode("gbk")
    info = response.info()
    status = response.getcode()
    response.close()
    print status
    print info
    print "Response:", text
    result = handleResponseText(text)
    if result["state"]:
        print "successfully login in!"
        return True
    else:
        print "failed to login in, error message: ",result["message"]
        return False
 
def handleResponseText(text):
    global token
    """处理登录返回结果"""
    global checkCodeUrl
     
    print "+"*20+"handleResponseText"+"+"*20  
    text = text.replace(',', ' ')   
    responseData = {"state": False,
                    "message" : "",
                    "code" : ""}
     
    m1 = re.match(r'\{?"state":(\w*)\ ', text)
    if m1 is not None:
        s = m1.group(1)
        if s == "true":
            responseData["state"] = True
            m2 = re.search(r'"token":"(\S*)"( |})', text)
            if m2 is not None:
                token = m2.group(1)
                print token
            else:
                print "failed to get the token"
        else:
            m2 = re.search(r'"message":"(\S*)"( |})', text)
            if m2 is not None:
                msg = m2.group(1)
                responseData["message"] = msg 
            else:
                print "failed to get the error message"
            m3 = re.search(r'"ccurl":"(\S*)"( |})', text)
            if m3 is not None:
                ccurl = m3.group(1)
                print ccurl
                checkCodeUrl = ccurl
#                 if code == "1000":                 
#                     getCheckCode(checkCodeUrl)
            else:
                print "failed to get the error code"
    return responseData
 
def getCheckCode(url):
    print "+"*20+"getCheckCode"+"+"*20
    response = urllib2.urlopen(url)
    status = response.getcode()
    picData = response.read()
     
    path = "G:\\\mTool\\taobaogolden\\checkcode.jpg"
    if status == 200:
        localPic = open(path, "wb")
        localPic.write(picData)
        localPic.close() 
        print "Please goto %s,see the check code"%path  
        checkCode = raw_input("Please enter the check code: ")
        print checkCode, type(checkCode)
        postData["TPL_checkcode"] = checkCode
        postData["need_check_code"] = "true"
    else:
        print "failed to get Check Code, status: ",status
 
def getGolden():
    
    global token
    queryData = {
             '_tb_token_':token
    }
    data = urllib.urlencode(queryData)
    url = tbGetGoldenUrl % (token)
    request = urllib2.Request(url, data, headers)
    print type(request)
  
    response = urllib2.urlopen(request)
    #查看响应结果
    url = response.geturl()
    text = response.read()
    info = response.info()
    status = response.getcode()
    print status,url,info
    print text.decode('utf-8')
 
if __name__ == "__main__":   
    loginToTaobao()
    getGolden()
    
 
#编码
# postData = urllib.urlencode(postData)
#  
# #发送请求
# request = urllib2.Request(tbLoginUrl, postData, headers)
# print type(request)
#  
# response = urllib2.urlopen(request)
# #查看响应结果
# url = response.geturl()
# text = response.read()
# info = response.info()
# status = response.getcode()
# print status,url,info
# print text.decode('gbk')
# 