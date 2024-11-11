# Markdown
## Heading 2
### Heading 3

**Example of Bold text**
*Example of Italic text*
~~This text was mistaken~~
**Example of Bold and _Nested Italic Text_ hehe**
H <sub> 2 </sub> O
x <sup> 2 </sup>
fill in the <ins>blanks</ins>


### Mathematical Expression
**The mathematical expression for vector dot product**
$$\bar{a}.\bar{b} = \sum_{k=1}^n a_k b_k$$

## Implementation of vector dot-product in Python
We had implemented vector dot-product using 2 different algorithms. 

### Algorithm1[^1]
```python
v1 = list(map(int, input().split())
v2 = list(map(int, input().split())
print("the dot product is ", v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])
```
>This text is qouted

### Algorithm2[^2]
```python
import numpy as np

# Creating two numpy One-Dimensional array using the array() method
arr1 = np.array([2+3j,5+6j])
arr2 = np.array([9+10j,11+12j])
# Display the arrays
print("Array1...\n",arr1)
print("\nArray2...\n",arr2)
# Check the Dimensions of both the arrays
print("\nDimensions of Array1...\n",arr1.ndim)
print("\nDimensions of Array2...\n",arr2.ndim)
# Check the Shape of both the arrays
print("\nShape of Array1...\n",arr1.shape)
print("\nShape of Array2...\n",arr2.shape)
# To return the dot product of two vectors, use the numpy.vdot() method in Python.
print("\nResult...\n",np.vdot(arr1, arr2))
```

The code is avaliable on [GitHub Pages](https://github.com/dev99p/first-repo).


### Vector Dot product Image
![This an Image depicting vector dot product](https://www.shutterstock.com/image-vector/dot-product-two-vectors-mathematics-260nw-2314658537.jpg)

### Unordered list
- hi
- hello
- hey

### Ordered list
1. hi
2. hello
3. hey

### List of Task
- [x] Create a “README.md” file for your GitHub repository describing your implementation
of the vector dot-product code. 
- [] Include its mathematical expression.
- [] an example code snippet
- [] a diagram (picture)
- [] a table showing the comparison among various versions of your algorithm. 
- [] Showcase all Markdown elements that you learnt in this assignment.
- [] Add and commit this file to your repository and push it to GitHub. 
- [] Attach the screenshot of this markdown file as rendered on GitHub.

[^1]: Algorithm1.
[^2]: Algorithm2.

### Table comparing Alorithm
| Property         | Algorithm 1       | Algorithm2     |
| ---------------- | ----------------- | -------------- |
| Time Complexity  | O(1)              | O(n)           |
| Memory Complexity| O(1)              | O(1)           |

> [!NOTE]
> An alert was successfully added






