from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template import loader
from .models import Contact
from django.urls import reverse
from .forms import ContactForm
from django.http import JsonResponse


# Create your views here.
def login(request):
    contact_list = Contact.objects.all().values()
    template = loader.get_template("index.html")
    context = {"contact_list": contact_list}
    # return JsonResponse({"name": "richard"})
    return HttpResponse(template.render(context, request))


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect(login)


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    # print("test", request.POST["fullname"])
    # print("test2", str(contact_id))
    contact.name = request.POST["fullname"]
    contact.phone_number = request.POST["phone"]
    contact.email = request.POST["email"]
    contact.save()
    # return JsonResponse({"name": str(request.POST["fullname"])})
    return redirect(reverse("login"))
    contact = get_object_or_404(Contact, pk=contact_id)
    # login_url = reverse("login")
    # redirect_url = f"{login_url}?contact={contact}"
    # return redirect(redirect_url)


# registration
def registration(request):
    return render(request, "registration.html")


def joinwaitlist(request):
    print("testing join")
    name = request.POST["fullname"]
    phone_number = request.POST["phone"]
    email = request.POST["email"]
    contact = Contact(name=name, phone_number=phone_number, email=email)
    contact.save()
    return redirect(reverse("login"))
    return JsonResponse({"name": "richard"})

def waitlist(request):
    return render(request, "terminal.html")

def userlogin(request):
    return render(request, "userlogin.html")

