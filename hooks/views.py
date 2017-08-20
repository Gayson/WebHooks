# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hmac
import hashlib
import commands

pathlist = [
    '~/github/WebHooks',
    '~/github/Future-Trading-Server',
]

bashlist = [
    '~/github/WebHooks/bashfile/pybash',
    '~/github/WebHooks/bashfile/springbootbash',
]

portlist = [
    3000,
    8000,
]

secret = 'WebHooks'


@csrf_exempt
def updateRepo(request, index):
    pos = int(index)
    if (pos < 0 or pos >= len(pathlist)):
        return HttpResponse("false:\ninvalid index.")

    try:
        signature = request.META.get('HTTP_X_HUB_SIGNATURE')
        signlist = signature.split('=', 1)
        algo = signlist[0]
        key = signlist[1]

        encode = ''
        if algo == 'sha1':
            encode = hmac.new(
                secret, request.body, digestmod=hashlib.sha1).hexdigest()
            if key == encode:
                try:
                    (status, output) = commands.getstatusoutput(
                        'bash %s %s %s' % (bashlist[pos], pathlist[pos],
                                           portlist[pos]))
                    return HttpResponse("success:\n%s" % (output))
                except:
                    return HttpResponse("false:\nbashfile error")
            else:
                return HttpResponse("false:\nsecret unmatch.")
    except:
        return HttpResponse("false:\ndecode error.")


def index(request):
    return HttpResponse("Hello, Index")
