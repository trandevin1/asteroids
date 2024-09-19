import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.set_caption("Asteroids!")
    score_font = pygame.font.SysFont("monospace", 24, True)
    life_font = pygame.font.SysFont("monospace", 24, True)
    respawn_font = pygame.font.SysFont("comicsans", 72, True)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()

    score = 0
    paused = False

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and player.is_alive:
                    if paused:
                        paused = False
                    else:
                        paused = True

        player.invincibility -= dt

        if player.is_alive and not paused:

            for object in updatable:
                object.update(dt)

            for asteroid in asteroids:
                if asteroid.collision(player):
                    if player.health < 1:
                        player.is_alive = False
                    if player.invincibility <= 0:
                        player.decrease_health()
                        player.invincibility = PLAYER_INVINCIBILITY
                for shot in shots:
                    if shot.collision(asteroid):
                        asteroid.split()
                        shot.kill()
                        score += 10

            # background
            screen.fill("black")

            # then render after updates
            for object in drawable:
                object.draw(screen)

            scoretext = score_font.render(f"Score: {score}", 1, WHITE_FONT)
            screen.blit(scoretext, (0, 0))

            lifetext = life_font.render(f"Life: {player.health}", 1, WHITE_FONT)
            screen.blit(lifetext, (SCREEN_WIDTH - 100, 0))

            # refresh screen
            pygame.display.flip()

        elif not player.is_alive or paused:
            if not paused:
                respawn_text = respawn_font.render(f"TRY AGAIN?", 1, WHITE_FONT)
                screen.blit(
                    respawn_text, ((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGHT / 2) - 100)
                )
                continue_text = respawn_font.render(
                    f"Press Enter to Continue!", 1, WHITE_FONT
                )
                screen.blit(
                    continue_text, ((SCREEN_WIDTH / 2) - 300, SCREEN_HEIGHT / 2)
                )
                pygame.display.flip()
                if keys[pygame.K_RETURN]:
                    player.health = 3
                    player.is_alive = True
                    player.invincibility = 5
                    score -= 50
            else:
                respawn_text = respawn_font.render(f"PAUSED", 1, WHITE_FONT)
                screen.blit(
                    respawn_text, ((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGHT / 2) - 100)
                )
                continue_text = respawn_font.render(
                    f"Press ESCAPE to Continue!", 1, WHITE_FONT
                )
                screen.blit(
                    continue_text, ((SCREEN_WIDTH / 2) - 300, SCREEN_HEIGHT / 2)
                )
                pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
