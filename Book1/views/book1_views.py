#from subscribe.forms import Subscribe
from os import name
from django.shortcuts import render,redirect
from Book1.models import Book1
from django.conf import settings
from django import forms
from django.core.mail import send_mail,EmailMessage
from Book1.models_enum import Math,Names
# Create your views here.


from datetime import date

def homepage(request):
    if request.method == "POST":
        data = request.POST
        if not data.get("id"):
            if data["ispub"] == "Yes":
                Book1.objects.create(name = data["nm"],
                    qty = data["qty"], 
                    price = data["price"], 
                    is_published = True,
                    published_date=date.today())
            elif data["ispub"] == "No":
                Book1.objects.create(name = data["nm"],
                    qty = data["qty"], 
                    price = data.get("price"))
            return redirect("home")
        else:
            bid = data.get("id")
            book_obj = Book1.objects.get(id=bid)
            book_obj.name = data["nm"]
            book_obj.qty = data["qty"]
            book_obj.price = data["price"]
            if data["ispub"] == "Yes":
                if book_obj.is_published:
                    pass
                else:
                    book_obj.is_published = True
                    book_obj.published_date = date.today()
            elif data["ispub"] == "No":
                if book_obj.is_published == True:
                    pass
            book_obj.save()
            return redirect("home")

    else:
        return render(request, template_name="home.html")

    # return HttpResponse("Hi Welcome to Home Page")
# <QueryDict: {'csrfmiddlewaretoken': ['u6xg8VmsaQxvrTWAydjD3AzYPz7VI568bcRfL7s9dXDNUDWUXg7cBW0XUcYjuG7z'], 'nm': ['edwe'], 'qty': ['51'], 'price': ['5151'], 'ispub': ['Yes']}>


def get_books(request):
    books = Book1.objects.all()
    return render(request, template_name="books.html", context={"all_books": books})


def delete_book(request, id):
    # print(id, "delete book id")
    Book1.objects.get(id=id).delete()
    send_mail('Welcome to Library',f'Book ID no:-{id} is Hard Deleted', settings.EMAIL_HOST_USER,['warkadketan47@gmail.com'],fail_silently=False) #mail connectivity
    return redirect("showbook")


def update_book(request, id):
    book_obj = Book1.objects.get(id=id)
    send_mail('Welcome to Library',f'Book ID no:-{id} is Updated', settings.EMAIL_HOST_USER,['warkadketan47@gmail.com'],fail_silently=False) #mailing
    return render(request, "home.html", context={"single_book": book_obj})

    
def soft_delete(request, id):
    book_obj = Book1.objects.get(id=id)
    book_obj.is_deleted = "1"
    book_obj.save()
    send_mail('Welcome to Library',f'Book ID no:-{id} is soft deleted', settings.EMAIL_HOST_USER,['warkadketan47@gmail.com'],fail_silently=False)
    return redirect("showbook")
  
    #return redirect ("showbook")

def active_books(request):
    # all_active_books = Book.objects.filter(is_deleted="1")
    all_active_books = Book1.objects.filter(is_deleted="0")
    return render(request, template_name="books.html", context={"all_books": all_active_books})

def inactive_books(request):
    # all_inactive_books = Book.objects.filter(is_deleted="1")
    all_inactive_books = Book1.objects.filter(is_deleted="1")
    return render(request, template_name="books.html", context={"all_books": all_inactive_books})

def restore_book(request,id):
    all_restore_books=Book1.objects.get(id=id)
    all_restore_books.is_deleted = "0"
    all_restore_books.save()
    send_mail('Welcome to Library',f'Book ID no:-{id} is restored', settings.EMAIL_HOST_USER,['warkadketan47@gmail.com'],fail_silently=False) # mail connectivity
    return redirect("showbook")


#Book1.objects.create(name=Names.BOOK_NAME1.value,qty=,price=)

Names.BOOK_NAME1.value