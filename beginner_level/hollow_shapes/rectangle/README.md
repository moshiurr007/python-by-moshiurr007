## Hollow Rectangle

### Challenge

Print a hollow rectangle using `*` characters based on the given width and height, without using any modules or external libraries.

### Instructions

1. Create a function called `rectangle()` that takes two integer parameters: `width` and `height`.
2. Validate that `width` is between 5 and 50, and `height` is between 4 and 40.
3. Use a loop to generate each line of the rectangle.
4. The first and last lines should contain `width` number of `*` characters with spaces between them.
5. The middle lines should contain a `*` at the beginning and end, with spaces between them.
6. Return the completed rectangle as a string.

### Example

Input:<br>
`print(rectangle(5,4))`

Output:<br>

```
* * * * *
*       *
*       *
* * * * *
```
