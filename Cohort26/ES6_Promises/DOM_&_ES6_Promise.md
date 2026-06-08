# 📘 JavaScript: DOM Manipulation & ES6 Promises

## 👋 Introduction

Welcome to this comprehensive JavaScript session! Today we'll explore two fundamental concepts that make modern web development possible: DOM manipulation (how JavaScript interacts with web pages) and Promises (how JavaScript handles time-consuming operations).

JavaScript is single-threaded, processing one task at a time. However, web applications need to be interactive and responsive, requiring us to both manipulate what users see and handle operations that take time—like fetching data from APIs, uploading files, or waiting for user interactions.

## 🎯 Learning Objectives

By the end of this session, you'll understand:

**DOM Manipulation:**
- What the DOM is and how JavaScript interacts with HTML
- How to find and select elements on a web page
- How to change content, styles, and structure dynamically
- How to respond to user interactions with event listeners
- How to create and add new elements to pages

**ES6 Promises:**
- What Promises are and why we use them
- How to create and use `.then()`, `.catch()`, and `.finally()`
- How to use `Promise.all`, `Promise.race`, `Promise.resolve`, and `Promise.reject`
- How to work with `async/await`
- How to handle errors using `try/catch`
- How to write your own functions that return promises

---

## 🌐 Part I: JavaScript DOM - Making Web Pages Interactive

### What is the DOM?

The DOM (Document Object Model) is how JavaScript sees your HTML page. Every HTML element becomes a JavaScript object that you can find and modify.

Think of your HTML page as a family tree—each element has parents, children, and siblings. JavaScript can find any element in this tree and change it.

### Finding Elements on Your Page

Before you can change something, you need to find it. JavaScript gives you several ways to locate elements:

