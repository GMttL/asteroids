import pygame
import constants
from player import Player

def main():
	print("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")

	# setting up pygame
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()
	delta_time = 0

	# Player
	player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

	# Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(color="black")
		player.draw(screen)
		pygame.display.flip()
		delta_time = game_clock.tick(60) // 1000
		

if __name__ == "__main__":
	main()
