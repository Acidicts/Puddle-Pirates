import pygame
from timer import Timer

pygame.init()

WIDTH, HEIGHT = 800, 600

pygame.display.set_caption("Puddle Pirates")
win = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 30)

timer = Timer(1000)

ship = pygame.image.load("ship.png").convert_alpha()
ship = pygame.transform.scale(ship, (ship.get_width()//2, ship.get_height()//2))
ship.set_colorkey((0, 0, 0))
rect = ship.get_rect()
rect.center = (WIDTH//2, HEIGHT//2 - 100)
health = 5

cannon = pygame.image.load("cannon.png").convert_alpha()
cannon = pygame.transform.scale(cannon, (cannon.get_width()*4, cannon.get_height()*4))
cannon_rect = cannon.get_rect()
cannon_rect.bottom = HEIGHT

cannon_ball = pygame.surface.Surface((32, 32)).convert_alpha()
cannon_ball.fill((0, 0, 0))
cannon_ball.set_colorkey((0, 0, 0))
pygame.draw.circle(cannon_ball, (20, 20, 20), (16, 16), 16)
cannon_ball_rect = cannon_ball.get_rect()
cannon_ball_rect.bottomright = cannon_rect.topleft


def main():
    global cannon_ball_rect, health
    timer.activate()
    run = True
    fired = False
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((100, 100, 200))

        if timer.active:
            text = font.render("Sink the Evil Cole Pirate Ship", True, (255, 255, 255))
            win.blit(text, (10, 10))

        keys = pygame.key.get_pressed()
        direction = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        cannon_rect.x += direction

        if keys[pygame.K_SPACE]:
            cannon_ball_rect.center = cannon_rect.center
            fired = True

        if cannon_ball_rect.y < 0:
            fired = False

        if not fired:
            cannon_ball_rect.center = cannon_rect.center

        if cannon_ball_rect.colliderect(rect):
            health -= 1
            fired = False

        if fired:
            cannon_ball_rect.y -= 10

        win.blit(cannon_ball, cannon_ball_rect)
        win.blit(ship, rect)
        win.blit(cannon, cannon_rect)

        if health <= 0:
            text = font.render("You sunk the cole Pirates!", True, (0, 0, 0))
            text2 = font.render("You Win!", True, (0, 0, 0))
            win.fill('lightblue')
            win.blit(text2, (int(WIDTH/2 - text2.get_width()/2), 200))
            win.blit(text, (int(WIDTH/2 - text.get_width()/2), 100))

        pygame.display.update()
        timer.update()

    pygame.quit()


if __name__ == '__main__':
    main()
