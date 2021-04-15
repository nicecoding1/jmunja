from jmunja import smssend

uid = ""
upw = ""
subject = "파이썬 python"
content = "파이썬 모듈 테스트\npython module test"
hpno = "01012345678"
callback = "01012345678"

jphone = smssend.JmunjaPhone(uid, upw)
presult = jphone.send(subject, content, hpno)

jweb = smssend.JmunjaWeb(uid, upw)
wresult = jweb.send(subject, content, hpno, callback)

if presult or wresult:
    print("폰문자 %s건, 웹문자 %s건 발송 성공" % (presult, wresult))
else:
    print("발송 실패")
