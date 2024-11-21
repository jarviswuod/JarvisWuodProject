from django.shortcuts import render
from django.http import HttpResponse

# from .forms import MailbodyForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return HttpResponse("HOME")


def addNewMail(request):
    return HttpResponse("NEW MAIL IN BLOCK")


def weeklyMail(request):
    return HttpResponse("WEEKLY MAILS IN BLOCK")
    # form = MailbodyForm()

    # loopMails = [
    #     "mail@sample.com",
    #     "sample@mail.org",
    # ]

    # if request.method == 'POST':
    #     form = MailbodyForm(request.POST)

    #     if form.is_valid():
    #         subject = request.POST.get('subject')
    #         body = request.POST.get('body')

    #         for mail in loopMails:
    #             print("Sending mail to:", mail)

    #             send_mail(
    #                 subject=subject,
    #                 message=body,
    #                 from_email="jarviswuod@gmail.com",
    #                 recipient_list=[mail],
    #                 fail_silently=False,
    #             )
    #         return HttpResponse("All mails sent successfully!")

    # context = {"form": form}
    # return render(request, 'mail_forms.html', context)

    # return HttpResponse("All mails sent successfully!")
