# ES6 Basics and Classes

## Welcome to Modern JavaScript! 🚀

Think of this lecture as learning to drive a newer, better car. You might know how to drive an old car (regular JavaScript), but now we're going to learn all the cool new features of a modern car (ES6)!

---

## Part 1: ES6 Basics

### What is ES6?

**ES6** stands for **ECMAScript 6** (also called ECMAScript 2015). Think of it like this:
- **JavaScript** is like the English language
- **ES6** is like a major update to English that added thousands of new words and better grammar rules
- It was released in 2015 and made JavaScript much more powerful and easier to write

**Why should you care?** ES6 makes your code:
- Shorter and cleaner
- Easier to read
- Less likely to have bugs
- More powerful

---

### 1. Constants vs Variables

In programming, we need to store information in "containers" called variables. Imagine you have different types of storage boxes: some you can open and change the contents anytime, others are sealed forever once you put something in them.

Before ES6, JavaScript only had one type of variable called `var`. This caused many problems because `var` behaved unpredictably. ES6 introduced two new, better options: `let` and `const`.

#### The Old Way (var) - The Unpredictable Container
In the old days, programmers used `var` for everything. Here's how it worked, but don't worry about memorizing this - just understand why it was problematic:

```javascript
var name = "John";
name = "Jane"; // This works
```

The problem with `var` is that it doesn't follow rules very well - it can "escape" from where you put it and cause confusion (we'll see this later).

#### The New Way - Two Types of Containers with Clear Rules
ES6 gave us two much better options. Think of them like different types of storage:

**Using `let` - The Changeable Container:**
When you know the value inside might need to change later, use `let`. It's like a storage box with a removable lid - you can always open it and change what's inside.

```javascript
// let - for things that can change (like a variable locker you can reopen)
let age = 15;
age = 16; // This works! Age can change over time
let favoriteColor = "blue";
favoriteColor = "red"; // Also fine - preferences can change
```

**Using `const` - The Permanent Container:**
When you know the value should NEVER change, use `const`. It's like a sealed envelope - once you put something in and seal it, that's it forever.

```javascript
// const - for things that should NEVER change (like a sealed envelope)
const birthYear = 2008;
birthYear = 2009; // ERROR! This breaks because birthYear should never change

const pi = 3.14159;
pi = 3; // ERROR! Mathematical constants don't change

const myName = "Alice";
myName = "Bob"; // ERROR! Your name doesn't change
```

