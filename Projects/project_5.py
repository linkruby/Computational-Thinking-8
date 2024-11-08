# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("alien good (1)")
player.set_size(0.5)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("space")




gameOver = False
lives = 5

# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("asteroid")
		object.set_size(0.9)
		object.goto(x_position, 250)
		object.set_y_speed(-8)
    
stage.event_interval(falling_object, 4)

# Section 3 - Collision

def collision(s1, s2):
	global lives, gameOver
	
	if s2.get_image_name() == "asteroid":
		stage.remove_sprite(s2)
		if lives == 0:
			gameOver = True
			stage.set_background("white")
			player.say("game over", 100)
		else:
			lives += -1
			player.say(f"you got hit! you have {lives} extra lives remaining",4)
player.event_collision(collision)


# Section 4 - Controls


def move_left(sprite):
	sprite.move_left(6)
    
def move_right(sprite):    
	sprite.move_right(6)


player.event_key("d", move_right)
player.event_key("a", move_left)