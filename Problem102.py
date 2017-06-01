def containsOrigin(triangle):
    splitCoords = triangle.split(",")
    coords = [[int(splitCoords[0]),int(splitCoords[1])],[int(splitCoords[2]),int(splitCoords[3])],[int(splitCoords[4]),int(splitCoords[5])]]

    A = [coords[0][0],coords[0][1]]
    B = [coords[1][0],coords[1][1]]
    C = [coords[2][0],coords[2][1]]

    v0 = A
    v1 = [B[0] - A[0],B[1] - A[1]]
    v2 = [C[0] - A[0],C[1] - A[1]]

    a = -(v0[0]*v2[1]-v0[1]*v2[0])/(v1[0]*v2[1]-v1[1]*v2[0])
    b = (v0[0]*v1[1]-v0[1]*v1[0])/(v1[0]*v2[1]-v1[1]*v2[0])

    if a > 0 and b > 0 and a+b < 1:
        return True
    else:
        return False

def main():
    triangles = open("p102_triangles.txt",'r')
    total = 0
    for line in triangles:
        if line[-1:] == "\n":
            line = line[:-1]
        if(containsOrigin(line)):
            total+=1
    return total

print(main())