**Finding by ID** (like looking up someone's address in a phone book):
```javascript
const header = document.getElementById('myHeader');
```

**Using CSS-style selectors** (more flexible, like describing someone by their characteristics):
```javascript
const firstParagraph = document.querySelector('p');        // First paragraph
const importantText = document.querySelector('.important'); // First element with class "important"
const submitButton = document.querySelector('#submit');    // Element with ID "submit"
```

### Changing What Users See

Once you've found an element, you can change it in many ways.

**Change the text inside an element:**
```javascript
const header = document.querySelector('h1');
header.textContent = 'Welcome to Our Site!';
```

**Change how an element looks:**
```javascript
const header = document.querySelector('h1');
header.style.color = 'blue';
header.style.fontSize = '24px';
```

**Add or remove CSS classes** (often better than changing individual styles):
```javascript
const button = document.querySelector('.my-button');
button.classList.add('highlighted');      // Add a class
button.classList.remove('old-style');     // Remove a class
button.classList.toggle('active');        // Add if missing, remove if present
```

### Responding to User Actions

To make your page interactive, you need to respond when users click, type, or perform other actions.

**Handle button clicks:**
```javascript
const button = document.getElementById('clickMe');
button.addEventListener('click', function() {
    alert('Button was clicked!');
});
```

**Respond to other events:**
```javascript
const input = document.querySelector('input');
input.addEventListener('focus', function() {
    this.style.backgroundColor = 'yellow';
});
```

### Creating New Elements

Sometimes you need to add new content to your page dynamically.

```javascript
// Create the new element
const newParagraph = document.createElement('p');
newParagraph.textContent = 'This paragraph was created by JavaScript!';

// Find where to put it
const container = document.getElementById('content');

// Add it to the page
container.appendChild(newParagraph);
```

---

## ⚡ Part II: ES6 Promises - Handling Asynchronous Operations

### 🔍 What is a Promise?

A Promise is an object that represents the eventual result (or failure) of an asynchronous operation. This is crucial when dealing with operations that take time, like fetching data from servers.

**Promise States:**
- ✅ **Fulfilled** – the operation completed successfully
- ❌ **Rejected** – the operation failed  
- ⏳ **Pending** – the operation is still happening

**Basic Example:**
```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Data received!");
  }, 1000);
});
```

### 🧪 Using .then() and .catch()

```javascript
promise
  .then(response => {
    console.log(response); // "Data received!"
  })
  .catch(error => {
    console.error(error);
  });
```

- `.then()` is used when the promise is fulfilled
- `.catch()` is used when the promise is rejected

### ✅ resolve and ❌ reject

```javascript
function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: "Success" });
    } else {
      reject(new Error("The fake API is not working currently"));
    }
  });
}
```

### 🪝 Handling Responses: .then, .catch, .finally

```javascript
function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: "success" }))
    .catch(() => new Error())
    .finally(() => console.log("Got a response from the API"));
}
```

### 🧹 Working with Multiple Promises: Promise.all

```javascript
function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      console.log(photo.body, user.firstName, user.lastName);
    })
    .catch(() => {
      console.log("Signup system offline");
    });
}
```

### 🛠 Mini Example Functions

```javascript
function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}

function uploadPhoto(fileName) {
  return Promise.reject(new Error(`${fileName} cannot be processed`));
}
```

### 🧪 Promise.allSettled – Wait for everything, no matter what

```javascript
function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  return Promise.allSettled(promises)
    .then(results => results.map(p => ({
      status: p.status,
      value: p.value || p.reason,
    })));
}
```

### ⚖️ Promise.race – Who wins first?

```javascript
function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
```

Whichever download finishes first wins the race!

### 💥 Throwing Errors

```javascript
function divideFunction(numerator, denominator) {
  if (denominator === 0) throw new Error("cannot divide by 0");
  return numerator / denominator;
}
```

### 🛡 Handling Errors with try/catch

```javascript
function guardrail(mathFunction) {
  const queue = [];
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (err) {
    queue.push(err.toString());
  } finally {
    queue.push("Guardrail was processed");
  }
  return queue;
}
```

### 🧠 Async / Await

Instead of chaining `.then()`s, you can await the result like this:

```javascript
async function getUserData() {
  try {
    const response = await getFullResponseFromAPI(true);
    console.log(response);
  } catch (err) {
    console.error(err);
  }
}
```

⚠️ **Important:** `await` only works inside functions marked with `async`.

---

## 🌟 Bringing DOM and Promises Together

Now let's see how DOM manipulation and Promises work together in real applications:

### Getting Data from Servers and Updating the DOM

Modern websites often need to get information from servers without reloading the page:

```javascript
// Using Promises with .then()
function loadUserList() {
  fetch('https://api.example.com/users')
    .then(response => response.json())  // Convert response to usable data
    .then(users => {
      // Use the data to update the page
      const userList = document.getElementById('user-list');
      users.forEach(user => {
        const listItem = document.createElement('li');
        listItem.textContent = user.name;
        userList.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Failed to load users:', error);
      const userList = document.getElementById('user-list');
      userList.textContent = 'Failed to load users. Please try again.';
    });
}

// Using async/await (cleaner syntax)
async function loadUserListAsync() {
  try {
    const response = await fetch('https://api.example.com/users');
    const users = await response.json();
    
    const userList = document.getElementById('user-list');
    users.forEach(user => {
      const listItem = document.createElement('li');
      listItem.textContent = user.name;
      userList.appendChild(listItem);
    });
  } catch (error) {
    console.error('Failed to load users:', error);
    const userList = document.getElementById('user-list');
    userList.textContent = 'Failed to load users. Please try again.';
  }
}
```

---

## 🥮 Summary of Promise Methods

| Method | Use Case |
|--------|----------|
| `Promise.resolve()` | Create a resolved promise immediately |
| `Promise.reject()` | Create a rejected promise immediately |
| `Promise.all()` | Wait for all promises to succeed |
| `Promise.race()` | Return result of the first settled one |
| `Promise.allSettled()` | Get all outcomes (fulfilled or rejected) |

## 📝 Key Concepts Recap

**DOM Manipulation:**
- Finding elements with `getElementById()` and `querySelector()`
- Changing content with `textContent` and styles with `style` properties
- Adding/removing CSS classes with `classList`
- Handling user interactions with `addEventListener()`
- Creating new elements with `createElement()` and `appendChild()`

**ES6 Promises:**
- Returning basic promises
- Handling success/failure with `.then()` and `.catch()`
- Aggregating multiple promises with `Promise.all` and `allSettled`
- Rejecting promises with error messages
- Gracefully handling errors using `try/catch` and `finally`
- Writing `async/await` functions for cleaner syntax

## 🧪 Testing Your Code

Remember:
- Your code is tested using Jest
- Linted with ESLint
- Use `npm run test` to run tests

```bash
npm install
npm run test
```

## 🚀 Closing Thought

JavaScript DOM manipulation and Promises are fundamental skills that work together to create dynamic, responsive web applications. DOM manipulation lets you create interactive user interfaces, while Promises help you handle asynchronous operations like API calls without blocking the user experience. 

Once you master these concepts, you'll be equipped to build modern, user-friendly web applications that can fetch data, respond to user actions, and provide smooth, interactive experiences without the dreaded "callback hell."

The combination of these technologies forms the foundation of modern frontend development—from simple interactive websites to complex single-page applications.