**Think of it like this:**
- `let` = a pencil (you can erase and rewrite)
- `const` = a pen (once written, it's permanent)

---

### 2. Block-Scoped Variables

Imagine your house has different rooms, and each room represents a different section of your code (like inside an `if` statement, a `for` loop, or between curly braces `{}`). In programming, we call these sections "blocks."

The big problem with the old `var` was that variables would "escape" from their rooms and wander around the house, causing confusion. It's like writing a note in your bedroom, but somehow that note appears in your kitchen - that's not supposed to happen!

ES6 fixed this by making `let` and `const` respect room boundaries. When you create a variable with `let` or `const` inside a block (room), it stays in that block and can't escape.

#### The Problem with `var` - Variables That Escape Their Rooms
Let's see what happened with the old `var`. This example shows how variables would "leak out" of where they were supposed to stay:

```javascript
// Old way with var (variables escape!)
if (true) {
    var oldWay = "I can escape this room!";
    // This variable is created inside the if statement
}
console.log(oldWay); // This works! Variable escaped from the if statement
// This is BAD because the variable was supposed to stay inside the if block
```

#### The Solution with `let` and `const` - Variables That Stay Where They Belong
Now let's see how ES6 fixed this problem. Variables created with `let` and `const` have good manners - they stay where they're supposed to:

```javascript
// New way with let/const (variables stay in their room)
if (true) {
    let newWay = "I stay in this room!";
    const alsoStays = "Me too!";
    // These variables are created inside the if statement and STAY there
}
console.log(newWay); // ERROR! Variable can't escape - this is GOOD!
console.log(alsoStays); // ERROR! This variable also can't escape - also GOOD!
```

#### A Real-World Example of Why This Matters
Here's a practical example that shows why block scope is so important. Imagine you're writing a program that processes student grades:

```javascript
let finalGrade = "A"; // This is the student's overall grade

if (testScore < 60) {
    let finalGrade = "F"; // This is just for inside this if statement
    console.log("Failed the test: " + finalGrade);
}

console.log("Overall grade: " + finalGrade); // Still "A"!
// The finalGrade inside the if statement didn't affect the main finalGrade
```

**Why is this good?** It prevents accidents where variables from one part of your code accidentally mess up variables in another part. It's like having good organization in your house - things stay where they belong!

---

### 3. Arrow Functions (The Cool Way to Write Functions)

Functions are like little machines that take some input, do something with it, and give you back a result. Before ES6, there was only one way to write functions, and it was quite verbose (meaning you had to type a lot of words). ES6 introduced "arrow functions" which let you write the same functions with much less typing.

Think of arrow functions like abbreviations in texting - instead of typing "you," you type "u." Arrow functions are the texting abbreviation version of regular functions!

#### The Old Way - Writing Functions the Long Way
Before ES6, every time you wanted to create a function, you had to write the full word "function" and use a specific format. Here's what that looked like:

```javascript
function sayHello(name) {
    return "Hello " + name;
}

// To use it:
console.log(sayHello("Alice")); // "Hello Alice"
```

This works perfectly fine, but it requires a lot of typing, especially when you have many simple functions.

#### The New Way - Arrow Functions (The Shortcut Method)
ES6 introduced arrow functions, which use the "arrow" symbol `=>` (made by typing equals and greater-than). Here's the same function written in the new, shorter way:

```javascript
const sayHello = (name) => {
    return "Hello " + name;
};

// To use it (exactly the same as before):
console.log(sayHello("Alice")); // "Hello Alice"
```

#### Even Shorter - For Really Simple Functions
If your function is really simple (just one line that returns something), you can make it even shorter by removing the curly braces `{}` and the `return` keyword:

```javascript
const sayHello = name => "Hello " + name;
// This automatically returns "Hello " + name
```

#### Let's See Different Types of Arrow Functions with Detailed Explanations

**Multiple Parameters - When Your Function Needs Several Inputs:**
Sometimes your function needs more than one piece of information. When you have multiple parameters, you must put them in parentheses:

```javascript
const add = (a, b) => a + b;
// This takes two numbers and adds them together
console.log(add(5, 3)); // 8
```

**No Parameters - When Your Function Doesn't Need Any Input:**
Sometimes your function doesn't need any information from the outside - it just does its thing. For no parameters, you still need empty parentheses:

```javascript
const sayHi = () => "Hi there!";
// This function always returns the same greeting
console.log(sayHi()); // "Hi there!"
```

**One Parameter - Special Rule for Single Inputs:**
When you have exactly one parameter, you can skip the parentheses around it (but you don't have to - both ways work):

```javascript
const double = x => x * 2;
// This takes one number and doubles it
console.log(double(7)); // 14

// You could also write it as:
const double2 = (x) => x * 2; // Also correct!
```

---

### 4. Default Parameters (No More Undefined Problems!)

Imagine you're creating a function that greets people, but sometimes someone might forget to tell you their name. What should your function do? Should it break? Should it say "Hello undefined"? That would be weird and unprofessional.

In the old days, programmers had to write extra code to handle these "missing information" situations. ES6 introduced default parameters, which automatically provide backup values when someone forgets to give you information.

It's like having a polite response ready when someone doesn't introduce themselves - instead of being awkward, you just say "Hello there, friend!"

#### The Problem - What Happens When Information is Missing
Let's first understand what happens when someone calls your function but forgets to provide all the information it needs:

```javascript
// A simple greeting function
function greet(name) {
    return "Hello " + name;
}

console.log(greet("Alice")); // "Hello Alice" - this works fine
console.log(greet());        // "Hello undefined" - this looks weird and unprofessional!
```

#### The Old Solution - Writing Extra Code to Handle Missing Values
Before ES6, programmers had to write extra code to check if values were missing and provide backups:

```javascript
function greet(name) {
    // Check if name was provided, if not, use "Friend" as backup
    if (name === undefined) {
        name = "Friend";
    }
    return "Hello " + name;
}

console.log(greet("Alice")); // "Hello Alice"
console.log(greet());        // "Hello Friend" - much better!
```

This works, but you have to write this checking code every time, which gets tedious and makes your functions longer.

#### The New Solution - Default Parameters Do the Work for You
ES6 lets you specify default values right in the function definition. If someone doesn't provide a value, JavaScript automatically uses your default:

```javascript
const greet = (name = "Friend") => "Hello " + name;

// Examples showing how defaults work:
console.log(greet("Alice")); // "Hello Alice" - name provided, use it
console.log(greet());        // "Hello Friend" - no name provided, use default
console.log(greet("Bob"));   // "Hello Bob" - name provided, use it
```

#### More Complex Examples with Multiple Default Parameters
You can have multiple parameters with defaults. This is especially useful when creating functions that have lots of optional settings:

```javascript
// Function to create a user profile with sensible defaults
const createProfile = (name, age = 18, country = "USA", language = "English") => {
    return `Profile: ${name}, ${age} years old, from ${country}, speaks ${language}`;
};

// Different ways to call this function:
console.log(createProfile("Alice"));
// "Profile: Alice, 18 years old, from USA, speaks English"

console.log(createProfile("Bob", 25));
// "Profile: Bob, 25 years old, from USA, speaks English"

console.log(createProfile("Carmen", 30, "Spain", "Spanish"));
// "Profile: Carmen, 30 years old, from Spain, speaks Spanish"
```

---

### 5. Rest Parameters (Collecting Unknown Amounts of Data)

Sometimes when you're writing a function, you don't know ahead of time how many pieces of information someone might give you. It's like planning a party - you might not know exactly how many people will show up, but you want to welcome everyone who comes.

Before ES6, handling an unknown number of inputs was complicated and messy. ES6 introduced "rest parameters" using three dots `...` which act like a magical collecting bag that gathers up all the extra information someone gives you.

#### The Problem - Not Knowing How Much Data You'll Get
Let's say you want to write a function that adds up numbers, but you don't know if someone will give you 2 numbers, 5 numbers, or 20 numbers. How do you handle that?

#### The Old Way - Messy and Hard to Understand
Before ES6, JavaScript had a special hidden variable called `arguments` that collected extra parameters, but it was confusing to use:

```javascript
// Old way - messy and complicated (don't worry about understanding this fully)
function addAll() {
    let sum = 0;
    // 'arguments' is a special hidden variable that collected all parameters
    for (let i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}

// This worked, but the code was hard to read and understand
console.log(addAll(1, 2, 3));       // 6
console.log(addAll(1, 2, 3, 4, 5)); // 15
```

#### The New Way - Rest Parameters with Three Dots (...)
ES6 introduced rest parameters, which use three dots `...` followed by a name you choose. This creates an array that automatically collects all the extra parameters:

```javascript
// New way with rest parameters (...)
const addAll = (...numbers) => {
    console.log("I received these numbers:", numbers); // This shows you what got collected
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
};

// Usage examples:
console.log(addAll(1, 2, 3));          // 6
console.log(addAll(1, 2, 3, 4, 5));    // 15
console.log(addAll(10));               // 10
console.log(addAll(2, 4, 6, 8, 10, 12)); // 42
```

**What's happening here?** The `...numbers` creates an array called `numbers` that contains whatever values were passed in. If you call `addAll(1, 2, 3)`, then `numbers` becomes `[1, 2, 3]`.

#### Mixing Regular Parameters with Rest Parameters
You can also combine normal parameters with rest parameters. The rest parameter always comes last and collects whatever is left over:

```javascript
// Function that takes a greeting message, then any number of names
const greetEveryone = (greeting, ...names) => {
    console.log(`${greeting} Here are all the people I'm greeting:`, names);
    
    for (let name of names) {
        console.log(`${greeting} ${name}!`);
    }
};

// Examples:
greetEveryone("Hello", "Alice", "Bob", "Charlie");
// Prints: "Hello Alice!", "Hello Bob!", "Hello Charlie!"

greetEveryone("Good morning", "Sarah");
// Prints: "Good morning Sarah!"
```

#### A Practical Example - Building a Shopping List Function
Here's a real-world example that shows how useful rest parameters can be:

```javascript
const createShoppingList = (storeName, ...items) => {
    console.log(`Shopping list for ${storeName}:`);
    console.log(`Items to buy (${items.length} total):`);
    
    for (let i = 0; i < items.length; i++) {
        console.log(`${i + 1}. ${items[i]}`);
    }
};

// You can call it with any number of items:
createShoppingList("Target", "milk", "bread", "eggs");
createShoppingList("Best Buy", "laptop", "mouse", "keyboard", "monitor", "speakers");
```

---

### 6. Spread Operator (Unpacking and Expanding Data)

While rest parameters collect multiple values into an array, the spread operator does the opposite - it takes an array (or other collections) and "spreads out" or "unpacks" all the individual values. It's like having a box of items and emptying all the items out onto a table.

The spread operator also uses three dots `...`, but it's used in a different context than rest parameters. Think of it as "expanding" or "spreading out" the contents of an array.

#### Understanding the Problem - Combining Arrays the Hard Way
Let's say you have two arrays and you want to combine them into one big array. Before ES6, this required using special methods that weren't very intuitive:

```javascript
const fruits = ["apple", "banana"];
const vegetables = ["carrot", "broccoli"];

// Old way to combine arrays - using the concat method
const oldCombined = fruits.concat(vegetables);
console.log(oldCombined); // ["apple", "banana", "carrot", "broccoli"]
```

This works, but it's not very readable, and you have to remember the name of the `concat` method.

#### The New Way - Spread Operator Makes It Visual and Intuitive
With the spread operator, combining arrays becomes much more visual and easy to understand:

```javascript
const fruits = ["apple", "banana"];
const vegetables = ["carrot", "broccoli"];

// New way with spread operator (...)
const newCombined = [...fruits, ...vegetables];
console.log(newCombined); // ["apple", "banana", "carrot", "broccoli"]

// You can even add extra items while combining:
const fullGroceryList = [...fruits, "milk", ...vegetables, "bread"];
console.log(fullGroceryList); // ["apple", "banana", "milk", "carrot", "broccoli", "bread"]
```

**What's happening?** The `...fruits` takes the fruits array and "spreads out" all its contents. It's like emptying the fruits box into the new combined box, then emptying the vegetables box into the same combined box.

#### Using Spread with Function Calls - Passing Array Elements as Individual Arguments
Sometimes you have data in an array, but a function expects you to pass each item separately. The spread operator can "unpack" your array for the function call:

```javascript
const numbers = [15, 25, 8, 42, 7];

// Let's say you want to find the largest number
// Math.max expects individual numbers: Math.max(15, 25, 8, 42, 7)
// But you have them in an array

// Old way - complicated
const oldMax = Math.max.apply(null, numbers); // Don't worry about understanding this

// New way with spread - much clearer
const newMax = Math.max(...numbers);
console.log(newMax); // 42

// The spread operator basically converts [...numbers] into: 15, 25, 8, 42, 7
// So Math.max(...numbers) becomes Math.max(15, 25, 8, 42, 7)
```

#### Copying Arrays - Making Independent Copies
Sometimes you want to create a copy of an array so you can modify the copy without affecting the original. The spread operator makes this easy:

```javascript
const originalTodos = ["study math", "walk dog", "buy groceries"];

// Create an independent copy using spread
const todosCopy = [...originalTodos];

// Now you can modify the copy without affecting the original
todosCopy.push("call mom");

console.log("Original:", originalTodos); // ["study math", "walk dog", "buy groceries"]
console.log("Copy:", todosCopy);        // ["study math", "walk dog", "buy groceries", "call mom"]
```

#### Spread with Objects - Combining and Copying Object Properties
The spread operator also works with objects, allowing you to combine properties from multiple objects or create copies:

```javascript
const person = { name: "Alice", age: 16 };
const contact = { email: "alice@email.com", phone: "555-1234" };

// Combine objects using spread
const fullProfile = { ...person, ...contact };
console.log(fullProfile);
// { name: "Alice", age: 16, email: "alice@email.com", phone: "555-1234" }

// You can also override properties while spreading
const updatedProfile = { ...person, age: 17, city: "New York" };
console.log(updatedProfile);
// { name: "Alice", age: 17, city: "New York" }
```

---

### 7. Template Literals (Smart String Building with Superpowers)

Building strings in programming is like writing a sentence where some words need to be filled in based on information you have. Before ES6, combining text with variables was messy and hard to read, especially when you had lots of variables or wanted to create multi-line text.

ES6 introduced template literals, which use backticks (the `` ` `` character, usually found above your Tab key) instead of regular quotes. Template literals are like smart strings that can automatically insert variables and even do calculations right inside the text.

