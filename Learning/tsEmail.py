from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'

origHdrs = ['From: cdts_change@qq.com', 'To: cdts_change@qq.com',
            'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
sendSvr.login('cdts_change@qq.com', 'genqian@111001*')
errs = sendSvr.sendmail('cdts_change@qq.com', ('cdts_change@qq.com',),origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)   #wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('cdts_change@qq.com')
recvSvr.pass_('genqian@111001*')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig MSG
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody # asset identical