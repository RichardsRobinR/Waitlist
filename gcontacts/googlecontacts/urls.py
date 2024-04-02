from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path(
        "delete_contact/<int:contact_id>/", views.delete_contact, name="delete_contact"
    ),
    path("edit_contact/<int:contact_id>/", views.edit_contact, name="edit_contact"),
    # path(
    #     "edit_contact/<str:name>/<str:phone_number>/<str:email>/<int:contact_id>/",
    #     views.edit_contact,
    #     name="edit_contact",
    # ),
    path("registration/", views.registration, name="registration"),
    path("joinwaitlist/", views.joinwaitlist, name="joinwaitlist"),
    path("waitlist/", views.waitlist, name="waitlist"),
    path("userlogin/", views.waitlist, name="userlogin"),
]
