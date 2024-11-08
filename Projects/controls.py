# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("castle")
s1 = codesters.Sprite("knight",0,-200)
s1.set_size(0.3)
s2 = codesters.Sprite("dragon")



# Section 2: define controls
def move_up(sprite):
	sprite.move_up(1)
   	 
def move_down(sprite):
	sprite.move_down(1)
    
def move_left(sprite):
	sprite.move_left(1)
    
def move_right(sprite):    
	sprite.move_right(1)
	
def turn_left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1)
	
def turn_right(sprite):
	heading = sprite.heading
	sprite.set_heading(heading - 1)
	
def forward(sprite):
	sprite.forward(1)
	
def attack(sprite):
	sprite.attack()

# Section 3: define hide and show
def hide(sprite):
	sprite.hide()
def show(sprite):
	sprite.show()

s2 = hide
# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d" ,move_right)
s1.event_key("q", hide)
s1.event_key("g", show)
s1.event_key("c" , forward)
s1.event_key("x" , turn_left)
s1.event_key("z" , turn_right)
s1.event_key("r" , attack)
s2.event_key("w", move_up)
s2.event_key("s", move_down)
s2.event_key("a", move_left)
s2.event_key("d" ,move_right)
s2.event_key("m", hide)
s2.event_key("r", show)
s2.event_key("c" , forward)
s2.event_key("x" , turn_left)
s2.event_key("z" , turn_right)
# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")