#### The Old Problem - Messy String Building
Before ES6, when you wanted to build a string that included variables, you had to use the plus sign `+` to glue pieces together. This became messy and hard to read, especially with longer sentences:

```javascript
const name = "Alice";
const age = 16;
const city = "New York";

// Old way - lots of plus signs and quote marks to keep track of
const oldMessage = "Hi, I'm " + name + " and I'm " + age + " years old. I live in " + city + ".";
console.log(oldMessage);
// "Hi, I'm Alice and I'm 16 years old. I live in New York."
```

This works, but look at all those plus signs and quote marks! It's easy to make mistakes, and it's hard to see what the final sentence will look like.

#### The New Way - Template Literals with Variable Insertion
Template literals use backticks `` ` `` and allow you to insert variables directly into the string using `${}`. It's like having blanks in a sentence that get automatically filled in:

```javascript
const name = "Alice";
const age = 16;
const city = "New York";

// New way with template literals - much cleaner and easier to read
const newMessage = `Hi, I'm ${name} and I'm ${age} years old. I live in ${city}.`;
console.log(newMessage);
// "Hi, I'm Alice and I'm 16 years old. I live in New York."
```

**What's happening?** Inside the `${}`, you can put any variable name, and JavaScript will automatically replace it with the variable's value.

#### Template Literals Can Do Math and Function Calls
Inside the `${}`, you can do calculations, call functions, or use any JavaScript expression:

```javascript
const price = 29.99;
const quantity = 3;
const taxRate = 0.08;

