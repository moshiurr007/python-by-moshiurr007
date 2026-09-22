### python by moshiurr007 --> beginner_level ###

# hollow equilateral triangle #

def triangle(n):

    if n < 5 or n > 50:
        return "Try with any value between 5 and 50 for a better visual result."
    
    result = ""

    for i in range(1, n+1):
        leading_space = " "*(n-i)

        if i == 1: # first line
            result += leading_space + "*\n"
        elif i == n: # last line
            result += "* "*n + "\n"
        else: # any of the middle lines
            space_between = " "*( 2*i - 3 )
            result += leading_space + "*" + space_between + "*\n"

    return result

print(triangle(50))


""" Output :

         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
* * * * * * * * * * 

"""