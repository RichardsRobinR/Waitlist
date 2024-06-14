import pytest
from django.urls import reverse
from django.test import Client
from googlecontacts.models import Contact, Adminusers

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def create_contacts(db):
    contact1 = Contact.objects.create(name="John Doe", phone_number="1234567890", email="john@example.com")
    contact2 = Contact.objects.create(name="Jane Doe", phone_number="0987654321", email="jane@example.com")
    return [contact1, contact2]

@pytest.fixture
def create_admin_user(db):
    admin_user = Adminusers.objects.create(name="admin", password="password")
    return admin_user

def test_dashboard_page(client, create_contacts):
    url = reverse("dashboard_page")
    response = client.get(url)
    assert response.status_code == 200
    assert "contact_list" in response.context
    assert len(response.context["contact_list"]) == 2

def test_delete_contact(client, create_contacts):
    contact = create_contacts[0]
    url = reverse("delete_contact", args=[contact.id])
    response = client.post(url)
    assert response.status_code == 302  # Redirect status
    assert not Contact.objects.filter(id=contact.id).exists()

def test_edit_contact(client, create_contacts):
    contact = create_contacts[0]
    url = reverse("edit_contact", args=[contact.id])
    response = client.post(url, {
        "fullname": "John Updated",
        "phone": "1111111111",
        "email": "johnupdated@example.com"
    })
    assert response.status_code == 302  # Redirect status
    contact.refresh_from_db()
    assert contact.name == "John Updated"
    assert contact.phone_number == "1111111111"
    assert contact.email == "johnupdated@example.com"

def test_registration_page(client):
    url = reverse("registration")
    response = client.get(url)
    assert response.status_code == 200

def test_join_waitlist(client, db):
    url = reverse("joinwaitlist")
    response = client.post(url, {
        "fullname": "New User",
        "phone": "2222222222",
        "email": "newuser@example.com"
    })
    assert response.status_code == 200  # Check response after form submission
    assert Contact.objects.filter(name="New User").exists()

def test_add_contact(client, db):
    url = reverse("add_contact")
    response = client.post(url, {
        "fullname": "New Contact",
        "phone": "3333333333",
        "email": "newcontact@example.com"
    })
    assert response.status_code == 302  # Redirect status
    assert Contact.objects.filter(name="New Contact").exists()

def test_waitlist_page(client):
    url = reverse("waitlist")
    response = client.get(url)
    assert response.status_code == 200

def test_adminlogin_page(client):
    url = reverse("adminlogin")
    response = client.get(url)
    assert response.status_code == 200

def test_admin_validate(client, create_admin_user):
    url = reverse("admin_validate")
    response = client.post(url, {
        "fullname": create_admin_user.name,
        "password": create_admin_user.password
    })
    assert response.status_code == 302  # Redirect status
    assert response.url == reverse("dashboard_page")

    response = client.post(url, {
        "fullname": "wrongname",
        "password": "wrongpassword"
    })
    assert response.status_code == 302  # Redirect status
    assert response.url == reverse("adminlogin")
