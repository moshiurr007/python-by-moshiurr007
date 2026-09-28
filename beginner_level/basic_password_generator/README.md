## Basic Password Generator

### Challenge

Create a basic password generator that creates a password from the user's desired password length. Use Python's built-in `random` module.

### Instructions

1. Import the `random` module.
2. Create a function called `generate_password()` that takes no arguments.
3. Inside the function, create separate strings for lowercase letters, uppercase letters, numbers, and special characters. Combine them into one string called `all_characters`.
4. Ask the user to enter the password length and convert it to an integer.
5. Validate that the password length is between `8` and `30`. Otherwise, raise a `ValueError` with a helpful message.
6. Create an empty string to store the password.
7. Use a loop to randomly select characters from `all_characters` and add them to the password until it reaches the required length.
8. Return the completed password as a string.

### Example

Input:<br>
`print(generate_password())`<br>

Output:<br>

```
Enter password length: 12
I:**,}XDAK$r
```
