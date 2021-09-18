from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from .forms import Subscribe
from django.conf import settings   # to define EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMessage
from Book1.views import *
# Create your views here.
#DataFlair #Send Email
def subscribe_email(request):  # Function based view
    sub = Subscribe()
    print("in subscribe email")
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject1 = 'Welcome to DataFlair'
        message1 = "Book is deleted"
        recepient = request.POST["Email"].strip()  #
        print(recepient)
        if ";" in recepient:
            final_rec_list= recepient.split(";")
        else:
            final_rec_list=[recepient]
        print(final_rec_list,"final_rec_list")
        if final_rec_list:
            # Msg=EmailMessage(subject=subject1,body=message1,from_email=settings.EMAIL_HOST_USER,to=final_rec_list)
            # Msg.attach_file("C:\\Users\\Ketan V Warkad\\Desktop\\sumit 1.docx")
            # Msg.send(fail_silently=False)
            send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list= [recepient])
    # elif soft_delete:
    #     sub = Subscribe(request.POST)
    #     subject1 = 'Welcome to DataFlair'
    #     message1 = 'Hope you are enjoying your Django Tutorials'
    #     recepient = request.POST["Email"].strip()  #
    #     print(recepient)
    #     if ";" in recepient:
    #         final_rec_list= recepient.split(";")
    #     else:
    #         final_rec_list=[recepient]
    #     print(final_rec_list,"final_rec_list")
    #     if final_rec_list:

        return render(request, 'success.html', {'recepient': recepient})
    return render(request,'index.html', context={'form1':sub})