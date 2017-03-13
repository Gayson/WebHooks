from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import hmac, hashlib
import commands

pathlist=[
'~/github/WebHooks',
]

bashlist=[
'~/github/Webhooks/bashfile/pybash',
]

secret = 'WebHooks'

def updateRepo(request,index):
	pos=int(index)
	if(pos<0 or pos>=len(pathlist)):
		return HttpResponse("false:\ninvalid index.")

	try:
		signature=request.META.get('HTTP_X_HUB_SIGNATURE')
		signlist=signature.split(str='=')
		algo=signlist[0]
		key=signlist[1]

		encode=''
		if algo=='sha1':
			encode=hmac.new(secret,request.body,digestmod=hashlib.sha1)
		if key==encode:
			return HttpResponse("success")
	except:
		return HttpResponse("test error")

	try:
		(status, output)=commands.getstatusoutput('bash %s %s'%(bashlist[pos],pathlist[pos]))
		return HttpResponse("success:\n%s"%(output))
	except:
		return HttpResponse("false:\nbashfile error")

def index(request):
	return HttpResponse("Hello, Index")
