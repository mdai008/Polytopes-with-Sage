# *********************************************************

points1 = [(0,0),(0,1),(1,0)]
points2 = [(0,0),(0,1),(1,0),(0.5,0.5)]
points3 = [(0,0),(0,1),(0.5,0.5)]
points4 = [(0,0),(0,1),(1,0),(0.5,0.5),(0.8,0.8)]

P1 = Polyhedron(points1)
P2 = Polyhedron(points2)
P3 = Polyhedron(points3)
P4 = Polyhedron(points4)

# P1.show()
# print(P1.vertices())
# P2.show()
# print(P2.vertices())
# P3.show()
# print(P3.vertices())
# P4.show()
# print(P4.vertices())

# *********************************************************

points1 = [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
points2 = [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0.8,0.8,0.8)]
points3 = [(0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(2,0,2,0)]
P1 = Polyhedron(points1)
P2 = Polyhedron(points2)
P3 = Polyhedron(points3)
# P1.show()
# P2.show()
# P3.show()

# *********************************************************

#x + y >= b, [-b,x,y]
h1 = [-1,1,1] #y >= -x + 1
h2 = [-1,-1,1] #y >= x + 1
h3 = [-1,1,-1] #y <= x - 1
h4 = [-1,-1,-1] #y <= -x - 1

P1 = Polyhedron(ieqs = [h1])
P2 = Polyhedron(ieqs = [h2])
P3 = Polyhedron(ieqs = [h3])
P4 = Polyhedron(ieqs = [h4])
P5 = Polyhedron(ieqs = [h1,h2])
P6 = Polyhedron(ieqs = [h1,h3])
P7 = Polyhedron(ieqs = [h1,h2,h3])

P1.show()
# P2.show()
# P3.show()
# P4.show()
# P5.show()
# P6.show()
# P7.show()

# *********************************************************

print(P1.Hrepresentation())

# *********************************************************

v1 = [(0,0),(0,1),(1,0)]
v2 = [(0,0),(0,1)]
v3 = [(0,0)]
v4 = [(1,2),(2,1)]
r1 = [(1,1)]
r2 = [(1,1),(2,5)]

p1 = Polyhedron(vertices = v1, rays = r1)
p2 = Polyhedron(vertices = v2, rays = r1)
p3 = Polyhedron(vertices = v3, rays = r1)
p4 = Polyhedron(vertices = v4, rays = r1)

p5 = Polyhedron(vertices = v1, rays = r2)
p6 = Polyhedron(vertices = v2, rays = r2)
p7 = Polyhedron(vertices = v3, rays = r2)
p8 = Polyhedron(vertices = v4, rays = r2)

# p1.show()
# p2.show()
# p3.show()
# p4.show()

# p5.show()
# p6.show()
# p7.show()
# p8.show()

# *********************************************************

print(p1.Vrepresentation())
print(p1.Hrepresentation())

# *********************************************************

fibPoints = [(1,1),(1,2),(2,3),(3,5),(5,8),(8,13),(13,21),(21,34),(34,55),(55,89),(89,144),(144,233),(233,377),(377,610)]
fibPoly = Polyhedron(vertices = fibPoints)
fibPoly.show()
print(fibPoly.Hrepresentation())
print(fibPoly.Vrepresentation())

# *********************************************************

v1 = [(0,0),(0,1),(1,0),(1,1)]
v2 = [(0,1.5),(1.5,0),(1.5,3),(3,1.5)]

p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = p1 + p2

# p1.show()
# p2.show()
# p3.show()

# *********************************************************

# cube()
# octahedron()
# dodecahedron()
# icosahedron()
# cube() + octahedron() + icosahedron()

# *********************************************************

#n=7, k=2, s=1
v1 = [(1,0,0,0,0,0,0),(0,1,0,0,0,0,0)]
v2 = [(0,1,0,0,0,0,0),(0,0,1,0,0,0,0)]
v3 = [(0,0,1,0,0,0,0),(0,0,0,1,0,0,0)]
v4 = [(0,0,0,1,0,0,0),(0,0,0,0,1,0,0)]
v5 = [(0,0,0,0,1,0,0),(0,0,0,0,0,1,0)]
v6 = [(0,0,0,0,0,1,0),(0,0,0,0,0,0,1)]

p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = Polyhedron(vertices = v3)
p4 = Polyhedron(vertices = v4)
p5 = Polyhedron(vertices = v5)
p6 = Polyhedron(vertices = v6)
p7 = p1 + p2 +p3 + p4 + p5 + p6

len(p7.vertices())

# *********************************************************

#n=7, k=3, s=1
v1 = [(1,0,0,0,0,0,0),(0,1,0,0,0,0,0),(0,0,1,0,0,0,0)]
v2 = [(0,1,0,0,0,0,0),(0,0,1,0,0,0,0),(0,0,0,1,0,0,0)]
v3 = [(0,0,1,0,0,0,0),(0,0,0,1,0,0,0),(0,0,0,0,1,0,0)]
v4 = [(0,0,0,1,0,0,0),(0,0,0,0,1,0,0),(0,0,0,0,0,1,0)]
v5 = [(0,0,0,0,1,0,0),(0,0,0,0,0,1,0),(0,0,0,0,0,0,1)]

p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = Polyhedron(vertices = v3)
p4 = Polyhedron(vertices = v4)
p5 = Polyhedron(vertices = v5)
p6 = p1 + p2 +p3 + p4 + p5

len(p6.vertices())

# *********************************************************

#n=7, k=3, s=2
v1 = [(1,0,0,0,0,0,0),(0,1,0,0,0,0,0),(0,0,1,0,0,0,0)]
v2 = [(0,0,1,0,0,0,0),(0,0,0,1,0,0,0),(0,0,0,0,1,0,0)]
v3 = [(0,0,0,0,1,0,0),(0,0,0,0,0,1,0),(0,0,0,0,0,0,1)]

p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = Polyhedron(vertices = v3)
p4 = p1 + p2 +p3

len(p4.vertices())

# *********************************************************

#n=4, k=3, s=1
v1 = [(1,0,0,0),(0,1,0,0),(0,0,1,0)]
v2 = [(0,1,0,0),(0,0,1,0),(0,0,0,1)]

p1 = Polyhedron(vertices = v1)
p2 = Polyhedron(vertices = v2)
p3 = p1 + p2

(0,1,1,0) in p3.vertices()

# *********************************************************
