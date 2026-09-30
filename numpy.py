import numpy as np
# d = np.array([1,22,3,4,5,56])
# print(d)
# print(d.size)
# print(d.dtype)
# print(d.ndim)
a=np.array([1,2,25,3])
b=np.array([7,8,9,5])
print(a+b)
print(b-a)
print(a*b)
print(b/a)
print(b%a)
# 3. Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum and average.
a = np.array([12, 25, 7, 45, 18, 30, 9, 50, 22, 15])
print("\nQ3")
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
print("Average:", np.mean(a))


# 4. Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate even and odd numbers.
a = np.arange(1, 21)
print("\nQ4")
print("Even:", a[a % 2 == 0])
print("Odd:", a[a % 2 != 0])


# 5. Create a one-dimensional array containing numbers from 1 to 12 and reshape it.
a = np.arange(1, 13)
print("\nQ5")
print("2 x 6:\n", a.reshape(2, 6))
print("3 x 4:\n", a.reshape(3, 4))
print("4 x 3:\n", a.reshape(4, 3))


# 6. Create two 3 x 3 NumPy matrices and perform matrix addition.
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("\nQ6")
print("Matrix Addition:\n", a + b)


# 7. Create two compatible matrices and perform matrix multiplication.
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
print("\nQ7")
print("Matrix Multiplication:\n", np.matmul(a, b))


# 8. Create a 3 x 4 matrix and display its transpose.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\nQ8")
print("Transpose:\n", a.T)


# 9. Create a 4 x 4 NumPy array and display first row, last column, diagonal and second and third rows.
a = np.arange(1, 17).reshape(4, 4)
print("\nQ9")
print("First row:", a[0])
print("Last column:", a[:, -1])
print("Diagonal:", np.diag(a))
print("Second and third rows:\n", a[1:3])


# 10. Create a 4 x 4 matrix and calculate sum of each row and column.
a = np.arange(1, 17).reshape(4, 4)
print("\nQ10")
print("Row sums:", np.sum(a, axis=1))
print("Column sums:", np.sum(a, axis=0))


# 11. Create a NumPy array from 1 to 20 and display elements using slicing.
a = np.arange(1, 21)
print("\nQ11")
print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate:", a[::2])
print("Reverse:", a[::-1])


# 12. Create an array of 10 integers and replace elements greater than 50 with 0.
a = np.array([10, 65, 25, 80, 45, 90, 30, 55, 20, 75])
a[a > 50] = 0
print("\nQ12")
print("After replacement:", a)


# 13. Create an unsorted NumPy array and display ascending and descending order.
a = np.array([45, 12, 78, 3, 56, 21, 90, 8])
print("\nQ13")
print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])


# 14. Create an array containing duplicate values and display unique elements.
a = np.array([1, 2, 3, 2, 4, 5, 3, 6, 1, 5])
print("\nQ14")
print("Unique:", np.unique(a))


# 15. Create two NumPy arrays and concatenate horizontally and vertically.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("\nQ15")
print("Horizontal:\n", np.hstack((a, b)))
print("Vertical:\n", np.vstack((a, b)))


# 16. Store marks of 10 students and calculate highest, lowest, average, median and standard deviation.
m = np.array([78, 85, 67, 92, 74, 88, 69, 95, 81, 76])
print("\nQ16")
print("Highest:", np.max(m))
print("Lowest:", np.min(m))
print("Average:", np.mean(m))
print("Median:", np.median(m))
print("Standard deviation:", np.std(m))


# 17. Take marks of 20 students, calculate class average and display marks above average.
m = np.array([65, 78, 45, 89, 92, 56, 73, 81, 67, 95,
              88, 54, 76, 84, 69, 91, 58, 72, 86, 63])
avg = np.mean(m)
print("\nQ17")
print("Class average:", avg)
print("Above average:", m[m > avg])


# 18. Create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24.
a = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ18")
print("Array:\n", a)
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)


# 19. Create a 3D array and access specified elements.
a = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ19")
print("First element:", a[0, 0, 0])
print("Last element:", a[-1, -1, -1])
print("Element [0,1,2]:", a[0, 1, 2])
print("Element [1,2,3]:", a[1, 2, 3])


# 20. Create a (2, 3, 4) array and calculate different sums.
a = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ20")
print("Sum of all elements:", np.sum(a))
print("Sum of each layer:", np.sum(a, axis=(1, 2)))
print("Sum along rows:", np.sum(a, axis=2))
print("Sum along columns:", np.sum(a, axis=1))


# 21. Create a 3D array of random integers between 1 and 100 and replace values greater than 50 with 0.
a = np.random.randint(1, 101, (2, 3, 4))
print("\nQ21")
print("Original:\n", a)
a[a > 50] = 0
print("After replacement:\n", a)


# 22. Generate a random 3D array of shape (3, 4, 5) and calculate statistical values.
a = np.random.randint(1, 101, (3, 4, 5))
print("\nQ22")
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))


# 23. Create a 3D array of shape (2, 3, 4), flatten it and display both.
a = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ23")
print("Original:\n", a)
print("Flattened:", a.flatten())


# 24. Create a 3D array containing integers from 1 to 27, flatten it and calculate statistics.
a = np.arange(1, 28).reshape(3, 3, 3)
b = a.flatten()
print("\nQ24")
print("Flattened:", b)
print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))


# 25. Create a random 3D array of shape (3, 4, 5), flatten it and display selected elements.
a = np.random.randint(1, 101, (3, 4, 5))
b = a.flatten()
avg = np.mean(b)
print("\nQ25")
print("Greater than 50:", b[b > 50])
print("Even numbers:", b[b % 2 == 0])
print("Less than average:", b[b < avg])