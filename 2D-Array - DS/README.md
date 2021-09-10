Given a  2D Array, :

1 1 1 0 0 0 <br>
0 1 0 0 0 0 <br>
1 1 1 0 0 0 <br>
0 0 0 0 0 0 <br>
0 0 0 0 0 0 <br>
0 0 0 0 0 0 <br>
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c <br> 
  d <br>
e f g <br>
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1 <br> 
 0 -9  0  4 3 2 <br>
-9 -9 -9  1 2 3 <br>
 0  0  8  6 6 0 <br>
 0  0  0 -2 0 0 <br>
 0  0  1  2 4 0 <br>
The  hourglass sums are:

-63, -34, -9, 12, <br> 
-10,   0, 28, 23,  <br>
-27, -11, -2, 10,  <br>
  9,  17, 25, 18 <br>
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3 <br>
  1 <br>
8 6 6 <br>

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers
Returns

int: the maximum hourglass sum
Input Format

Each of the  lines of inputs  contains  space-separated integers .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0 <br>
0 1 0 0 0 0 <br>
1 1 1 0 0 0 <br>
0 0 2 4 4 0 <br>
0 0 0 2 0 0 <br>
0 0 1 2 4 0 <br>
Sample Output

19
Explanation

 contains the following hourglasses:

image

The hourglass with the maximum sum () is:

2 4 4 <br>
  2 <br>
1 2 4 <br>
