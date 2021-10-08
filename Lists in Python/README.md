Consider a list (list = []). You can perform the following commands: <br>

insert i e: Insert integer  at position . <br>
print: Print the list. <br>
remove e: Delete the first occurrence of integer . <br>
append e: Insert integer  at the end of the list. <br>
sort: Sort the list. <br>
pop: Pop the last element from the list. <br>
reverse: Reverse the list. <br>
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.  <br>

Example <br>





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array. <br>
Output:
[1, 3, 2] <br>
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

 # Sample Input 0

12 <br>
insert 0 5 <br>
insert 1 10 <br>
insert 0 6 <br>
print <br>
remove 6 <br>
append 9 <br>
append 1 <br>
sort <br>
print <br>
pop <br>
reverse <br>
print <br>
# Sample Output 0

[6, 5, 10] <br>
[1, 5, 9, 10] <br>
[9, 5, 1] <br>
