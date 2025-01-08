import pygame
import constants


def main():
	print("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")

	# setting up pygame
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

	while True:
		screen.fill(color="black")
		pygame.display.flip()

if __name__ == "__main__":
	main()
