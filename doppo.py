print("Enter the xyz-dimension of vector 1 separated by spaces: ")
vector1 = list(map(int, input().split())

print("Enter the xyz-dimension of vector 2 separated by spaces: ")
vector2 = list(map(int, input().split())

print("The dot product of vector 1 and vector 2 is ", vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2])
