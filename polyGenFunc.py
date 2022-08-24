def windGen(r, windowSize, windows):
    i = 0
    k = r - windowSize + 1
    while i < k:
        x = list(range(i+1,i+1+windowSize))
        windows.append(x)
        i += 1

def vertGen(r, windows, vertices):
    for w in windows:
        for v in w:
            x = [0] * r
            x[v - 1] = 1
            x = tuple(x)
            vertices.append(x)


def polyGenSlow(r, windowSize, vertices, polys):
    i = 0
    k = r - windowSize + 1
    while i < k:
        x = vertices[windowSize * i:windowSize * (i+1)]
        polys.append(x)
        i += 1


#combine windGen, vertGen, and polyGenSlow together
def polyGenFast(r, windowSize, polys, vertices):
    i = 0
    k = r - windowSize + 1
    
    while i < k:
        a = list(range(i+1,i+1+windowSize))
        for v in a:
            b = [0] * r
            b[v - 1] = 1
            b = tuple(b)
            vertices.append(b)
        
        # c = vertices[windowSize * i:windowSize * (i+1)]
        # polys.append(c)

        polys.append(vertices)
        vertices = []

        # d = Polyhedron(vertices = c)
        # polys.append(d)
        
        #polyF += d
        i += 1
    
    
        

    
    
        
        
        