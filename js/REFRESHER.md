<div align="center">

  <h1> JavaScript Refresher</h1>
<sub>Author:
<a href="https://www.linkedin.com/in/sjayanthkumar/" target="_blank">Jayanth Kumar</a><br>
<small> October, 2022</small>
</sub>

</div>


- [JavaScript Refresher](#javascript-refresher)
  - [0. Adding JavaScript to a Web Page](#0-adding-javascript-to-a-web-page)
    - [Inline Script](#inline-script)
    - [Internal Script](#internal-script)
    - [External Script](#external-script)
    - [Multiple External Scripts](#multiple-external-scripts)
  - [1. Variables](#1-variables)
  - [2. Data types](#2-data-types)
  - [3. Arrays](#3-arrays)
    - [How to create an empty array](#how-to-create-an-empty-array)
    - [How to create an array with values](#how-to-create-an-array-with-values)
    - [Creating an array using split](#creating-an-array-using-split)
    - [Accessing array items using index](#accessing-array-items-using-index)
    - [Modifying array element](#modifying-array-element)
    - [Methods to manipulate array](#methods-to-manipulate-array)
      - [Array Constructor](#array-constructor)
      - [Creating static values with fill](#creating-static-values-with-fill)
      - [Concatenating array using concat](#concatenating-array-using-concat)
      - [Getting array length](#getting-array-length)
      - [Getting index of an element in an array](#getting-index-of-an-element-in-an-array)
      - [Getting last index of an element in array](#getting-last-index-of-an-element-in-array)
      - [Checking array](#checking-array)
      - [Converting array to string](#converting-array-to-string)
      - [Joining array elements](#joining-array-elements)
      - [Slice array elements](#slice-array-elements)
      - [Splice method in array](#splice-method-in-array)
      - [Adding item to an array using push](#adding-item-to-an-array-using-push)
      - [Removing the end element using pop](#removing-the-end-element-using-pop)
      - [Removing an element from the beginning](#removing-an-element-from-the-beginning)
      - [Add an element from the beginning](#add-an-element-from-the-beginning)
      - [Reversing array order](#reversing-array-order)
      - [Sorting elements in array](#sorting-elements-in-array)
    - [Array of arrays](#array-of-arrays)
  - [💻 Exercise](#-exercise)
      - [Exercise: Level 1](#exercise-level-1)
      - [Exercise: Level 2](#exercise-level-2)
      - [Exercise: Level 3](#exercise-level-3)
  - [4. Conditionals](#4-conditionals)
    - [If](#if)
    - [If Else](#if-else)
    - [If Else if Else](#if-else-if-else)
    - [Switch](#switch)
    - [Ternary Operators](#ternary-operators)
  - [💻 Exercises](#-exercises)
      - [Exercises: Level 1](#exercises-level-1)
      - [Exercises: Level 2](#exercises-level-2)
      - [Exercises: Level 3](#exercises-level-3)
  - [5. Loops](#5-loops)
    - [Types of Loops](#types-of-loops)
      - [1. for](#1-for)
      - [2. while](#2-while)
      - [3. do while](#3-do-while)
      - [4. for of](#4-for-of)
      - [5. forEach](#5-foreach)
      - [6. for in](#6-for-in)
    - [Interrupting a loop and skipping an item](#interrupting-a-loop-and-skipping-an-item)
      - [break](#break)
      - [continue](#continue)
    - [Conclusions](#conclusions)


## JavaScript Refresher

### 0. Adding JavaScript to a Web Page

JavaScript can be added to a web page in three different ways:

- **_Inline script_**
- **_Internal script_**
- **_External script_**
- **_Multiple External scripts_**

The following sections show different ways of adding JavaScript code to your web page.

#### Inline Script

Create a project folder on your desktop or in any location, name it 30DaysOfJS and create an **_index.html_** file in the project folder. Then paste the following code and open it in a browser, for example [Chrome](https://www.google.com/chrome/).

```html
<!DOCTYPE html>
<html>
  <head>
    <title>30DaysOfScript:Inline Script</title>
  </head>
  <body>
    <button onclick="alert('Welcome to 30DaysOfJavaScript!')">Click Me</button>
  </body>
</html>
```

Now, you just wrote your first inline script. We can create a pop up alert message using the _alert()_ built-in function.

#### Internal Script

The internal script can be written in the _head_ or the _body_, but it is preferred to put it on the body of the HTML document.
First, let us write on the head part of the page.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>30DaysOfScript:Internal Script</title>
    <script>
      console.log('Welcome to 30DaysOfJavaScript')
    </script>
  </head>
  <body></body>
</html>
```

This is how we write an internal script most of the time. Writing the JavaScript code in the body section is the most preferred option. Open the browser console to see the output from the console.log()

```html
<!DOCTYPE html>
<html>
  <head>
    <title>30DaysOfScript:Internal Script</title>
  </head>
  <body>
    <button onclick="alert('Welcome to 30DaysOfJavaScript!');">Click Me</button>
    <script>
      console.log('Welcome to 30DaysOfJavaScript')
    </script>
  </body>
</html>
```

Open the browser console to see the output from the console.log()

![js code from vscode](../images/js_code_vscode.png)

#### External Script

Similar to the internal script, the external script link can be on the header or body, but it is preferred to put it in the body.
First, we should create an external JavaScript file with .js extension. All files ending with .js extension. All files ending with .js extension are JavaScript files. Create a file named introduction.js inside your project directory and write the following code and link this .js file at the bottom of the body.

```js
console.log('Welcome to JavaScript')
```

External scripts in the _head_:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>JavaScript:External script</title>
    <script src="introduction.js"></script>
  </head>
  <body></body>
</html>
```

External scripts in the _body_:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>JavaScript:External script</title>
  </head>
  <body>
    //it could be in the header or in the body // Here is the recommended place
    to put the external script
    <script src="introduction.js"></script>
  </body>
</html>
```

Open the browser console to see the output of the console.log()

#### Multiple External Scripts

We can also link multiple external JavaScript files to a web page.
Create a helloworld.js file inside the 30DaysOfJS folder and write the following code.

```js
console.log('Hello, World!')
```

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Multiple External Scripts</title>
  </head>
  <body>
    <script src="./helloworld.js"></script>
    <script src="./introduction.js"></script>
  </body>
</html>
```

_Your main.js file should be below all other scripts_. It is very important to remember this.



### 1. Variables

We use _var_, _let_ and _const_ to declare a variable. The _var_ is functions scope, however _let_ and _const_ are block scope. In this challenge we use ES6 and above features of JavaScript. Avoid using _var_.

```js
let firstName = 'Asabeneh'
firstName = 'Eyob'

const PI = 3.14 // Not allowed to reassign PI to a new value
// PI = 3.
```

### 2. Data types

### 3. Arrays

In contrast to variables, an array can store _multiple values_. Each value in an array has an _index_, and each index has _a reference in a memory address_. Each value can be accessed by using their _indexes_. The index of an array starts from _zero_, and the index of the last element is less by one from the length of the array.

An array is a collection of different data types which are ordered and changeable(modifiable). An array allows storing duplicate elements and different data types. An array can be empty, or it may have different data type values.

#### How to create an empty array

In JavaScript, we can create an array in different ways. Let us see different ways to create an array.
It is very common to use _const_ instead of _let_ to declare an array variable. If you are using const it means you do not use that variable name again.

- Using Array constructor

```js
// syntax
const arr = Array()
// or
// let arr = new Array()
console.log(arr) // []
```

- Using square brackets([])

```js
// syntax
// This the most recommended way to create an empty list
const arr = []
console.log(arr)
```

#### How to create an array with values

Array with initial values. We use _length_ property to find the length of an array.

```js
const numbers = [0, 3.14, 9.81, 37, 98.6, 100] // array of numbers
const fruits = ['banana', 'orange', 'mango', 'lemon'] // array of strings, fruits
const vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'] // array of strings, vegetables
const animalProducts = ['milk', 'meat', 'butter', 'yoghurt'] // array of strings, products
const webTechs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB'] // array of web technologies
const countries = ['Finland', 'Denmark', 'Sweden', 'Norway', 'Iceland'] // array of strings, countries

// Print the array and its length

console.log('Numbers:', numbers)
console.log('Number of numbers:', numbers.length)

console.log('Fruits:', fruits)
console.log('Number of fruits:', fruits.length)

console.log('Vegetables:', vegetables)
console.log('Number of vegetables:', vegetables.length)

console.log('Animal products:', animalProducts)
console.log('Number of animal products:', animalProducts.length)

console.log('Web technologies:', webTechs)
console.log('Number of web technologies:', webTechs.length)

console.log('Countries:', countries)
console.log('Number of countries:', countries.length)
```

```sh
Numbers: [0, 3.14, 9.81, 37, 98.6, 100]
Number of numbers: 6
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

- Array can have items of different data types

```js
const arr = [
  'Asabeneh',
  250,
  true,
  { country: 'Finland', city: 'Helsinki' },
  { skills: ['HTML', 'CSS', 'JS', 'React', 'Python'] },
] // arr containing different data types
console.log(arr)
```

#### Creating an array using split

As we have seen in the earlier section, we can split a string at different positions, and we can change to an array. Let us see the examples below.

```js
let js = 'JavaScript'
const charsInJavaScript = js.split('')

console.log(charsInJavaScript) // ["J", "a", "v", "a", "S", "c", "r", "i", "p", "t"]

let companiesString = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
const companies = companiesString.split(',')

console.log(companies) // ["Facebook", " Google", " Microsoft", " Apple", " IBM", " Oracle", " Amazon"]
let txt =
  'I love teaching and empowering people. I teach HTML, CSS, JS, React, Python.'
const words = txt.split(' ')

console.log(words)
// the text has special characters think how you can just get only the words
// ["I", "love", "teaching", "and", "empowering", "people.", "I", "teach", "HTML,", "CSS,", "JS,", "React,", "Python"]
```

#### Accessing array items using index

We access each element in an array using their index. An array index starts from 0. The picture below clearly shows the index of each element in the array.



```js
const fruits = ['banana', 'orange', 'mango', 'lemon']
let firstFruit = fruits[0] // we are accessing the first item using its index

console.log(firstFruit) // banana

secondFruit = fruits[1]
console.log(secondFruit) // orange

let lastFruit = fruits[3]
console.log(lastFruit) // lemon
// Last index can be calculated as follows

let lastIndex = fruits.length - 1
lastFruit = fruits[lastIndex]

console.log(lastFruit) // lemon
```

```js
const numbers = [0, 3.14, 9.81, 37, 98.6, 100] // set of numbers

console.log(numbers.length) // => to know the size of the array, which is 6
console.log(numbers) // -> [0, 3.14, 9.81, 37, 98.6, 100]
console.log(numbers[0]) //  -> 0
console.log(numbers[5]) //  -> 100

let lastIndex = numbers.length - 1
console.log(numbers[lastIndex]) // -> 100
```

```js
const webTechs = [
  'HTML',
  'CSS',
  'JavaScript',
  'React',
  'Redux',
  'Node',
  'MongoDB',
] // List of web technologies

console.log(webTechs) // all the array items
console.log(webTechs.length) // => to know the size of the array, which is 7
console.log(webTechs[0]) //  -> HTML
console.log(webTechs[6]) //  -> MongoDB

let lastIndex = webTechs.length - 1
console.log(webTechs[lastIndex]) // -> MongoDB
```

```js
const countries = [
  'Albania',
  'Bolivia',
  'Canada',
  'Denmark',
  'Ethiopia',
  'Finland',
  'Germany',
  'Hungary',
  'Ireland',
  'Japan',
  'Kenya',
] // List of countries

console.log(countries) // -> all countries in array
console.log(countries[0]) //  -> Albania
console.log(countries[10]) //  -> Kenya

let lastIndex = countries.length - 1
console.log(countries[lastIndex]) //  -> Kenya
```

```js
const shoppingCart = [
  'Milk',
  'Mango',
  'Tomato',
  'Potato',
  'Avocado',
  'Meat',
  'Eggs',
  'Sugar',
] // List of food products

console.log(shoppingCart) // -> all shoppingCart in array
console.log(shoppingCart[0]) //  -> Milk
console.log(shoppingCart[7]) //  -> Sugar

let lastIndex = shoppingCart.length - 1
console.log(shoppingCart[lastIndex]) //  -> Sugar
```

#### Modifying array element

An array is mutable(modifiable). Once an array is created, we can modify the contents of the array elements.

```js
const numbers = [1, 2, 3, 4, 5]
numbers[0] = 10 // changing 1 at index 0 to 10
numbers[1] = 20 // changing  2 at index 1 to 20

console.log(numbers) // [10, 20, 3, 4, 5]

const countries = [
  'Albania',
  'Bolivia',
  'Canada',
  'Denmark',
  'Ethiopia',
  'Finland',
  'Germany',
  'Hungary',
  'Ireland',
  'Japan',
  'Kenya',
]

countries[0] = 'Afghanistan' // Replacing Albania by Afghanistan
let lastIndex = countries.length - 1
countries[lastIndex] = 'Korea' // Replacing Kenya by Korea

console.log(countries)
```

```sh
["Afghanistan", "Bolivia", "Canada", "Denmark", "Ethiopia", "Finland", "Germany", "Hungary", "Ireland", "Japan", "Korea"]
```

#### Methods to manipulate array

There are different methods to manipulate an array. These are some of the available methods to deal with arrays:_Array, length, concat, indexOf, slice, splice, join, toString, includes, lastIndexOf, isArray, fill, push, pop, shift, unshift_

##### Array Constructor

Array:To create an array.

```js
const arr = Array() // creates an an empty array
console.log(arr)

const eightEmptyValues = Array(8) // it creates eight empty values
console.log(eightEmptyValues) // [empty x 8]
```

##### Creating static values with fill

fill: Fill all the array elements with a static value

```js
const arr = Array() // creates an an empty array
console.log(arr)

const eightXvalues = Array(8).fill('X') // it creates eight element values filled with 'X'
console.log(eightXvalues) // ['X', 'X','X','X','X','X','X','X']

const eight0values = Array(8).fill(0) // it creates eight element values filled with '0'
console.log(eight0values) // [0, 0, 0, 0, 0, 0, 0, 0]

const four4values = Array(4).fill(4) // it creates 4 element values filled with '4'
console.log(four4values) // [4, 4, 4, 4]
```

##### Concatenating array using concat

concat:To concatenate two arrays.

```js
const firstList = [1, 2, 3]
const secondList = [4, 5, 6]
const thirdList = firstList.concat(secondList)

console.log(thirdList) // [1, 2, 3, 4, 5, 6]
```

```js
const fruits = ['banana', 'orange', 'mango', 'lemon'] // array of fruits
const vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'] // array of vegetables
const fruitsAndVegetables = fruits.concat(vegetables) // concatenate the two arrays

console.log(fruitsAndVegetables)
```

```sh
["banana", "orange", "mango", "lemon", "Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
```

##### Getting array length

Length:To know the size of the array

```js
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.length) // -> 5 is the size of the array
```

##### Getting index of an element in an array

indexOf:To check if an item exist in an array. If it exists it returns the index else it returns -1.

```js
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.indexOf(5)) // -> 4
console.log(numbers.indexOf(0)) // -> -1
console.log(numbers.indexOf(1)) // -> 0
console.log(numbers.indexOf(6)) // -> -1
```

Check an element if it exist in an array.

- Check items in a list

```js
// let us check if a banana exist in the array

const fruits = ['banana', 'orange', 'mango', 'lemon']
let index = fruits.indexOf('banana') // 0

if (index != -1) {
  console.log('This fruit does exist in the array')
} else {
  console.log('This fruit does not exist in the array')
}
// This fruit does exist in the array

// we can use also ternary here
index != -1
  ? console.log('This fruit does exist in the array')
  : console.log('This fruit does not exist in the array')

// let us check if a avocado exist in the array
let indexOfAvocado = fruits.indexOf('avocado') // -1, if the element not found index is -1
if (indexOfAvocado != -1) {
  console.log('This fruit does exist in the array')
} else {
  console.log('This fruit does not exist in the array')
}
// This fruit does not exist in the array
```

##### Getting last index of an element in array

lastIndexOf: It gives the position of the last item in the array. If it exist, it returns the index else it returns -1.

```js
const numbers = [1, 2, 3, 4, 5, 3, 1, 2]

console.log(numbers.lastIndexOf(2)) // 7
console.log(numbers.lastIndexOf(0)) // -1
console.log(numbers.lastIndexOf(1)) //  6
console.log(numbers.lastIndexOf(4)) //  3
console.log(numbers.lastIndexOf(6)) // -1
```

includes:To check if an item exist in an array. If it exist it returns the true else it returns false.

```js
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.includes(5)) // true
console.log(numbers.includes(0)) // false
console.log(numbers.includes(1)) // true
console.log(numbers.includes(6)) // false

const webTechs = [
  'HTML',
  'CSS',
  'JavaScript',
  'React',
  'Redux',
  'Node',
  'MongoDB',
] // List of web technologies

console.log(webTechs.includes('Node')) // true
console.log(webTechs.includes('C')) // false
```

##### Checking array

Array.isArray:To check if the data type is an array

```js
const numbers = [1, 2, 3, 4, 5]
console.log(Array.isArray(numbers)) // true

const number = 100
console.log(Array.isArray(number)) // false
```

##### Converting array to string

toString:Converts array to string

```js
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.toString()) // 1,2,3,4,5

const names = ['Asabeneh', 'Mathias', 'Elias', 'Brook']
console.log(names.toString()) // Asabeneh,Mathias,Elias,Brook
```

##### Joining array elements

join: It is used to join the elements of the array, the argument we passed in the join method will be joined in the array and return as a string. By default, it joins with a comma, but we can pass different string parameter which can be joined between the items.

```js
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.join()) // 1,2,3,4,5

const names = ['Asabeneh', 'Mathias', 'Elias', 'Brook']

console.log(names.join()) // Asabeneh,Mathias,Elias,Brook
console.log(names.join('')) //AsabenehMathiasEliasBrook
console.log(names.join(' ')) //Asabeneh Mathias Elias Brook
console.log(names.join(', ')) //Asabeneh, Mathias, Elias, Brook
console.log(names.join(' # ')) //Asabeneh # Mathias # Elias # Brook

const webTechs = [
  'HTML',
  'CSS',
  'JavaScript',
  'React',
  'Redux',
  'Node',
  'MongoDB',
] // List of web technologies

console.log(webTechs.join()) // "HTML,CSS,JavaScript,React,Redux,Node,MongoDB"
console.log(webTechs.join(' # ')) // "HTML # CSS # JavaScript # React # Redux # Node # MongoDB"
```

##### Slice array elements

Slice: To cut out a multiple items in range. It takes two parameters:starting and ending position. It doesn't include the ending position.

```js
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.slice()) // -> it copies all  item
console.log(numbers.slice(0)) // -> it copies all  item
console.log(numbers.slice(0, numbers.length)) // it copies all  item
console.log(numbers.slice(1, 4)) // -> [2,3,4] // it doesn't include the ending position
```

##### Splice method in array

Splice: It takes three parameters:Starting position, number of times to be removed and number of items to be added.

```js
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.splice()) // -> remove all items
```

```js
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.splice(0, 1)) // remove the first item
```

```js
const numbers = [1, 2, 3, 4, 5, 6]
console.log(numbers.splice(3, 3, 7, 8, 9)) // -> [1, 2, 3, 7, 8, 9] //it removes three item and replace three items
```

##### Adding item to an array using push

Push: adding item in the end. To add item to the end of an existing array we use the push method.

```js
// syntax
const arr = ['item1', 'item2', 'item3']
arr.push('new item')

console.log(arr)
// ['item1', 'item2','item3','new item']
```

```js
const numbers = [1, 2, 3, 4, 5]
numbers.push(6)

console.log(numbers) // -> [1,2,3,4,5,6]

numbers.pop() // -> remove one item from the end
console.log(numbers) // -> [1,2,3,4,5]
```

```js
let fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.push('apple')

console.log(fruits) // ['banana', 'orange', 'mango', 'lemon', 'apple']

fruits.push('lime')
console.log(fruits) // ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
```

##### Removing the end element using pop

pop: Removing item in the end.

```js
const numbers = [1, 2, 3, 4, 5]
numbers.pop() // -> remove one item from the end

console.log(numbers) // -> [1,2,3,4]
```

##### Removing an element from the beginning

shift: Removing one array element in the beginning of the array.

```js
const numbers = [1, 2, 3, 4, 5]
numbers.shift() // -> remove one item from the beginning

console.log(numbers) // -> [2,3,4,5]
```

##### Add an element from the beginning

unshift: Adding array element in the beginning of the array.

```js
const numbers = [1, 2, 3, 4, 5]
numbers.unshift(0) // -> add one item from the beginning

console.log(numbers) // -> [0,1,2,3,4,5]
```

##### Reversing array order

reverse: reverse the order of an array.

```js
const numbers = [1, 2, 3, 4, 5]
numbers.reverse() // -> reverse array order

console.log(numbers) // [5, 4, 3, 2, 1]

numbers.reverse()
console.log(numbers) // [1, 2, 3, 4, 5]
```

##### Sorting elements in array

sort: arrange array elements in ascending order. Sort takes a call back function, we will see how we use sort with a call back function in the coming sections.

```js
const webTechs = [
  'HTML',
  'CSS',
  'JavaScript',
  'React',
  'Redux',
  'Node',
  'MongoDB',
]

webTechs.sort()
console.log(webTechs) // ["CSS", "HTML", "JavaScript", "MongoDB", "Node", "React", "Redux"]

webTechs.reverse() // after sorting we can reverse it
console.log(webTechs) // ["Redux", "React", "Node", "MongoDB", "JavaScript", "HTML", "CSS"]
```

#### Array of arrays

Array can store different data types including an array itself. Let us create an array of arrays

```js
const firstNums = [1, 2, 3]
const secondNums = [1, 4, 9]

const arrayOfArray = [
  [1, 2, 3],
  [1, 2, 3],
]
console.log(arrayOfArray[0]) // [1, 2, 3]

const frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
const backEnd = ['Node', 'Express', 'MongoDB']
const fullStack = [frontEnd, backEnd]
console.log(fullStack) // [["HTML", "CSS", "JS", "React", "Redux"], ["Node", "Express", "MongoDB"]]
console.log(fullStack.length) // 2
console.log(fullStack[0]) // ["HTML", "CSS", "JS", "React", "Redux"]
console.log(fullStack[1]) // ["Node", "Express", "MongoDB"]
```

### 💻 Exercise

##### Exercise: Level 1

```js
const countries = [
  'Albania',
  'Bolivia',
  'Canada',
  'Denmark',
  'Ethiopia',
  'Finland',
  'Germany',
  'Hungary',
  'Ireland',
  'Japan',
  'Kenya',
]

const webTechs = [
  'HTML',
  'CSS',
  'JavaScript',
  'React',
  'Redux',
  'Node',
  'MongoDB',
]
```

1. Declare an _empty_ array;
2. Declare an array with more than 5 number of elements
3. Find the length of your array
4. Get the first item, the middle item and the last item of the array
5. Declare an array called _mixedDataTypes_, put different data types in the array and find the length of the array. The array size should be greater than 5
6. Declare an array variable name itCompanies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
7. Print the array using _console.log()_
8. Print the number of companies in the array
9. Print the first company, middle and last company
10. Print out each company


##### Exercise: Level 2

1. Create a separate countries.js file and store the countries array into this file, create a separate file web_techs.js and store the webTechs array into this file. Access both file in main.js file
1. First remove all the punctuations and change the string to array and count the number of words in the array

   ```js
   let text =
     'I love teaching and empowering people. I teach HTML, CSS, JS, React, Python.'
   console.log(words)
   console.log(words.length)
   ```

   ```sh
   ["I", "love", "teaching", "and", "empowering", "people", "I", "teach", "HTML", "CSS", "JS", "React", "Python"]

   13
   ```

1. In the following shopping cart add, remove, edit items

   ```js
   const shoppingCart = ['Milk', 'Coffee', 'Tea', 'Honey']
   ```

   - add 'Meat' in the beginning of your shopping cart if it has not been already added
   - add Sugar at the end of you shopping cart if it has not been already added
   - remove 'Honey' if you are allergic to honey
   - modify Tea to 'Green Tea'

1. In countries array check if 'Ethiopia' exists in the array if it exists print 'ETHIOPIA'. If it does not exist add to the countries list.
1. In the webTechs array check if Sass exists in the array and if it exists print 'Sass is a CSS preprocess'. If it does not exist add Sass to the array and print the array.
1. Concatenate the following two variables and store it in a fullStack variable.

   ```js
   const frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
   const backEnd = ['Node', 'Express', 'MongoDB']

   console.log(fullStack)
   ```

   ```sh
   ["HTML", "CSS", "JS", "React", "Redux", "Node", "Express", "MongoDB"]
   ```

##### Exercise: Level 3

1. The following is an array of 10 students ages:
   `js const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] ` - Sort the array and find the min and max age - Find the median age(one middle item or two middle items divided by two) - Find the average age(all items divided by number of items) - Find the range of the ages(max minus min) - Compare the value of (min - average) and (max - average), use _abs()_ method

   1.Slice the first ten countries from the [countries array](https://github.com/Asabeneh/30DaysOfJavaScript/tree/master/data/countries.js)

1. Find the middle country(ies) in the [countries array](https://github.com/Asabeneh/30DaysOfJavaScript/tree/master/data/countries.js)
1. Divide the countries array into two equal arrays if it is even. If countries array is not even , one more country for the first half.

### 4. Conditionals

Conditional statements are used for make decisions based on different conditions.
By default , statements in JavaScript script executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two ways:

- Conditional execution: a block of one or more statements will be executed if a certain expression is true
- Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover _if_, _else_ , _else if_ statements. The comparison and logical operators we learned in the previous sections will be useful in here.

Conditions can be implementing using the following ways:

- if
- if else
- if else if else
- switch
- ternary operator

#### If

In JavaScript and other programming languages the key word _if_ is to used check if a condition is true and to execute the block code. To create an if condition, we need _if_ keyword, condition inside a parenthesis and block of code inside a curly bracket({}).

```js
// syntax
if (condition) {
  //this part of code runs for truthy condition
}
```

**Example:**

```js
let num = 3
if (num > 0) {
  console.log(`${num} is a positive number`)
}
//  3 is a positive number
```

As you can see in the condition example above, 3 is greater than 0, so it is a positive number. The condition was true and the block of code was executed. However, if the condition is false, we won't see any results.

```js
let isRaining = true
if (isRaining) {
  console.log('Remember to take your rain coat.')
}
```

The same goes for the second condition, if isRaining is false the if block will not be executed and we do not see any output. In order to see the result of a falsy condition, we should have another block, which is going to be _else_.

#### If Else

If condition is true the first block will be executed, if not the else condition will be executed.

```js
// syntax
if (condition) {
  // this part of code runs for truthy condition
} else {
  // this part of code runs for false condition
}
```

```js
let num = 3
if (num > 0) {
  console.log(`${num} is a positive number`)
} else {
  console.log(`${num} is a negative number`)
}
//  3 is a positive number

num = -3
if (num > 0) {
  console.log(`${num} is a positive number`)
} else {
  console.log(`${num} is a negative number`)
}
//  -3 is a negative number
```

```js
let isRaining = true
if (isRaining) {
  console.log('You need a rain coat.')
} else {
  console.log('No need for a rain coat.')
}
// You need a rain coat.

isRaining = false
if (isRaining) {
  console.log('You need a rain coat.')
} else {
  console.log('No need for a rain coat.')
}
// No need for a rain coat.
```

The last condition is false, therefore the else block was executed. What if we have more than two conditions? In that case, we would use _else if_ conditions.

#### If Else if Else

On our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions instead we make decisions based on multiple conditions. As similar to our daily life, programming is also full of conditions. We use _else if_ when we have multiple conditions.

```js
// syntax
if (condition) {
  // code
} else if (condition) {
  // code
} else {
  //  code
}
```

**Example:**

```js
let a = 0
if (a > 0) {
  console.log(`${a} is a positive number`)
} else if (a < 0) {
  console.log(`${a} is a negative number`)
} else if (a == 0) {
  console.log(`${a} is zero`)
} else {
  console.log(`${a} is not a number`)
}
```

```js
// if else if else
let weather = 'sunny'
if (weather === 'rainy') {
  console.log('You need a rain coat.')
} else if (weather === 'cloudy') {
  console.log('It might be cold, you need a jacket.')
} else if (weather === 'sunny') {
  console.log('Go out freely.')
} else {
  console.log('No need for rain coat.')
}
```

#### Switch

Switch is an alternative for **if else if else else**.
The switch statement starts with a _switch_ keyword followed by a parenthesis and code block. Inside the code block we will have different cases. Case block runs if the value in the switch statement parenthesis matches with the case value. The break statement is to terminate execution so the code execution does not go down after the condition is satisfied. The default block runs if all the cases don't satisfy the condition.

```js
switch (caseValue) {
  case 1:
    // code
    break
  case 2:
    // code
    break
  case 3:
  // code
  default:
  // code
}
```

```js
let weather = 'cloudy'
switch (weather) {
  case 'rainy':
    console.log('You need a rain coat.')
    break
  case 'cloudy':
    console.log('It might be cold, you need a jacket.')
    break
  case 'sunny':
    console.log('Go out freely.')
    break
  default:
    console.log(' No need for rain coat.')
}

// Switch More Examples
let dayUserInput = prompt('What day is today ?')
let day = dayUserInput.toLowerCase()

switch (day) {
  case 'monday':
    console.log('Today is Monday')
    break
  case 'tuesday':
    console.log('Today is Tuesday')
    break
  case 'wednesday':
    console.log('Today is Wednesday')
    break
  case 'thursday':
    console.log('Today is Thursday')
    break
  case 'friday':
    console.log('Today is Friday')
    break
  case 'saturday':
    console.log('Today is Saturday')
    break
  case 'sunday':
    console.log('Today is Sunday')
    break
  default:
    console.log('It is not a week day.')
}
```

// Examples to use conditions in the cases

```js
let num = prompt('Enter number')
switch (true) {
  case num > 0:
    console.log('Number is positive')
    break
  case num == 0:
    console.log('Numbers is zero')
    break
  case num < 0:
    console.log('Number is negative')
    break
  default:
    console.log('Entered value was not a number')
}
```

#### Ternary Operators

Ternary operator is very common in _React_. It is a short way to write if else statement. In React we use ternary operator in many cases.

To generalize, ternary operator is another way to write conditionals.

```js
let isRaining = true
isRaining
  ? console.log('You need a rain coat.')
  : console.log('No need for a rain coat.')
```

### 💻 Exercises

##### Exercises: Level 1

1. Get user input using prompt(“Enter your age:”). If user is 18 or older , give feedback:'You are old enough to drive' but if not 18 give another feedback stating to wait for the number of years he needs to turn 18.

   ```sh
   Enter your age: 30
   You are old enough to drive.

   Enter your age:15
   You are left with 3 years to drive.
   ```

1. Compare the values of myAge and yourAge using if … else. Based on the comparison and log the result to console stating who is older (me or you). Use prompt(“Enter your age:”) to get the age as input.

   ```sh
   Enter your age: 30
   You are 5 years older than me.
   ```

1. If a is greater than b return 'a is greater than b' else 'a is less than b'. Try to implement it in two ways

   - using if else
   - ternary operator.

   ```js
   let a = 4
   let b = 3
   ```

   ```sh
     4 is greater than 3
   ```

1. Even numbers are divisible by 2 and the remainder is zero. How do you check, if a number is even or not using JavaScript?

   ```sh
   Enter a number: 2
   2 is an even number

   Enter a number: 9
   9 is is an odd number.
   ```

##### Exercises: Level 2

1. Write a code which can give grades to students according to theirs scores:
   - 80-100, A
   - 70-89, B
   - 60-69, C
   - 50-59, D
   - 0-49, F
1. Check if the season is Autumn, Winter, Spring or Summer.
   If the user input is :
   - September, October or November, the season is Autumn.
   - December, January or February, the season is Winter.
   - March, April or May, the season is Spring
   - June, July or August, the season is Summer
1. Check if a day is weekend day or a working day. Your script will take day as an input.

```sh
    What is the day  today? Saturday
    Saturday is a weekend.

    What is the day today? saturDaY
    Saturday is a weekend.

    What is the day today? Friday
    Friday is a working day.

    What is the day today? FrIDAy
    Friday is a working day.
```

##### Exercises: Level 3

1. Write a program which tells the number of days in a month.

```sh
  Enter a month: January
  January has 31 days.

  Enter a month: JANUARY
  January has 31 day

  Enter a month: February
  February has 28 days.

  Enter a month: FEbruary
  February has 28 days.
```

1. Write a program which tells the number of days in a month, now consider leap year.

### 5. Loops

In programming we use different loops to carry out repetitive tasks. Therefore, loop can help us to automate tedious and repetitive task. JavaScript has also different types of loops which we can use to work on repetitive task.

Imagine if your are asked to print Hello world one thousand times without a loop, it may take an hour or two to do this tedious task. However, using loop we can print it in less than a second.

Loops:

- for
- while
- do while
- for of
- forEach
- for in

A loop usually goes until the condition gets false. But sometimes we like to interrupt the loop or skip an item during iteration. We use _break_ to interrupt the loop and _continue_ to skip an item during iteration.

#### Types of Loops

##### 1. for

We use for loop when we know how many iteration we go. Let's see the following example

```js
// for loop syntax

for (initialization, condition, increment/decrement) {
    code goes here
}
```

This code prints from 0 to 5.

```js
for (let i = 0; i < 6; i++) {
  console.log(i)
}
```

For example if we want to sum all the numbers from 0 to 100.

```js
let sum = 0
for (let i = 0; i < 101; i++) {
  sum += i
}

console.log(sum)
```

If we want to sum only even numbers:

```js
let sum = 0
for (let i = 0; i < 101; i += 2) {
  sum += i
}

console.log(sum)

// or another way

let total = 0
for (let i = 0; i < 101; i++) {
  if (i % 2 == 0) {
    total += i
  }
}
console.log(total)
```

This code iterates through the array

```js
const nums = [1, 2, 3, 4, 5]
for (let i = 0; i < 6; i++) {
  console.log(nums[i])
}
```

This code prints 5 to 0. Looping in reverse order

```js
for (let i = 5; i >= 0; i--) {
  console.log(i)
}
```

The Code below can reverse an array.

```js
const nums = [1, 2, 3, 4, 5]
const lastIndex = nums.length - 1
const newArray = []
for (let i = lastIndex; i >= 0; i--) {
  newArray.push(nums[i])
}

console.log(newArray)
```

##### 2. while

We use the while loop when we do not know how man iteration we go in advance.

```js
let count = prompt('Enter a positive number: ')
while (count > 0) {
  console.log(count)
  count--
}
```

##### 3. do while

Do while run at least once if the condition is true or false

```js
let count = 0
do {
  console.log(count)
  count++
} while (count < 11)
```

The code below runs ones though the condition is false

```js
let count = 11
do {
  console.log(count)
  count++
} while (count < 11)
```

While loop is the least important loop in many programming languages.

##### 4. for of

The for of loop is very handy to use it with array. If we are not interested in the index of the array a for of loop is preferable to regular for loop or forEach loop.

```js
const numbers = [1, 2, 3, 4, 5]
for (const number of numbers) {
  console.log(number)
}

const countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for (const country of countries) {
  console.log(country.toUpperCase())
}
```

##### 5. forEach

If we are interested in the index of the array forEach is preferable to for of loop. The forEach array method takes a callback function, the callback function takes three arguments: the item, the index and the array itself.

```js
const numbers = [1, 2, 3, 4, 5]
numbers.forEach((number, i) => {
  console.log(number, i)
})

const countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
countries.forEach((country, i, arr) => {
  console.log(i, country.toUpperCase())
})
```

##### 6. for in

The for in loop can be used with object literals to get the keys of the object.

```js
const user = {
  firstName: 'Asabeneh',
  lastName: 'Yetayeh',
  age: 250,
  country: 'Finland',
  skills: ['HTML', 'CSS', 'JS', 'React', 'Node', 'Python', 'D3.js'],
}

for (const key in user) {
  console.log(key, user[key])
}
```

#### Interrupting a loop and skipping an item

##### break

Break is used to interrupt a loop.

```js
for (let i = 0; i <= 5; i++) {
  if (i == 3) {
    break
  }
  console.log(i)
}

// 0 1 2
```

The above code stops if 3 found in the iteration process.

##### continue

We use the keyword continue to skip a certain iterations.

```js
for (let i = 0; i <= 5; i++) {
  if (i == 3) {
    continue
  }
  console.log(i)
}
// 0 1 2 4 5
```

#### Conclusions

- Regular for loop can be used anywhere when the number of iteration is known.
- While loop when the number of iteration is not know
- Do while loop and while loop are almost the same but do while loop run at least once even when the condition is false
- for of is used only for array
- forEach is used for array
- for in is used for object

  </body>
</html>
```



🌕 You are amazing! You have just completed the challenge and you are on your way to greatness. Now you are a JavaScript Ninja!

🎉 CONGRATULATIONS ! 🎉

