from django.urls import path
from . import views


urlpatterns = [
    path("dashboard_page/", views.dashboard_page, name="dashboard_page"),
    path(
        "delete_contact/<int:contact_id>/", views.delete_contact, name="delete_contact"
    ),
    path("edit_contact/<int:contact_id>/", views.edit_contact, name="edit_contact"),
    # path(
    #     "edit_contact/<str:name>/<str:phone_number>/<str:email>/<int:contact_id>/",
    #     views.edit_contact,
    #     name="edit_contact",
    # ),
    path(
        "registration/", views.registration, name="registration"
    ),  # user registration page to join waitlist
    path("joinwaitlist/", views.joinwaitlist, name="joinwaitlist"),  # adding to the DB
    path("waitlist/", views.waitlist, name="waitlist"),  # waitlist details page
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("admin_validate/", views.admin_validate, name="admin_validate"),
    path("add_contact/", views.add_contact, name="add_contact"),
]
