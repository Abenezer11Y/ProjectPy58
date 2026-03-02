import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

LIME = (0, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Arial', 36)
text_surf = font.render('Hello there!', True, LIME)

rect_width, rect_height = 300, 100
main_rect = pygame.Rect(0, 0, rect_width, rect_height)
main_rect.center = screen.get_rect().center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, LIME, main_rect)
    screen.blit(text_surf, (0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
