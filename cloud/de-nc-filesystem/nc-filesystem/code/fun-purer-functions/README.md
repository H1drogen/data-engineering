# Building pure functions

These katas are designed to make you think about building functions that are **pure** and part of this means creating functions without _side effects_ so they don't for example mutate the data they are passed as arguments. Functions that have _side effects_ can expose you to bugs that are often difficult to find, so avoiding side effects as soon as possible is a very good habit to get in to from the beginning.

As with previous days, you will need to set up a few things first:

1. Create a `package.json`

2. Install your dependencies (the amazing Jest as ever)

3. Update the scripts section of your `package.json` so you can get Jest to run your test files

---

## Core Tasks

Implement the following functions using TDD ...

### `removeLastNumber`

This function should as its only argument take:

- an array of numbers

This function should return a new array of numbers with the last one removed

```js
removeLastNumber([1, 2, 3, 4]);

/* should return 
[1,2,3]
*/
```

---

### `raiseSalaries`

This function should take as its arguments:

- an array representing a list of employees and a number (representing a percentage increase)
- each employee will be represented as an object with a `name` and a `salary` property

It should return a new array of employees with their salary now increased by the given percentage increase. The new salaries should be rounded up to the nearest integer. None of the original employee objects should be mutated.

```js
raiseSalaries(
	[
		{ name: "Alice", salary: 3000 },
		{ name: "Bob", salary: 2000 },
		{ name: "Vel", salary: 4500 }
	],
	10
);
/* should return 
[{ name: 'Alice', salary: 3300 },
 { name: 'Bob', salary: 2200 }, 
 { name: 'Vel', salary: 4950 }
]
*/
```

---

### `updateTasks`

This function should take as its arguments:

- a person object (with name and tasks properties)
- one or more new tasks

The function should return a new person object with a new tasks properties. The tasks property from the input object should not be mutated.

```js
updateTasks(
	{ name: "Anat", tasks: ["feed Schnitzel", "Go to pottery"] },
	"read books",
	"tidy room"
);
/* should return 
{
  name: 'Anat',
  tasks: ['feed Schnitzel', 'Go to pottery', 'read books', 'tidy room']
}
*/
```

---

## Further Tasks

### `cloneObject`

This function should take as its arguments:

- a target object (values are only primitives)
- a source object (values are only primitives)

The function should return the target object with all the key-value pairs from the source object copied over. This function _should_ mutate the target object. This function has identical functionality to [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

---

### `calculateConfectioneryCosts`

Write a function that takes an array of pop star objects with information about the amount they have spent so far this year on confectionery at the cinema, and how much they have spent on today's visit. It should return a **new array** of **new objects** with a property for the pop star's `name` and the `yearlyCumulativeSpend` property updated to include today's costs.

```js
const celebs = [
	{
		name: "Beyonce Bowls",
		yearlyCumulativeSpend: "£44",
		purchaseToday: {
			item: "White mice",
			costPerItem: "£3",
			amountBought: 17
		}
	},
	{
		name: "Kray-Z",
		yearlyCumulativeSpend: "£28",
		purchaseToday: {
			item: "Flying saucers",
			costPerItem: "£2",
			amountBought: 28
		}
	},
	{
		name: "Matey Terry",
		yearlyCumulativeSpend: "£36",
		purchaseToday: {
			item: "Cola bottles",
			costPerItem: "£4",
			amountBought: 81
		}
	},
	{
		name: "Justine Klimberbake",
		yearlyCumulativeSpend: "£30",
		purchaseToday: {
			item: "Giant jelly snakes",
			costPerItem: "£103",
			amountBought: 2
		}
	}
];

calculateConfectioneryCosts(celebs);
/*
[
    {
        name: 'Beyonce Bowls',
        yearlyCumulativeSpend: £95
    },
    // ...etc
*/
```

---

### Reimplementation

Reimplement the following JavaScript array functions. Each function should take as arguments an array, have a look at the documentation for each function on MDN to see if they need more arguments. They should produce the same output and have the same effect on the input as the Javascript version. (And no, you can't just use the JavaScript version...)

#### map()

#### filter()

#### splice()

---

## Post-sprint

Look through the **post-sprint** section and have a go at answering the questions in `post-sprint/evaluation.md`. These tasks will serve as a good immediate way of assessing your understanding after the lecture and working on the main sprint.
