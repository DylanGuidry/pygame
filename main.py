import pygame
import os 

WIDTH, HEIGHT = 1021, 829
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Project")

BLUE = (78, 111, 219)
RED = (255, 0, 0)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 4
CHARACTER_WIDTH, CHARACTER_HEIGHT = 75, 75

FIREBALL_HIT = pygame.USEREVENT + 1

FIREBALL_GIRL_IMAGE = pygame.image.load(os.path.join("Assets", "fire_girl.png"))
FIREBALL_GIRL_IMAGE = pygame.transform.scale(FIREBALL_GIRL_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

BACKGROUND_IMPORT = pygame.image.load(os.path.join("Assets", "background.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMPORT, (1021, 829))

GHOST = pygame.image.load(os.path.join("Assets", "bad_guy1.png"))
GHOST = pygame.transform.scale(GHOST, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

def firegirl_movement(keys_pressed, fireballgirl):
        if keys_pressed[pygame.K_a]: #LEFT
            fireballgirl.x -= VEL
        if keys_pressed[pygame.K_d]: #RIGHT
            fireballgirl.x += VEL
        if keys_pressed[pygame.K_w]: #UP
            fireballgirl.y -= VEL
        if keys_pressed[pygame.K_s]: #DOWN
            fireballgirl.y += VEL

def ghost_movement(keys_pressed, ghost):
        if keys_pressed[pygame.K_j]: #LEFT
            ghost.x -= VEL
        if keys_pressed[pygame.K_l]: #RIGHT
            ghost.x += VEL
        if keys_pressed[pygame.K_i]: #UP
            ghost.y -= VEL
        if keys_pressed[pygame.K_k]: #DOWN
            ghost.y += VEL

def handle_bullets(firegirl_bullets, fireballgirl):
    for bullet in firegirl_bullets:
        bullet.x += BULLET_VEL
        if fireballgirl.colliderect(bullet):
            pygame.event.post(pygame.event.Event(FIREBALL_HIT))
            firegirl_bullets.remove(bullet)

def draw_window(fireballgirl, ghost, firegirl_bullets):
        WIN.fill(BLUE)
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(FIREBALL_GIRL_IMAGE, (fireballgirl.x, fireballgirl.y))
        WIN.blit(GHOST, (ghost.x, ghost.y))
        pygame.display.update()

        for bullet in firegirl_bullets:
            pygame.draw.rect(WIN, RED, bullet)

#Game loop:
def main():
    fireballgirl = pygame.Rect(275, 420, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    ghost = pygame.Rect(800, 310, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    firegirl_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(firegirl_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(fireballgirl.x + fireballgirl.width, fireballgirl.y + fireballgirl.height//2 - 2, 10, 5)
                firegirl_bullets.append(bullet)

        print(firegirl_bullets)
        keys_pressed = pygame.key.get_pressed()
        firegirl_movement(keys_pressed, fireballgirl)
        ghost_movement(keys_pressed, ghost)

        handle_bullets(firegirl_bullets, fireballgirl)
        draw_window(fireballgirl, ghost, firegirl_bullets)

    pygame.quit()

if __name__ == "__main__":
    main()