from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template import loader
from .models import Contact, Adminusers
from django.urls import reverse
from .forms import ContactForm
from django.http import JsonResponse


# Create your views here.
def dashboard_page(request):
    contact_list = Contact.objects.all().values()
    template = loader.get_template("dashboard.html")
    context = {"contact_list": contact_list}
    # return JsonResponse({"name": "richard"})
    return HttpResponse(template.render(context, request))


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect(reverse("dashboard_page"))


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    # print("test", request.POST["fullname"])
    # print("test2", str(contact_id))
    contact.name = request.POST["fullname"]
    contact.phone_number = request.POST["phone"]
    contact.email = request.POST["email"]
    contact.save()
    # return JsonResponse({"name": str(request.POST["fullname"])})
    return redirect(reverse("dashboard_page"))
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

    user = Contact.objects.filter(
        name=name, phone_number=phone_number, email=email
    ).first()

    context = {"name": name}
    template = loader.get_template("terminal.html")

    if user:
        # return redirect(reverse("waitlist"))
        return HttpResponse(template.render(context, request))
    else:
        contact = Contact(name=name, phone_number=phone_number, email=email)
        contact.save()
        HttpResponse(template.render(context, request))
        # return redirect(reverse("waitlist"))
    # return JsonResponse({"name": "richard"})


def waitlist(request):
    return render(request, "terminal.html")


def adminlogin(request):
    return render(request, "adminlogin.html")


def admin_validate(request):
    name = request.POST["fullname"]
    password = request.POST["password"]

    user = Adminusers.objects.filter(name=name, password=password).first()

    if user:
        return redirect(reverse("dashboard_page"))
    else:
        return redirect(reverse("adminlogin"))
