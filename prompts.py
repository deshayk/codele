'''
This module is a collection of prompts for the user. There are three types of prompts the
user will be able to choose from: easy, medium, and hard. The prompts are saved in an array
and will be generated randomly for the user.
'''

# Easy prompts

easy_prompts = ["Write a program that prints ‘Hello World’ to the screen.",
"Write a program that asks the user for their name and greets them with their name.",
"Write a program that asks the user for their age and accurately guess what year they were born.",
"Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.",
"Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.",
"Write a program that prints a multiplication table for numbers up to 12.",
"Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)",
"Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.",
"Write a program that prints the next 20 leap years.",
"Write a function that returns the largest element in a list.",
"Write function that reverses a list, preferably in place.",
"Write a function that checks whether an element occurs in a list.",
"Write a function that returns the elements on odd positions in a list.",
"Write a function that computes the running total of a list.",
"Write a function that tests whether a string is a palindrome.",
"Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion. (Subject to availability of these constructs in your language of choice.)",
"Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]",
"Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].",
"Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].",
"Write function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”."            
]

# Medium prompts
medium_prompts = ["Write a program that outputs all possibilities to put + or - or nothing between the numbers 1,2,…,9 (in this order) such that the result is 100. For example 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100.",
"Write a program that takes the duration of a year (in fractional days) for an imaginary planet as an input and produces a leap-year rule that minimizes the difference to the planet’s solar year.",                  
"Implement a data structure for graphs that allows modification (insertion, deletion). It should be possible to store values at edges and nodes. It might be easiest to use a dictionary of (node, edgelist) to do this.",
"Write a function that generates a DOT representation of a graph.",
"Write a program that automatically converts English text to Morse code and vice versa.",
"Write a program that finds the longest palindromic substring of a given string. Try to be as efficient as possible!",
"Think of a good interface for a list. What operations do you typically need? You might want to investigate the list interface in your language and in some other popular languages for inspiration.",                  
"Implement your list interface using a fixed chunk of memory, say an array of size 100. If the user wants to add more stuff to your list than fits in your memory you should produce some kind of error, for example you can throw an exception if your language supports that.",
"Implement a binary heap. Once using a list as the base data structure and once by implementing a pointer-linked binary tree. Use it for implementing heap-sort.",
"Implement an unbalanced binary search tree.",
"Implement a balanced binary search tree of your choice. I like (a,b)-trees best.",
]

# Hard prompts
hard_prompts = [
  
]