###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("fall")

s1 = codesters.Square ( -100, 100, 200, "red")
s2 = codesters.Square ( -100, -100, 200, "yellow")
s3 = codesters.Square ( 100, -100, 200, "green")
s4 = codesters.Square ( 100, 100, 200, "blue")

s5 = codesters.Sprite ("kitten", 100,100)
s5.set_size (1)
s6 = codesters.Sprite ("tiger",100,-100)
s6.set_size (0.1)
s7 = codesters.Sprite ("fish",-100,100)
s7.set_size(0.2)
s8 = codesters.Sprite ("flower",-100,-100)
