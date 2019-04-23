import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()


size = (900, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
background_image = pygame.image.load("saturn_family1.jpg").convert()
background_image_position = [0, 0]

player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

def musice():
    pygame.mixer.music.load('00560.mp3')
    pygame.mixer.music.play()

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            musice()
    screen.blit(background_image, background_image_position)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    pygame.mouse.set_visible(False)

    screen.blit(player_image, [x, y])

    pygame.display.flip()

    clock.tick(60)
pygame.quit()