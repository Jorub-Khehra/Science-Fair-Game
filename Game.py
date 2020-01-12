import pygame
import sys
import random
pygame.init()

WIDTH = 1000
HEIGHT = 800

RED = (255,0,0)
BACKGROUND_COLOUR = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

player_pos = [100, 100]
player_size = 50

enemy_size = 100
enemy_pos = [700, 600]

food_size = 25
food_pos = [random.randint(25,WIDTH), random.randint(25,HEIGHT)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

def detect_food_collision(player_pos, food_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	f_x = food_pos[0]
	f_y = food_pos[1]

	if (f_x >= p_x and f_x < (p_x + player_size)) or (p_x >= f_x and p_x < (f_x + food_size)):
		if (f_y >= p_y and f_y < (p_y+ player_size)) or (p_y >= f_y and p_y < (f_y + food_size)):
			return True
	return False

def detect_enemy_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y+ player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False

def move_towards_player_x():
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if player_pos[0] > enemy_pos[0]:
		enemy_pos[0] += 0.5
	elif enemy_pos[0] > player_pos[0]:
		enemy_pos[0] -= 0.5
	elif player_pos[1] > enemy_pos[1]:
		enemy_pos[1] += 0.5
	elif enemy_pos[1] > player_pos[1]:
		enemy_pos[1] -= 0.5


	

		


 

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
		
			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_UP and y > 0:
				y -= 50

			elif event.key == pygame.K_DOWN and y < 800 - 50:
				y += 50

			elif event.key == pygame.K_LEFT and x > 0: 
				x -= 50

			elif event.key == pygame.K_RIGHT and x < 1000 - 50: 
				x += 50




			player_pos = [x,y]

	screen.fill(BACKGROUND_COLOUR)

	if detect_enemy_collision(player_pos,enemy_pos):
		game_over = True
		print("Your Score Was:")
		print(str(score))
		score = 0

	if detect_food_collision(player_pos,food_pos):
		score += 1
		food_pos.clear()
		food_pos.append(random.randint(25,WIDTH))
		food_pos.append(random.randint(25,HEIGHT))



	move_towards_player_x()

	

	
		

			

    


	

	

	pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
	pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
	pygame.draw.rect(screen, GREEN, (food_pos[0], food_pos[1], food_size, food_size))
	pygame.display.update()
