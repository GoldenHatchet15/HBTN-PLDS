# TypeScript Fundamentals: From Zero to Hero 🚀

## Table of Contents

1. [What is TypeScript and Why Do We Need It?](#1-what-is-typescript-and-why-do-we-need-it)
2. [Setting Up Your Development Environment](#2-setting-up-your-development-environment)
3. [Basic Types](#3-basic-types)
4. [Interfaces](#4-interfaces)
5. [Classes](#5-classes)
6. [Functions with Types](#6-functions-with-types)
7. [Working with the DOM](#7-working-with-the-dom)
8. [Advanced Concepts](#8-advanced-concepts)
9. [Project Structure and Best Practices](#9-project-structure-and-best-practices)
10. [Practice Questions](#10-practice-questions)

---

# 1. What is TypeScript and Why Do We Need It?

TypeScript is JavaScript with types.

That means TypeScript allows us to write normal JavaScript, but with extra rules that help us catch mistakes before the code runs.

## The Problem with JavaScript

In JavaScript, this function looks normal:

```js
// JavaScript - No type checking
function addNumbers(a, b) {
  return a + b;
}

addNumbers(5, 3);        // 8
addNumbers("5", "3");    // "53"
addNumbers(5, "hello");  // "5hello"
```

The problem is that JavaScript does not stop us from passing strings when the function was supposed to receive numbers.

This can create bugs that are hard to find later.

## The TypeScript Solution

In TypeScript, we can tell the function exactly what types it should accept and return:

```ts
// TypeScript - With type checking
function addNumbers(a: number, b: number): number {
  return a + b;
}

addNumbers(5, 3);        // Works
addNumbers("5", "3");    // Error
```

TypeScript catches the mistake before the code runs.

## Key Benefits of TypeScript

- It catches errors early.
- It makes code easier to understand.
- It improves autocomplete in VS Code.
- It helps large projects stay organized.
- It makes functions, objects, and classes clearer.

## How TypeScript Works

```txt
TypeScript code (.ts)
        ↓
TypeScript compiler (tsc)
        ↓
JavaScript code (.js)
        ↓
Browser or Node.js runs JavaScript
```

Important idea: browsers do not run TypeScript directly. TypeScript must be compiled into JavaScript first.

---

# 2. Setting Up Your Development Environment

A TypeScript project usually includes configuration files that tell the tools how to compile and bundle the code.

## package.json

The `package.json` file describes the project and its scripts.

```json
{
  "name": "typescript_dependencies",
  "scripts": {
    "start-dev": "webpack-dev-server",
    "build": "webpack",
    "test": "jest"
  }
}
```

Common scripts:

```bash
npm install
npm run start-dev
npm run build
npm test
```

## tsconfig.json

The `tsconfig.json` file controls how TypeScript behaves.

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "es6",
    "strict": true,
    "noImplicitAny": true,
    "lib": ["ES2020", "DOM"]
  }
}
```

Explanation:

- `target`: chooses the JavaScript version TypeScript compiles to.
- `module`: controls the module system.
- `strict`: enables stronger type checking.
- `noImplicitAny`: prevents TypeScript from silently using `any`.
- `lib`: includes available JavaScript and browser APIs.

## webpack.config.js

Webpack bundles TypeScript/JavaScript files so they can run in the browser.

In simple words:

```txt
Multiple source files
        ↓
Webpack
        ↓
One bundled file for the browser
```

---

# 3. Basic Types

Types are labels that tell TypeScript what kind of value a variable should store.

## Boolean

A `boolean` can only be `true` or `false`.

```ts
let isStudent: boolean = true;
let isTeacher: boolean = false;

if (isStudent) {
  console.log("Welcome to class!");
}
```

## Number

A `number` can store integers, decimals, and negative numbers.

```ts
let age: number = 23;
let height: number = 5.9;
let temperature: number = -10;

// Error:
// age = "twenty-three";
```

## String

A `string` stores text.

```ts
let firstName: string = "John";
let lastName: string = "Doe";
let fullName: string = `${firstName} ${lastName}`;

// Error:
// firstName = 123;
```

## Array

Arrays store multiple values of the same type.

```ts
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["Alice", "Bob", "Charlie"];

names.push("David");
// names.push(123); // Error
```

Another valid syntax:

```ts
let scores: Array<number> = [95, 87, 92];
```

## Tuple

A tuple is an array with a fixed order and fixed types.

```ts
let student: [string, number] = ["John", 25];
let coordinate: [number, number] = [10, 20];

// Error because the order is wrong:
// let invalid: [string, number] = [30, "Alice"];
```

Use tuples when the position of each value has meaning.

## Any

The `any` type disables TypeScript checking for that variable.

```ts
let anything: any = "hello";
anything = 42;
anything = true;
```

Use `any` carefully. It is useful when migrating old JavaScript code, but using it too much removes the main benefit of TypeScript.

## Practical Example

```ts
let studentId: number = 12345;
let studentName: string = "Emma Wilson";
let isEnrolled: boolean = true;
let grades: number[] = [85, 92, 78, 95];
let contactInfo: [string, string] = ["emma@email.com", "555-0123"];

console.log(`Student: ${studentName} (ID: ${studentId})`);
console.log(`Enrolled: ${isEnrolled}`);
console.log(`Average Grade: ${grades.reduce((a, b) => a + b) / grades.length}`);
```

---

# 4. Interfaces

An interface is a blueprint that describes the shape of an object.

## Basic Interface

```ts
interface Student {
  firstName: string;
  lastName: string;
  age: number;
  location: string;
}

const student1: Student = {
  firstName: "John",
  lastName: "Doe",
  age: 20,
  location: "New York"
};
```

If one required property is missing, TypeScript will show an error.

```ts
// Error: location is missing
const student2: Student = {
  firstName: "Jane",
  lastName: "Smith",
  age: 22
};
```

## Optional Properties

Use `?` when a property is not required.

```ts
interface Teacher {
  firstName: string;
  lastName: string;
  fullTimeEmployee: boolean;
  yearsOfExperience?: number;
  location: string;
}

const teacher1: Teacher = {
  firstName: "Alice",
  lastName: "Johnson",
  fullTimeEmployee: true,
  yearsOfExperience: 5,
  location: "Boston"
};

const teacher2: Teacher = {
  firstName: "Bob",
  lastName: "Wilson",
  fullTimeEmployee: false,
  location: "Seattle"
};
```

## Readonly Properties

Use `readonly` when a property should not change after creation.

```ts
interface RegisteredStudent {
  readonly studentId: number;
  firstName: string;
  lastName: string;
}

const student: RegisteredStudent = {
  studentId: 12345,
  firstName: "John",
  lastName: "Doe"
};

student.firstName = "Johnny";
// student.studentId = 67890; // Error
```

## Index Signatures

Index signatures allow additional properties.

```ts
interface FlexibleTeacher {
  firstName: string;
  lastName: string;
  fullTimeEmployee: boolean;
  location: string;
  [key: string]: string | boolean | number;
}

const teacher: FlexibleTeacher = {
  firstName: "John",
  lastName: "Doe",
  fullTimeEmployee: false,
  location: "London",
  contract: false,
  department: "Mathematics",
  yearsOfExperience: 4
};
```

## Interface Inheritance

An interface can extend another interface.

```ts
interface Teacher {
  firstName: string;
  lastName: string;
  fullTimeEmployee: boolean;
  location: string;
}

interface Director extends Teacher {
  numberOfReports: number;
}

const director: Director = {
  firstName: "Sarah",
  lastName: "Connor",
  fullTimeEmployee: true,
  location: "New York",
  numberOfReports: 15
};
```

---

# 5. Classes

A class is a blueprint used to create objects.

An object created from a class is called an instance.

## Basic Class

```ts
class Student {
  firstName: string;
  lastName: string;

  constructor(firstName: string, lastName: string) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  displayName(): string {
    return this.firstName;
  }

  workOnHomework(): string {
    return "Currently working";
  }
}

const student1 = new Student("John", "Doe");

console.log(student1.displayName());
console.log(student1.workOnHomework());
```

## Constructor Shorthand

TypeScript can create and assign properties directly in the constructor.

```ts
class StudentShort {
  constructor(public firstName: string, public lastName: string) {}
}

const student = new StudentShort("Jane", "Smith");
console.log(student.firstName);
```

## Access Modifiers

Access modifiers control where properties and methods can be used.

- `public`: accessible everywhere.
- `private`: accessible only inside the class.
- `protected`: accessible inside the class and child classes.

```ts
class BankAccount {
  public accountHolder: string;
  private balance: number;
  protected accountNumber: string;

  constructor(holder: string, initialBalance: number) {
    this.accountHolder = holder;
    this.balance = initialBalance;
    this.accountNumber = this.generateAccountNumber();
  }

  public getBalance(): number {
    return this.balance;
  }

  private generateAccountNumber(): string {
    return Math.random().toString(36).substring(2, 11);
  }

  public deposit(amount: number): void {
    if (amount > 0) {
      this.balance += amount;
    }
  }
}

const account = new BankAccount("John Doe", 1000);

console.log(account.accountHolder);
console.log(account.getBalance());
// console.log(account.balance); // Error
```

## Implementing Interfaces with Classes

A class can promise to follow an interface using `implements`.

```ts
interface WorkerInterface {
  workFromHome(): string;
  getCoffeeBreak(): string;
}

class Teacher implements WorkerInterface {
  workFromHome(): string {
    return "Cannot work from home";
  }

  getCoffeeBreak(): string {
    return "Cannot have a break";
  }

  workTeacherTasks(): string {
    return "Getting to work";
  }
}

class Director implements WorkerInterface {
  workFromHome(): string {
    return "Working from home";
  }

  getCoffeeBreak(): string {
    return "Getting a coffee break";
  }

  workDirectorTasks(): string {
    return "Getting to director tasks";
  }
}
```

---

# 6. Functions with Types

Function types make it clear what a function receives and what it returns.

## Parameter and Return Types

```ts
function greetStudent(name: string, age: number): string {
  return `Hello ${name}, you are ${age} years old!`;
}

greetStudent("Alice", 20);
// greetStudent("Alice", "20"); // Error
```

## Optional Parameters

```ts
function createStudent(firstName: string, lastName: string, age?: number): string {
  if (age) {
    return `${firstName} ${lastName}, age ${age}`;
  }

  return `${firstName} ${lastName}`;
}

createStudent("John", "Doe", 25);
createStudent("Jane", "Smith");
```

## Default Parameters

```ts
function calculateGrade(score: number, totalPoints: number = 100): string {
  const percentage = (score / totalPoints) * 100;

  if (percentage >= 90) return "A";
  if (percentage >= 80) return "B";
  if (percentage >= 70) return "C";
  if (percentage >= 60) return "D";
  return "F";
}

calculateGrade(85);
calculateGrade(85, 200);
```

## Function Interface Types

An interface can describe the shape of a function.

```ts
interface PrintTeacherFunction {
  (firstName: string, lastName: string): string;
}

const printTeacher: PrintTeacherFunction = (
  firstName: string,
  lastName: string
): string => {
  return `${firstName.charAt(0)}. ${lastName}`;
};

console.log(printTeacher("John", "Doe"));
```

## Union Types

Union types allow more than one possible type.

```ts
function createEmployee(salary: number | string): string {
  if (typeof salary === "number") {
    return salary < 500 ? "Teacher" : "Director";
  }

  return "Director";
}

createEmployee(200);
createEmployee(1000);
createEmployee("$500");
```

---

# 7. Working with the DOM

The DOM is how JavaScript interacts with HTML.

TypeScript gives us specific types for HTML elements, such as:

- `HTMLTableElement`
- `HTMLButtonElement`
- `HTMLInputElement`
- `HTMLParagraphElement`

## Creating HTML with TypeScript

```ts
interface Student {
  firstName: string;
  lastName: string;
  age: number;
  location: string;
}

const studentsList: Student[] = [
  { firstName: "John", lastName: "Doe", age: 20, location: "New York" },
  { firstName: "Jane", lastName: "Smith", age: 22, location: "California" }
];

const table: HTMLTableElement = document.createElement("table");

studentsList.forEach((student: Student) => {
  const row: HTMLTableRowElement = table.insertRow();

  const firstNameCell: HTMLTableCellElement = row.insertCell(0);
  const locationCell: HTMLTableCellElement = row.insertCell(1);

  firstNameCell.textContent = student.firstName;
  locationCell.textContent = student.location;
});

document.body.appendChild(table);
```

## DOM Event Example

```ts
const button: HTMLButtonElement = document.createElement("button");
button.textContent = "Click me!";

button.addEventListener("click", (): void => {
  console.log("Button clicked!");
});

document.body.appendChild(button);
```

## Input Example

```ts
const input: HTMLInputElement = document.createElement("input");
input.type = "text";
input.placeholder = "Enter your name";

document.body.appendChild(input);
```

---

# 8. Advanced Concepts

## Generic Types

Generics allow us to write reusable code that works with different types.

```ts
function getFirst<T>(items: T[]): T {
  return items[0];
}

const firstNumber = getFirst<number>([1, 2, 3]);
const firstString = getFirst<string>(["a", "b", "c"]);
```

TypeScript can often infer the type automatically:

```ts
const firstBoolean = getFirst([true, false, true]);
```

## Type Guards

Type guards help TypeScript understand what type a value is at runtime.

```ts
interface Teacher {
  workTeacherTasks(): string;
}

interface Director {
  numberOfReports: number;
  workDirectorTasks(): string;
}

function isDirector(employee: Director | Teacher): employee is Director {
  return (employee as Director).numberOfReports !== undefined;
}

function executeWork(employee: Director | Teacher): string {
  if (isDirector(employee)) {
    return employee.workDirectorTasks();
  }

  return employee.workTeacherTasks();
}
```

## String Literal Types

String literal types limit a variable to specific string values.

```ts
type Subjects = "Math" | "History";

function teachClass(todayClass: Subjects): string {
  switch (todayClass) {
    case "Math":
      return "Teaching Math";
    case "History":
      return "Teaching History";
  }
}

teachClass("Math");
teachClass("History");
// teachClass("Science"); // Error
```

## Namespaces

Namespaces organize code under one name.

```ts
namespace Subjects {
  export interface Teacher {
    firstName: string;
    lastName: string;
  }

  export class Subject {
    teacher!: Teacher;

    setTeacher(teacher: Teacher): void {
      this.teacher = teacher;
    }
  }
}

const teacher: Subjects.Teacher = {
  firstName: "John",
  lastName: "Doe"
};

const subject = new Subjects.Subject();
subject.setTeacher(teacher);
```

## Declaration Merging

TypeScript can merge declarations with the same name.

```ts
namespace Subjects {
  export interface Teacher {
    firstName: string;
    lastName: string;
  }
}

namespace Subjects {
  export interface Teacher {
    experienceTeachingC?: number;
  }
}

const teacher: Subjects.Teacher = {
  firstName: "John",
  lastName: "Doe",
  experienceTeachingC: 5
};
```

## Basic Nominal Typing with Brands

TypeScript is normally structurally typed. That means if two objects have the same shape, TypeScript treats them as compatible.

Branding is a technique used to make similar-looking types different.

```ts
interface MajorCredits {
  credits: number;
  brand: "major";
}

interface MinorCredits {
  credits: number;
  brand: "minor";
}

function sumMajorCredits(subject1: MajorCredits, subject2: MajorCredits): MajorCredits {
  return {
    credits: subject1.credits + subject2.credits,
    brand: "major"
  };
}

function sumMinorCredits(subject1: MinorCredits, subject2: MinorCredits): MinorCredits {
  return {
    credits: subject1.credits + subject2.credits,
    brand: "minor"
  };
}

const major1: MajorCredits = { credits: 3, brand: "major" };
const major2: MajorCredits = { credits: 4, brand: "major" };
const minor1: MinorCredits = { credits: 1, brand: "minor" };

sumMajorCredits(major1, major2);
// sumMajorCredits(major1, minor1); // Error
```

---

# 9. Project Structure and Best Practices

## Recommended File Organization

```txt
project/
├── js/
│   ├── main.ts
│   ├── interfaces.ts
│   └── subjects/
│       ├── Teacher.ts
│       ├── Subject.ts
│       ├── Cpp.ts
│       ├── React.ts
│       └── Java.ts
├── package.json
├── tsconfig.json
├── webpack.config.js
└── README.md
```

## Development Workflow

```txt
1. Write TypeScript code in .ts files
2. Run the development server
3. Read TypeScript errors carefully
4. Fix type errors before running the app
5. Build the project
```

Useful commands:

```bash
npm install
npm run start-dev
npm run build
npm test
```

## Common Beginner Mistakes

### Using `any` too much

```ts
// Bad
let data: any = getData();

// Better
interface UserData {
  name: string;
  age: number;
}

let data: UserData = getData();
```

### Repeating object shapes instead of using interfaces

```ts
// Bad
function processUser(name: string, age: number, email: string): void {}
function displayUser(name: string, age: number, email: string): void {}

// Better
interface User {
  name: string;
  age: number;
  email: string;
}

function processUser(user: User): void {}
function displayUser(user: User): void {}
```

### Ignoring compiler errors

```ts
// Bad
let age: number = "25";

// Good
let age: number = 25;

// Also valid if the value should really be text
let ageText: string = "25";
```

---

# 10. Practice Questions

## Concept Questions

1. What problem does TypeScript solve compared to JavaScript?
2. Why does TypeScript need to compile into JavaScript?
3. What is the difference between `number`, `string`, and `boolean`?
4. What is the difference between an array and a tuple?
5. Why should we avoid using `any` too much?
6. What is an interface?
7. What does an optional property do?
8. What is the difference between `private`, `public`, and `protected`?
9. What does `implements` mean in a class?
10. What is a generic type?

## Mini Exercises

### Exercise 1

Create an interface called `Student` with:

- `firstName`
- `lastName`
- `age`
- `location`

Then create two students using that interface.

### Exercise 2

Create a function called `printTeacher` that receives `firstName` and `lastName` and returns the first letter of the first name plus the full last name.

Expected result:

```txt
John Doe -> J. Doe
```

### Exercise 3

Create a class called `StudentClass` with:

- `firstName`
- `lastName`
- `workOnHomework()`
- `displayName()`

Expected behavior:

```txt
workOnHomework() returns "Currently working"
displayName() returns the first name
```

---

# Final Reminder

TypeScript is not a replacement for JavaScript.

TypeScript is JavaScript with a safety system added on top.

The main goal is not to write more complicated code. The goal is to write code that is easier to understand, easier to maintain, and harder to break.
