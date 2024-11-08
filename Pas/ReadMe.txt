These programs were written during my university studies for a course called "Algorithms and Algorithmization." They are implemented in the Pascal programming language.

Program (DimDan9.pas)

Description:  
This program reads a sequence of words (each with a maximum of 6 characters) and displays them in alphabetical order, along with the count of each word's occurrences.

Functionality:  
- Reading Words: The program sequentially reads words from input, ignoring spaces and commas. Each word is limited to 6 characters.  
- Validation: The program ensures that each word consists only of uppercase Latin letters and does not exceed 6 characters. If a word does not meet these conditions, the program outputs an error and stops.  
- Storing Words in a Binary Tree: Each word is added to a binary search tree. If the word already exists in the tree, its count is incremented.  
- Displaying Words: At the end, the program outputs all unique words in alphabetical order, along with their repetition counts.

Example Input:  
BCGHFD, DCT, JIBRB, BCGHFDM, DCT.

Example Output:  
Resulting Sequence:  
BCGHFD (2)  
DCT (2)  
JIBRB (1)

Program (integral.pas)

Description:  
This program performs numerical calculations to find the points of intersection of functions and the area of the curvilinear triangle formed by the intersections of three functions’ graphs. It also includes test calculations for roots and integrals.

Methods for Numerical Integration and Root Finding:  
- Root Finding using the Bisection Method:  
   The root function uses the bisection method to find the intersection point of two functions f and g on a given interval, with a precision defined by eps1.
   
- Trapezoidal Rule for Numerical Integration:  
   To calculate the area under the curve of function f over the interval [a, b], the integral function applies the trapezoidal rule. The method iteratively divides the interval into equal parts, sums the function values, and adjusts the integration step to achieve the specified precision eps2.

Modes of Operation:  
- Main Mode:  
   The program finds the points of intersection for three specified functions:  
   f1(x) = e^(-x) + 3  
   f2(x) = 2 * x - 2  
   f3(x) = 1 / x  
   These intersection points are then used to calculate the area of the curvilinear triangle formed by these functions, using the trapezoidal rule.

- Test Mode:  
   The user selects one of two operations: root finding or integral calculation. The program verifies that the input interval [a, b] has a valid range, where the start point is less than the end point.

Example Input and Output:  
Intersection Points: 2.384, 1.756, 0.567  
Area of the Curvilinear Triangle: 1.234
