print("Enter the xyz-dimension of vector 1 separated by spaces: ")
vector1 = list(map(int, input().split())

print("Enter the xyz-dimension of vector 2 separated by spaces: ")
vector2 = list(map(int, input().split())

int v_x = vector1[0]*vector2[0]
int v_y = vector1[1]*vector2[1]
int v_z = vector1[2]*vector2[2]

print("The dot product of vector 1 and vector 2 is ", v_x + v_y + v_z)
