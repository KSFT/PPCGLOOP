# PPCGLOOP

This is an interpreter for a modified version of the programming language [LOOP](https://en.wikipedia.org/wiki/LOOP_%28programming_language%29) created for [a PPCG Stack Exchange challenge](http://codegolf.stackexchange.com/questions/69162/what-is-the-shortest-loop-program-that-outputs-2016). It currently has a very simple syntax, but I might expand it to allow more complicated I/O sometime. Programs may be of any of the following forms:

- `P;Q`, where P and Q are subprograms--Subprogram P is executed, then subprogram Q is executed.
- `x++` or `x--`, where x is a variable name--The value of the variable with name x is increased or decreased by 1, and the value of that variable is set to the result.
- `LOOP x DO P END` (spaces added for readability), where x a varable name, and P is a subprogram--Subprogram P is executed a number of times equal to the value of variable x at the beginning of the loop. If subprogram P changes the value of variable x, the number of iterations does not change.

Spaces and newlines may be inserted or removed at any point.

A variable name is the character `x` followed by one or more digits. If the value of variable that hasn't been assigned a value is used, 0 is used instead. At the end of the program, the value of `x0` is printed.
