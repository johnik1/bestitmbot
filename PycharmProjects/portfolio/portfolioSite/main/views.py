from django.shortcuts import render
from .models import About, Intro, Contact, Enter, Work
from django.core.mail import send_mail


def index(request):
    about = About.objects.all()
    intro = Intro.objects.all()
    contact = Contact.objects.all()
    work = Work.objects.all()
    enter = Enter.objects.all()
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['johnlongman842@gmail.com']  # to email
            )
    return render(request, 'main/index.html', {'about': about, 'intro': intro, 'contact': contact, 'work': work,
                                                   'enter': enter})

# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']
#
#         #send an email
#         send_mail(
#             message_name, #subject
#             message, #message
#             message_email,#from email
#             ['johnlongman842@gmail.com'], #to email
#             )
#         return render(request, 'main/index.html', {'message_name': message_name})
#