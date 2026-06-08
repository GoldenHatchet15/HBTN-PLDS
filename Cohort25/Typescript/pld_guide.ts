// JavaScript - No type checking
function addNumbers(a, b) {
    return a + b;
}

addNumbers(5, 3);        // Returns 8 ✅
addNumbers("5", "3");    // Returns "53" ❌ (concatenation, not addition!)
addNumbers(5, "hello");  // Returns "5hello" ❌



// TypeScript - With type checking
function addNumbers(a: number, b: number): number {
    return a + b;
}

addNumbers(5, 3);        // Returns 8 ✅
addNumbers("5", "3");    // ❌ ERROR: Argument of type 'string' is not assignable to parameter of type 'number'


let isStudent: boolean = true;
let isTeacher: boolean = false;

// Why use it?
if (isStudent) {
    console.log("Welcome to class!");
}



let age: number = 23;
let height: number = 5.9;
let temperature: number = -10;

// TypeScript prevents this error:
// age = "twenty-three"; // ❌ Error!


let firstName: string = "John";
let lastName: string = "Doe";
let fullName: string = `${firstName} ${lastName}`; // Template literals work!

// Common mistake prevention:
// firstName = 123; // ❌ Error: Type 'number' is not assignable to type 'string'



// Method 1: Type followed by []
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["Alice", "Bob", "Charlie"];

// Method 2: Array<Type> syntax
let scores: Array<number> = [95, 87, 92];

// Why this helps:
names.push("David");     // ✅ OK
names.push(123);         // ❌ Error: Argument of type 'number' is not assignable




// A tuple is like a contract: "This array has exactly 2 elements: string, then number"
let student: [string, number] = ["John", 25];

// This is useful for paired data:
let coordinate: [number, number] = [10, 20]; // x, y coordinates
let nameAge: [string, number] = ["Alice", 30];

// TypeScript enforces the order and types:
// let invalid: [string, number] = [30, "Alice"]; // ❌ Error!




let anything: any = "hello";
anything = 42;           // No error
anything = true;         // No error

// When to use 'any':
// - Migrating from JavaScript gradually
// - Working with dynamic content (user input, APIs)
// - Third-party libraries without type definitions

// ⚠️ Warning: 'any' defeats the purpose of TypeScript!





// Real-world example combining all basic types
let studentId: number = 12345;
let studentName: string = "Emma Wilson";
let isEnrolled: boolean = true;
let grades: number[] = [85, 92, 78, 95];
let contactInfo: [string, string] = ["emma@email.com", "555-0123"]; // email, phone

console.log(`Student: ${studentName} (ID: ${studentId})`);
console.log(`Enrolled: ${isEnrolled}`);
console.log(`Average Grade: ${grades.reduce((a, b) => a + b) / grades.length}`);







// Define the blueprint
interface Student {
    firstName: string;
    lastName: string;
    age: number;
    location: string;
}

// Use the blueprint to create objects
let student1: Student = {
    firstName: "John",
    lastName: "Doe", 
    age: 20,
    location: "New York"
};

let student2: Student = {
    firstName: "Jane",
    lastName: "Smith",
    age: 22,
    location: "California"
};

// TypeScript will error if you miss a property:
// let invalidStudent: Student = {
//     firstName: "Bob",
//     // ❌ Error: Property 'lastName' is missing
// };






interface Teacher {
    firstName: string;
    lastName: string;
    fullTimeEmployee: boolean;
    yearsOfExperience?: number;  // ❓ Optional property
    location: string;
}

// Both of these are valid:
let teacher1: Teacher = {
    firstName: "Alice",
    lastName: "Johnson",
    fullTimeEmployee: true,
    yearsOfExperience: 5,  // Has experience
    location: "Boston"
};

let teacher2: Teacher = {
    firstName: "Bob",
    lastName: "Wilson", 
    fullTimeEmployee: false,
    // No yearsOfExperience - that's OK because it's optional!
    location: "Seattle"
};






// Readonly properties in interfaces

interface Student {
    readonly studentId: number;  // 🔒 Cannot be modified after creation
    firstName: string;
    lastName: string;
}

let student: Student = {
    studentId: 12345,
    firstName: "John",
    lastName: "Doe"
};

student.firstName = "Johnny";  // ✅ OK - not readonly
// student.studentId = 67890;  // ❌ Error: Cannot assign to 'studentId' because it is read-only
















interface Teacher {
    firstName: string;
    lastName: string;
    fullTimeEmployee: boolean;
    location: string;
    
    // Index signature: allows any additional string properties
    [key: string]: any;
}

