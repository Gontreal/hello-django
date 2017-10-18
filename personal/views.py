from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def index(request):
    return render(request, 'personal/home.html')


def contactForm(request):
    ret = {
        "err": False,
        "msg": ""
    }
    if request.method == "POST":
        name = request.POST['senderName']
        address = request.POST['EmailAddr']
        phone = request.POST['telephone']
        message = request.POST['Msg']

        if not name or not address or not message:
            ret["err"] = True
            ret["msg"] = "Fill out the required field."
            return JsonResponse(ret)
        elif "@" not in address:
            ret["err"] = True
            ret["msg"] = "Invalid Email Address."
            return JsonResponse(ret)
        else:
            try:
                send_mail(name+" leaves a message", message+phone, address,
                          ['zg900311@outlook.com'])
                ret["msg"] = "Email Sent."
                return JsonResponse(ret)
            except BadHeaderError:
                ret["err"] = True
                ret["msg"] = "Bad header error."
                return JsonResponse(ret)
