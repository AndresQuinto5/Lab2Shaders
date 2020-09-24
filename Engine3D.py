#Andrés Emilio Quinto Villagrán - 18288
#Lab 2 shaders

from gl import Render
#from gl import color

render = Render()
PLANET = "PLANET"

render.load("sphere.obj", translate=(400, 400, 0), scale=(250, 250, 350), shape=PLANET)
render.glFinish(filename="output.bmp")