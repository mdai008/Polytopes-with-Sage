from polyGenFunc import *

#write a function for any r and window size. stride = 1
# r = input("Enter input dimension: ").strip()
r = "7"
# windowSize = input("Enter window size: ").strip()
windowSize = "3"

windows = []
vertices1 = []
polys1 = []

vertices2 = []
polys2 = []

windGen(int(r), int(windowSize), windows)
vertGen(int(r), windows, vertices1)
polyGenSlow(int(r), int(windowSize), vertices1, polys1)


polyGenFast(int(r), int(windowSize), polys2, vertices2)

print(polys1 == polys2)
# print(vertices1 == vertices2)