const receipt = `
Order Summary:
Item price: ${price}
Quantity: ${quantity}
Subtotal: ${price * quantity}
Tax: ${(price * quantity * taxRate).toFixed(2)}
Total: ${(price * quantity * (1 + taxRate)).toFixed(2)}
`;

console.log(receipt);
```

#### Multi-Line Strings - No More Complicated Line Breaks
One of the most annoying things about old-style strings was creating text that spans multiple lines. You had to use special characters like `\n` or concatenate multiple strings. Template literals make multi-line text natural and easy:

```javascript
// Old way - messy and hard to format
const oldPoem = "Roses are red,\n" +
                "Violets are blue,\n" +
                "ES6 is awesome,\n" +
                "And so are you!";

// New way - write it exactly as you want it to appear
const newPoem = `
    Roses are red,
    Violets are blue,
    ES6 is awesome,
    And so are you!
`;

console.log(newPoem);
```

#### Practical Example - Creating HTML with Template Literals
Template literals are especially useful when creating HTML content dynamically. Here's an example of creating a user profile card:

```javascript
const user = {
    name: "Sarah Johnson",
    age: 17,
    grade: "12th",
    favoriteSubjects: ["Math", "Physics", "Computer Science"],
    profilePicture: "sarah.jpg"
};

// Creating HTML with template literals - much more readable than string concatenation
const profileHTML = `
    <div class="user-profile">
        <img src="${user.profilePicture}" alt="${user.name}'s photo">
        <h2>${user.name}</h2>
        <p>Age: ${user.age}</p>
        <p>Grade: ${user.grade}</p>
        <p>Favorite Subjects: ${user.favoriteSubjects.join(", ")}</p>
        <p>Days until graduation: ${365 - new Date().getDay()}</p>
    </div>
`;

