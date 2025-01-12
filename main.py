import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")

	# setting up pygame
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()
	dt = 0

	# Groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# Player
	Player.containers = (updatable, drawable)
	player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

	# Asteroids
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	# Shots
	Shot.containers = (updatable, drawable)

	# Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for item in updatable:	
			item.update(dt)
			if item == player:
				player.timer -= dt
		
		for item in asteroids:
			if item.collision(player):
				print("Game Over!")
				return

		screen.fill(color="black")
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()

		# limit FPS to 60
		dt = game_clock.tick(60) / 1000
		

if __name__ == "__main__":
	main()
