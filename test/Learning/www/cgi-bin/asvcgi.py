# from cgi import FieldStorage
# from os import environ
# from cStringIO import StringIO
# from urllib import quote_plus
# from string import capwords, strip, split, join
# from email.quoprimime import unquote
# 
# class AdvCGI(object):
# 
#     header = 'Content-Type: text/html\n\n'
#     url = '/cgi-bin/advcgi.py'
# 
#     formhtml = '''<HTML><HEAD><TITLE>
# Advanced CGI Demo</TITLE></HEAD>
# <BODY><H2>Advanced CGI Demo Form</H2>
# <FORM method=post ACTION="%s" enctype="multipart/form-data">
# <H3>My Cookie Setting</H3>
# <LI><CODE><B>CPPuser = %s</B></CODE>
# <H3>Enter cookie value<BR>
# <INPUT NAME=cookie VALUE="%s">(<I>optional</I>)</H3>
# <H3>Enter your name<BR>
# <INPUT NAME=person VALUE="%s">(<I>required</I>)</H3>
# <H3>What languages can you program in?
# (<I>at least one required</I>)</H3>
# %s
# <H3>Enter file to upload </H3>
# <INPUT TYPE=file name=upfile value="%s" size=45>
# <P><INPUT type=submit>
# </FORM></BODY></HTML>'''
#     
#     langSet = ('Phython','PERL','Java','C++','PHP','C','JavaScript')
#     langItem=\
#     '<input type=checkbox name=lang value="%s"%s> %s\n'
#     
#     def getCPPCookies(self):#read cookies from client
#         if environ.has_key('HTTP_COOKIE'):
#             for eachCookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
#                 if len(eachCookie)>6 and eachCookie[:3]=='CPP':
#                     tag = eachCookie[3:7]
#                     try:
#                         self.cookies[tag]=eval(unquote(eachCookie[8:]))
#                     except (NameError, SyntaxError):
#                         self.cookies[tag]=unquote(eachCookie[8:])
#                 else:
#                     self.cookies['info'] = self.cookies['user'] =''
#                     
#                 if self.cookies['info']!='':
#                     self.who, langStr, self.fn=split(self.cookies['info'],':')
#                     self.langs = split(langStr, ',')
#                 else:
#                     self.who=self.fn=' '
#                     self.langs=['Python']
#     
#     def showForm(self):#show fill-out form
#         self.getCPPCookies()
#         langStr = ''
#         for eachLang in AdvCGI.langSet:
#             if eachLangin self.langs:
#                 langStr+=AdvCGI.langItem%(eachLang,' CHECKED',eachLang)
#             else:
#                 langStr+=AdvCGI.langItem %(eachLang,'',eachLang)
#             if not self.cookies.has_key('user') or self.cookies['user']=='':
#                 cookStatus='<I>(cookie has not been set yet)</I>'
#                 userCook=''
#             else:
#                 userCook = cookStatus=self.cookies['user']
#             print AdvCGI.header+AdvCGI.formhtml % (AdvCGI.url,cookStatus,userCook,self.who,langStr,self.fn)
#         
#         
#     
# errhtml = '''<HTML><HEAD><TITLE>
# Friends CGI Demo
# </TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT>Type=button Value=back
#  onlick="window.history.back()"></FORM>
#  </BODY></HTML>'''
#  
# def showError(error_str):
#      print header+errhtml % (error_str)
# 
# 
# 
# fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'
# 
# def showForm(who, howmany):
#     friends = ''
#     for i in [0,10,25,50,100]:
#         checked = ''
#         if str(i) == howmany:
#             checked = 'CHECKED'
#         friends = friends + fradio % \
#         (str(i), checked, str(i))
#         
#     print header + formhtml % (who, url, who, friends)
#     
# reshtml = '''Content-Type: text/html\n
# <HTML><HEAD><TITLE>
# Friends CGI Demo
# </TITLE></HEAD>
# <BODY><H3>Friends list for: <I>%s</I></H3>
# Your name is: <B>%s</B><P>
# You have <B>%s</B> friends.
# <P>Click<A href="%s">here</A> to edit your data again.
# </BODY></HTML>'''
#     
# def doResults(who, howmany):
#     newurl = url +'?action=reedit&person=%s&howmany=%s' %\
#         (quote_plus(who), howmany)
#     print header + reshtml % (who, who, howmany, newurl)
#     
# def process():
#     error = ''
#     form = cgi.FieldStorage()
#     if form.has_key('person'):
#         who = capwords(form['person'].value)
#     else:
#         who = 'NEW USER'
#         
#     if form.has_key('howmany'):
#         howmany = form['howmany'].value
#     else:
#         if form.has_key('action') and\
#             form['action'].value == 'edit':
#             error = 'Please select number of friends.'
#         else:
#             howmany = 0
#         
#     if not error: 
#         if form.has_key('action') and\
#             form['action'].value != 'reedit':
#              doResults(who, howmany)
#         else:
#             showForm(who, howmany) 
#     else:
#         showError(error)
#         
# if __name__ == '__main__':
#     process()