console.log(profileHTML);
```

**Notice how easy it is to read and understand what the final HTML will look like, compared to building it with string concatenation!**

---

### 8. Enhanced Object Creation

#### Old Way
```javascript
const name = "Alice";
const age = 16;

const person = {
    name: name,
    age: age,
    sayHello: function() {
        return "Hello!";
    }
};
```

#### New Way (Shorthand Properties)
```javascript
const name = "Alice";
const age = 16;

const person = {
    name,    // Same as name: name
    age,     // Same as age: age
    sayHello() {  // Shorter method syntax
        return "Hello!";
    }
};
```

---

### 9. Iterators and For-Of Loops

#### Old Way to Loop Through Arrays
```javascript
const colors = ["red", "green", "blue"];

for (let i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}
```

#### New Way (For-Of Loop)
```javascript
const colors = ["red", "green", "blue"];

for (let color of colors) {
    console.log(color);
}
```

**It's like saying "for each color in the colors array" - much more natural!**

---

## Part 2: ES6 Classes

### What are Classes?

Think of a **class** like a **blueprint** or **cookie cutter**:
- A blueprint shows how to build a house, but it's not a house itself
- A cookie cutter shows the shape of a cookie, but it's not a cookie
- A class shows how to create objects, but it's not an object itself

---

### 1. Defining a Class

```javascript
class Person {
    // Constructor - runs when you create a new person
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    // Method - something the person can do
    sayHello() {
        return `Hi, I'm ${this.name} and I'm ${this.age} years old!`;
    }
    
    // Another method
    haveBirthday() {
        this.age++;
        return `Happy birthday! I'm now ${this.age}!`;
    }
}