// Now you can add extra properties:
let teacher: Teacher = {
    firstName: "John",
    lastName: "Doe",
    fullTimeEmployee: false,
    location: "London",
    contract: false,           // ✅ Extra property allowed
    department: "Mathematics", // ✅ Another extra property
    phoneNumber: "555-0123"    // ✅ Yet another one
};









// Base interface
interface Teacher {
    firstName: string;
    lastName: string;
    fullTimeEmployee: boolean;
    location: string;
}

// Extended interface - has everything Teacher has, plus more
interface Director extends Teacher {
    numberOfReports: number;  // Additional property
}

let director: Director = {
    firstName: "Sarah",
    lastName: "Connor",
    fullTimeEmployee: true,
    location: "New York",
    numberOfReports: 15  // Must include this new property
};











class Student {
    // Properties (data)
    firstName: string;
    lastName: string;
    
    // Constructor (special method that runs when creating a new object)
    constructor(firstName: string, lastName: string) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    
    // Methods (functions that belong to the class)
    displayName(): string {
        return this.firstName;
    }
    
    workOnHomework(): string {
        return "Currently working";
    }
}

// Creating objects from the class
let student1 = new Student("John", "Doe");
let student2 = new Student("Jane", "Smith");

console.log(student1.displayName());     // "John"
console.log(student1.workOnHomework());  // "Currently working"











// Long way:
class StudentLong {
    firstName: string;
    lastName: string;
    
    constructor(firstName: string, lastName: string) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

// Short way (equivalent):
class StudentShort {
    constructor(public firstName: string, public lastName: string) {
        // TypeScript automatically creates properties and assigns them!
    }
}









class BankAccount {
    public accountHolder: string;      // Anyone can access
    private balance: number;           // Only this class can access
    protected accountNumber: string;   // This class and subclasses can access
    
    constructor(holder: string, initialBalance: number) {
        this.accountHolder = holder;
        this.balance = initialBalance;
        this.accountNumber = this.generateAccountNumber();
    }
    
    // Public method - anyone can call
    public getBalance(): number {
        return this.balance;
    }
    
    // Private method - only used internally
    private generateAccountNumber(): string {
        return Math.random().toString(36).substr(2, 9);
    }
    
    // Public method that uses private data safely
    public deposit(amount: number): void {
        if (amount > 0) {
            this.balance += amount;
        }
    }
}

let account = new BankAccount("John Doe", 1000);
console.log(account.accountHolder);   // ✅ OK - public
console.log(account.getBalance());    // ✅ OK - public method
// console.log(account.balance);      // ❌ Error - private property













// Interface defines what methods a class must have
interface WorkerInterface {
    workFromHome(): string;
    getCoffeeBreak(): string;
}

// Class must implement all methods from the interface
class Teacher implements WorkerInterface {
    workFromHome(): string {
        return "Cannot work from home";
    }
    
    getCoffeeBreak(): string {
        return "Cannot have a break";
    }
    
