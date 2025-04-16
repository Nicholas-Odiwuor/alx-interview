##Pascal's Triangle Generator
This Python script generates Pascal’s Triangle up to a specified number of rows (n). Pascal’s Triangle is a triangular array where each number is the sum of the two directly above it. The first row is [1], the second row is [1, 1], and each subsequent row starts and ends with 1.

Features
Generates Pascal’s Triangle for any positive integer n.

Returns an empty list if n <= 0.

Efficiently constructs each row using list operations and nested loops.

Prerequisites
Python 3.x
##Code Explanation
Edge Handling: Returns an empty list if n <= 0.

Initialization: Starts with the first row [1].

Row Construction:

Each new row begins and ends with 1.

Middle elements are sums of adjacent elements from the previous row.

Efficiency: Time complexity is O(n²) (optimal for this problem).
