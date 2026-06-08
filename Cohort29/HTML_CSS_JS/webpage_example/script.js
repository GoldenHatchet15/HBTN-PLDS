const messageBtn = document.getElementById("messageBtn");
const message = document.getElementById("message");
const contactForm = document.getElementById("contactForm");
const formResponse = document.getElementById("formResponse");

messageBtn.addEventListener("click", function () {
  message.textContent = "Hello! JavaScript is working correctly.";
});

contactForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const userMessage = document.getElementById("messageInput").value.trim();

  if (name === "" || email === "" || userMessage === "") {
    formResponse.textContent = "Please fill in all fields.";
    formResponse.style.color = "red";
    return;
  }

  formResponse.textContent = `Thank you, ${name}. Your message has been received!`;
  formResponse.style.color = "green";

  contactForm.reset();
});