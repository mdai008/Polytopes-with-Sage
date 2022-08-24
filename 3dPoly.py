# *********************************************************

#3x2xn cube with window size = 2x2x2, stride = (1,1,1), and n=2
#Let L be the layer number. Each layer is a 3x2 matrix. 

#layer 1:
#[1 2]
#[3 4]
#[5 6]

#layer 2:
#[7   8]
#[9  10]
#[11 12]

#window1:
#[1 2],[7  8]
#[3 4],[9 10]

#window2:
#[3 4],[9  10]
#[5 6],[11 12]

# *********************************************************

r = 12
windowSize = 8
window1 = [1,2,3,4,7,8,9,10]
window2 = [3,4,5,6,9,10,11,12]

windows = [window1, window2]
vertices = []

for w in windows:
    for v in w:
        x = [0] * r
        x[v - 1] = 1
        x = tuple(x)
        vertices.append(x)

v1 = vertices[:windowSize]
v2 = vertices[windowSize:windowSize * 2]

p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
pF = p1 + p2

print(len(pF.vertices()))

# *********************************************************

#3x2xn cube with window size = 2x2x2, stride = (1,1,1), and n=3
r = 18
windowSize = 8
window1 = [1,2,3,4,7,8,9,10]
window2 = [3,4,5,6,9,10,11,12]
window3 = [7,8,9,10,13,14,15,16]
window4 = [9,10,11,12,15,16,17,18]

windows = [window1, window2, window3, window4]
vertices = []

for w in windows:
    for v in w:
        x = [0] * r
        x[v - 1] = 1
        x = tuple(x)
        vertices.append(x)

v1 = vertices[:windowSize]
v2 = vertices[windowSize:windowSize * 2]
v3 = vertices[windowSize * 2:windowSize * 3]
v4 = vertices[windowSize * 3:windowSize * 4]


p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = Polyhedron(vertices = v3)
p4 = Polyhedron(vertices = v4)
pF = p1 + p2 + p3 + p4

print(len(pF.vertices()))

# *********************************************************

#3x2xn cube with window size = 2x2x2, stride = (1,1,1), and n=4
#computation will take a long time
r = 24
windowSize = 8
window1 = [1,2,3,4,7,8,9,10]
window2 = [3,4,5,6,9,10,11,12]
window3 = [7,8,9,10,13,14,15,16]
window4 = [9,10,11,12,15,16,17,18]
window5 = [13,14,15,16,19,20,21,22]
window6 = [15,16,17,18,21,22,23,24]

windows = [window1, window2, window3, window4, window5, window6]
vertices = []

for w in windows:
    for v in w:
        x = [0] * r
        x[v - 1] = 1
        x = tuple(x)
        vertices.append(x)

v1 = vertices[:windowSize]
v2 = vertices[windowSize:windowSize * 2]
v3 = vertices[windowSize * 2:windowSize * 3]
v4 = vertices[windowSize * 3:windowSize * 4]
v5 = vertices[windowSize * 4:windowSize * 5]
v6 = vertices[windowSize * 5:windowSize * 6]


p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = Polyhedron(vertices = v3)
p4 = Polyhedron(vertices = v4)
p5 = Polyhedron(vertices = v5)
p6 = Polyhedron(vertices = v6)
pF = p1 + p2 + p3 + p4 + p5 + p6

print(len(pF.vertices()))

# *********************************************************

