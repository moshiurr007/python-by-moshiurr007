## Hollow Equilateral Triangle

### Challenge

Print a hollow equilateral triangle using `*` characters without using any modules or external libraries.<br>
The input value represents the number of `*` characters on each side of the triangle.

### Instructions

1. Create a function called `triangle()` that takes an integer as an argument.
2. Validate that the input is between `5` and `50`.
3. Use a loop to generate each line of the triangle.
4. Add leading spaces to center the triangle.
5. The first line should contain one `*`.
6. For the middle lines, place two `*` characters with spaces between them.
7. The last line should contain `n` number of `*` characters, with one space between each `*`.
8. Return the completed triangle as a string.

### Example

Input:<br>
`print(triangle(7))`

Output:<br>

```
      *
     * *
    *   *
   *     *
  *       *
 *         *
* * * * * * *
```