// Creating new people (instances)
const alice = new Person("Alice", 16);
const bob = new Person("Bob", 17);

console.log(alice.sayHello()); // "Hi, I'm Alice and I'm 16 years old!"
console.log(bob.haveBirthday()); // "Happy birthday! I'm now 18!"
```

---

### 2. Static Methods (Class Methods)

Sometimes you want a method that belongs to the class itself, not to individual objects:

```javascript
class MathHelper {
    static add(a, b) {
        return a + b;
    }
    
    static multiply(a, b) {
        return a * b;
    }
}

// You call static methods on the class, not on instances
console.log(MathHelper.add(5, 3)); // 8
console.log(MathHelper.multiply(4, 2)); // 8

// You DON'T do this:
// const helper = new MathHelper();
// helper.add(5, 3); // This won't work!
```

**Think of static methods like tools that belong to the whole toolbox, not to individual projects.**

---

### 3. Class Inheritance (Extending Classes)

Sometimes you want to create a more specific version of a class:

```javascript
// Base class (parent)
class Animal {
    constructor(name, species) {
        this.name = name;
        this.species = species;
    }
    
    makeSound() {
        return `${this.name} makes a sound`;
    }
    
    eat() {
        return `${this.name} is eating`;
    }
}

// Extended class (child)
class Dog extends Animal {
    constructor(name, breed) {
        super(name, "Dog"); // Call parent constructor
        this.breed = breed;
    }
    
    // Override parent method
    makeSound() {
        return `${this.name} barks: Woof! Woof!`;
    }
    
    // New method specific to dogs
    fetch() {
        return `${this.name} fetches the ball!`;
    }
}

// Usage
const myDog = new Dog("Buddy", "Golden Retriever");
console.log(myDog.makeSound()); // "Buddy barks: Woof! Woof!"
console.log(myDog.eat());       // "Buddy is eating" (inherited)
console.log(myDog.fetch());     // "Buddy fetches the ball!" (dog-specific)
```

**Think of inheritance like family traits:**
- Dogs inherit basic animal abilities (eating, moving)
- But they also have special dog abilities (barking, fetching)

---

### 4. Metaprogramming and Symbols (Advanced Topic)

**Metaprogramming** means "writing code that writes or modifies code." It's like being a magician who creates new magic tricks!

#### Symbols
Symbols are like secret, unique identifiers:

```javascript
// Creating symbols
const secret1 = Symbol("my secret");
const secret2 = Symbol("my secret");

console.log(secret1 === secret2); // false - each symbol is unique!

// Using symbols as object properties
const person = {
    name: "Alice",
    age: 16,
    [secret1]: "This is a secret property"
};

console.log(person[secret1]); // "This is a secret property"
console.log(person.secret1);  // undefined - can't access it normally!
```

#### Practical Example with Classes:
```javascript
const _private = Symbol("private");

class BankAccount {
    constructor(balance) {
        this.owner = "Alice";
        this[_private] = balance; // Secret balance
    }
    
    deposit(amount) {
        this[_private] += amount;
        return `Deposited $${amount}. New balance: $${this[_private]}`;
    }
    
    getBalance() {
        return this[_private];
    }
}

const account = new BankAccount(100);
console.log(account.getBalance()); // 100
console.log(account.owner);        // "Alice"
console.log(account._private);     // undefined - can't access directly!
```

---

## Summary: What You've Learned

### ES6 Basics:
- **ES6** made JavaScript more modern and powerful
- **let/const** vs **var** - better variable control
- **Arrow functions** - shorter, cleaner function syntax
- **Default parameters** - no more undefined problems
- **Rest/spread** - collect and unpack data easily
- **Template literals** - smart string building with backticks
- **Enhanced objects** - shorter syntax for object properties
- **For-of loops** - easier array iteration

### ES6 Classes:
- **Classes** are blueprints for creating objects
- **Constructor** sets up new objects
- **Methods** define what objects can do
- **Static methods** belong to the class, not instances
- **Inheritance** lets classes share and extend functionality
- **Symbols** create unique, secret identifiers for metaprogramming

---

## Next Steps

Practice these concepts by:
1. Converting old JavaScript code to ES6 syntax
2. Creating your own classes (Car, Student, Game, etc.)
3. Using inheritance to create specialized versions
4. Experimenting with all the new features

Remember: ES6 isn't just about new syntax - it's about writing better, cleaner, and more maintainable code. You're now equipped with modern JavaScript superpowers! 🎉