    // Class can have additional methods too
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












// JavaScript - What does this function expect? What does it return?
function mysterious(a, b) {
    return a + b;
}





// TypeScript - Crystal clear!
function add(a: number, b: number): number {
    return a + b;
}









// Basic function with typed parameters
function greetStudent(name: string, age: number): string {
    return `Hello ${name}, you are ${age} years old!`;
}

// Usage
greetStudent("Alice", 20);        // ✅ Works
// greetStudent("Alice", "20");   // ❌ Error: Expected number, got string










function createStudent(firstName: string, lastName: string, age?: number): string {
    if (age) {
        return `${firstName} ${lastName}, age ${age}`;
    }
    return `${firstName} ${lastName}`;
}

// Both calls are valid:
createStudent("John", "Doe", 25);    // "John Doe, age 25"
createStudent("Jane", "Smith");      // "Jane Smith"











function calculateGrade(score: number, totalPoints: number = 100): string {
    const percentage = (score / totalPoints) * 100;
    
    if (percentage >= 90) return "A";
    if (percentage >= 80) return "B"; 
    if (percentage >= 70) return "C";
    if (percentage >= 60) return "D";
    return "F";
}

calculateGrade(85);      // Uses default totalPoints = 100
calculateGrade(85, 200); // Uses custom totalPoints = 200












// Interface for a function
interface PrintTeacherFunction {
    (firstName: string, lastName: string): string;
}

// Function that matches the interface
const printTeacher: PrintTeacherFunction = (firstName: string, lastName: string): string => {
    return `${firstName.charAt(0)}. ${lastName}`;
};

console.log(printTeacher("John", "Doe")); // "J. Doe"









// Parameter can be either number or string
function createEmployee(salary: number | string): string {
    if (typeof salary === "number") {
        return salary < 500 ? "Teacher" : "Director";
    } else {
        // salary is string
        return "Director"; // Assume string salaries are high
    }
}

createEmployee(200);     // "Teacher"
createEmployee(1000);    // "Director"  
createEmployee("$500");  // "Director"













// Create a table element
const table: HTMLTableElement = document.createElement("table");

// Create sample student data
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

// Create table rows for each student
studentsList.forEach((student: Student) => {
    const row: HTMLTableRowElement = table.insertRow();
    
    // Insert cells with student data
    const firstNameCell: HTMLTableCellElement = row.insertCell(0);
    const locationCell: HTMLTableCellElement = row.insertCell(1);
    
    firstNameCell.textContent = student.firstName;
    locationCell.textContent = student.location;
});

// Add table to the page
document.body.appendChild(table);










// TypeScript knows what methods are available on each element type
const button: HTMLButtonElement = document.createElement("button");
button.textContent = "Click me!";
button.addEventListener("click", () => {
    console.log("Button clicked!");
});

const input: HTMLInputElement = document.createElement("input");
input.type = "text";
input.placeholder = "Enter your name";

// TypeScript prevents errors like:
// button.value = "test"; // ❌ Error: Property 'value' does not exist on HTMLButtonElement
// input.click();         // ❌ Error: 'click' is not a function (it's an event)














// Without generics - need separate functions for each type:
function getFirstNumber(items: number[]): number {
    return items[0];
}

function getFirstString(items: string[]): string {
    return items[0];
}

// With generics - one function works for all types:
function getFirst<T>(items: T[]): T {
    return items[0];
}

// Usage:
const firstNumber = getFirst<number>([1, 2, 3]);       // Returns number
const firstString = getFirst<string>(["a", "b", "c"]); // Returns string
const firstStudent = getFirst<Student>([student1, student2]); // Returns Student




function isDirector(employee: Director | Teacher): employee is Director {
    return (employee as Director).numberOfReports !== undefined;
}

function executeWork(employee: Director | Teacher): string {
    if (isDirector(employee)) {
        // TypeScript knows employee is Director here
        return employee.workDirectorTasks();
    } else {
        // TypeScript knows employee is Teacher here
        return employee.workTeacherTasks();
    }
}









// Only these exact strings are allowed
type Subjects = "Math" | "History";

function teachClass(todayClass: Subjects): string {
    switch (todayClass) {
        case "Math":
            return "Teaching Math";
        case "History":
            return "Teaching History";
        default:
            // TypeScript ensures this never happens
            const exhaustiveCheck: never = todayClass;
            return exhaustiveCheck;
    }
}

teachClass("Math");     // ✅ OK
teachClass("History");  // ✅ OK
// teachClass("Science"); // ❌ Error: Argument of type '"Science"' is not assignable











namespace Subjects {
    export interface Teacher {
        firstName: string;
        lastName: string;
    }
    
    export class Subject {
        teacher: Teacher;
        
        setTeacher(teacher: Teacher): void {
            this.teacher = teacher;
        }
    }
}

// Usage:
const teacher: Subjects.Teacher = {
    firstName: "John",
    lastName: "Doe"
};

const subject = new Subjects.Subject();
subject.setTeacher(teacher);
















// First declaration
namespace Subjects {
    export interface Teacher {
        firstName: string;
        lastName: string;
    }
}

// Second declaration - gets merged with the first!
namespace Subjects {
    export interface Teacher {
        experienceTeachingC?: number; // Added to existing interface
    }
}

// Now Teacher interface has all properties:
const teacher: Subjects.Teacher = {
    firstName: "John",
    lastName: "Doe",
    experienceTeachingC: 5 // This property is now available
};














// Brand interfaces to prevent mixing similar types
interface MajorCredits {
    credits: number;
    brand: "major"; // Brand property makes this unique
}

interface MinorCredits {
    credits: number;
    brand: "minor"; // Different brand
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

// This prevents accidentally mixing major and minor credits:
const major1: MajorCredits = { credits: 3, brand: "major" };
const minor1: MinorCredits = { credits: 1, brand: "minor" };

// sumMajorCredits(major1, minor1); // ❌ Error: Can't mix major and minor credits













// ❌ Bad - defeats TypeScript's purpose
let data: any = getData();

// ✅ Good - be specific about types
interface UserData {
    name: string;
    age: number;
}
let data: UserData = getData();
















// ❌ Bad - repeated code, easy to make mistakes  
function processUser(name: string, age: number, email: string) { }
function displayUser(name: string, age: number, email: string) { }

// ✅ Good - centralized definition
interface User {
    name: string;
    age: number;
    email: string;
}
function processUser(user: User) { }
function displayUser(user: User) { }












// ❌ Bad - ignoring TypeScript's help
let age: number = "25"; // Error ignored

// ✅ Good - fix the type issue
let age: number = 25;
// or
let age: string = "25";