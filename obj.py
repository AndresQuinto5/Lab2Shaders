#Andres Emilio Quinto Villagran
#carne - 18288

#Determinamos la clase objeto
class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.faces = []
        self.normals = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                
                # Split vertices
                if prefix == 'v':
                    # vertice
                    self.vertices.append(
                        list(map(float, value.split(' ')))
                    )
                # Split normals
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                # Split faces
                elif prefix == 'f':
                    # Face
                    self.faces.append (
                        [ list(map(int , face.split('/'))) for face in value.split(' ') ]
                    )