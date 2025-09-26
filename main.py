import pygame # type: ignore
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import*
from bullets import Shot


def main():
    pygame.init()
    
    #DISPLAYS / SURFACES
    screen = pygame.display.set_mode((SCREEN_WIDTH, (SCREEN_HEIGHT)))
    info_bar_surface = pygame.Surface((SCREEN_WIDTH, INFO_BAR_HEIGHT), pygame.SRCALPHA)

    #GENERAL VAR
    pygame.display.set_caption("Asteroids")
    info_bar_color = (60, 60, 60, 100)
    clock = pygame.time.Clock()
    dt = 0
    game_timer = 0

    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, bullets)
    
    #OBJECTS
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #ASSETS
    background_image = pygame.image.load("background.png")

    #GAME LOOP
    while True:
        game_timer += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                raise SystemExit("Game over!")
            
            for bullet in bullets:
                if bullet.collision_check(asteroid) == True:
                    bullet.kill()
                    asteroid.split() 

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(info_bar_surface, info_bar_color, (0, 0, SCREEN_WIDTH, INFO_BAR_HEIGHT))
        screen.blit(info_bar_surface, (0, 0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
