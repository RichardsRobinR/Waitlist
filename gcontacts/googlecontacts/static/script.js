// document.addEventListener("DOMContentLoaded", function () {
//     const searchInput = document.getElementById("searchInput");
//     const contactsList = document.getElementById("contactsList");
//     const viewContactsLink = document.getElementById("viewContacts");
//     const addContactLink = document.getElementById("addContact");
  
//     let contacts = [];
  
//     // Load contacts from local storage
//     loadContacts();
  
//     // Event listener for "View Contacts" link
//     viewContactsLink.addEventListener("click", function (event) {
//       event.preventDefault();
//       renderContacts();
//     });
  
//     // Event listener for "Add Contact" link
//     addContactLink.addEventListener("click", function (event) {
//       event.preventDefault();
//       showAddContactForm();
//     });
  
//     // Event listener for search input
//     searchInput.addEventListener("input", function () {
//       renderContacts();
//     });
  
//     // Function to render contacts
//     function renderContacts() {
//       const searchTerm = searchInput.value.toLowerCase();
//       const filteredContacts = contacts.filter(contact =>
//         contact.name.toLowerCase().includes(searchTerm) ||
//         contact.email.toLowerCase().includes(searchTerm) ||
//         contact.phone.toLowerCase().includes(searchTerm)
//       );
//       render(filteredContacts);
//     }
  
//     // Function to render contacts on the UI
//     function render(contactsToShow) {
//       contactsList.innerHTML = "";
//       contactsToShow.forEach(contact => {
//         const contactCard = document.createElement("div");
//         contactCard.classList.add("contact-card");
//         contactCard.innerHTML = `
//           <h2>${contact.name}</h2>
//           <p>Email: ${contact.email}</p>
//           <p>Phone: ${contact.phone}</p>
//           <div class="action-buttons">
//             <md-outlined-button class="delete mat-button" data-email="${contact.email}" >Delete</md-outlined-button>
//             <md-filled-button class="edit mat-button" data-email="${contact.email}">Edit</md-filled-button>
//           </div>
//         `;
//         contactsList.appendChild(contactCard);
  
//         // Event listener for delete button
//         const deleteButton = contactCard.querySelector(".delete");
//         deleteButton.addEventListener("click", function () {
//           const email = deleteButton.getAttribute("data-email");
//           confirmDeleteContact(email);
//         });
  
//         // Event listener for edit button
//         const editButton = contactCard.querySelector(".edit");
//         editButton.addEventListener("click", function () {
//           const email = editButton.getAttribute("data-email");
//           editContact(email);
//         });
//       });
//     }
  
//     // Function to add a new contact
//     function addContact(name, email, phone) {
//       contacts.push({ name, email, phone });
//       saveContacts();
//       renderContacts();
//     }
  
//     // Function to delete a contact
//     function deleteContact(email) {
//       contacts = contacts.filter(contact => contact.email !== email);
//       saveContacts();
//       renderContacts();
//     }
  
//     // Function to edit a contact
//     function editContact(email) {
//       const contactToEdit = contacts.find(contact => contact.email === email);
//       const newName = prompt("Enter new name:", contactToEdit.name);
//       const newEmail = prompt("Enter new email:", contactToEdit.email);
//       const newPhone = prompt("Enter new phone:", contactToEdit.phone);
//       if (newName && newEmail && newPhone) {
//         contactToEdit.name = newName;
//         contactToEdit.email = newEmail;
//         contactToEdit.phone = newPhone;
//         saveContacts();
//         renderContacts();
//       } else {
//         alert("Please enter valid details for the contact.");
//       }
//     }
  
//     // Function to show the add contact form
//     function showAddContactForm() {
//       const name = prompt("Enter contact name:");
//       const email = prompt("Enter contact email:");
//       const phone = prompt("Enter contact phone:");
//       if (name && email && phone) {
//         addContact(name, email, phone);
//       } else {
//         alert("Please enter valid details for the contact.");
//       }
//     }
  
//       // Function to confirm delete action
//   function confirmDeleteContact(email) {
//     const confirmed = confirm("Are you sure you want to delete this contact?");
//     if (confirmed) {
//       deleteContact(email);
//     }
//   }

//   // Function to save contacts to local storage
//   function saveContacts() {
//     localStorage.setItem("contacts", JSON.stringify(contacts));
//   }

//   // Function to load contacts from local storage
//   function loadContacts() {
//     const savedContacts = localStorage.getItem("contacts");
//     if (savedContacts) {
//       contacts = JSON.parse(savedContacts);
//       renderContacts();
//     }
//   }
// });
