from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, EmailContentForm

from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, "mail/home.html")


def addNewMail(request):
    form = UserForm()
    context = {"form": form}
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            mail_body_field = request.POST.get("mail_body_field")

            print("Sending mail to:", email)

            send_mail(
                subject="Week 2: jobs",
                message=mail_body_field,
                from_email="jarviswuod@gmail.com",
                recipient_list=[email],
                fail_silently=False,
            )

            form.save()

            return HttpResponse("Mail successfully saved!")

    return render(request,  "mail/newMail.html", context)


def weeklyMail(request):
    form = EmailContentForm()

    loopMails = [
        "admin@mail.org",
        "john@doe.org",
    ]

    if request.method == 'POST':
        form = EmailContentForm(request.POST)

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
