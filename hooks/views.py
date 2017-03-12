from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import commands

pathlist=[
'~/github/WebHooks',
]

bashlist=[
'~/github/Webhooks/bashfile/pybash',
]

def updateRepo(request,index):
	pos=int(index)
	if(pos<0 or pos>=len(pathlist)):
		return HttpResponse("false:\ninvalid index.")

	try:
		print(request.META)
		print("********************")
		print(request.body)
		signature=request.META.get('HTTP_X_Hub_Signature')
		return "test header"

	try:
		(status, output)=commands.getstatusoutput('bash %s %s'%(bashlist[pos],pathlist[pos]))
		return HttpResponse("success:\n%s"%(output))
	except:
		return HttpResponse("false:\nbashfile error")

def index(request):
	return HttpResponse("Hello, Index")