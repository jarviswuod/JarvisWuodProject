from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, "mail/home.html")


def addNewMail(request):
    form = UserForm()
    context = {"form": form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            mail = request.POST.get('mail')
            print(f"first_name: {first_name}")
            print(f"last_name: {last_name}")
            print(f"mail: {mail}")

            for mail in loopMails:
                print("Sending mail to:", mail)

                send_mail(
                    subject=subject,
                    message=body,
                    from_email="jarviswuod@gmail.com",
                    recipient_list=[mail],
                    fail_silently=False,
                )
            form.save()

            return HttpResponse("Mail successfully saved!")

    return render(request,  "mail/newMail.html", context)


def weeklyMail(request):
    form = MailbodyForm()

    loopMails = [
        "mail@sample.com",
        "sample@mail.org",
    ]

    if request.method == 'POST':
        form = MailbodyForm(request.POST)

        if form.is_valid():
            subject = request.POST.get('subject')
            body = request.POST.get('body')

            for mail in loopMails:
                print("Sending mail to:", mail)

                send_mail(
                    subject=subject,
                    message=body,
                    from_email="jarviswuod@gmail.com",
                    recipient_list=[mail],
                    fail_silently=False,
                )
            return HttpResponse("All mails sent successfully!")

    context = {"form": form}
    return render(request, "mail/weeklyMail.html", context)

    return HttpResponse("All mails sent successfully!")
