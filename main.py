import pygame
import planet

pygame.init()
HEIGHT, WIDTH = 800, 800
WIN = pygame.display.set_mode((HEIGHT, WIDTH)); 
pygame.display.set_caption("Py-Planet")
FONT = pygame.font.SysFont("comicsans", 16)

def main():
    clock = pygame.time.Clock()
    running = True

    sun = planet.Planet(0, 0, 30, 1.98892 * 10**30, "yellow")
    sun.sun = True

    mercury = planet.Planet(-0.387 * planet.Planet.AU, 0, 14, 6.39 * 10**23, "orange")
    mercury.y_vel = 47.4*1000

    venus = planet.Planet(-0.723 * planet.Planet.AU, 0, 14, 4.8685 * 10**24, "white")
    venus.y_vel = 35.02 * 1000
    
    earth = planet.Planet(-1*planet.Planet.AU, 0, 16, 5.9742 * 10**24, "blue")
    earth.y_vel = 29.783 * 1000
    
    mars = planet.Planet(-1.524 * planet.Planet.AU, 0, 12, 6.39 * 10**23, "red")
    mars.y_vel = 24.077 * 1000 

    solar_bodies = [sun, mercury, venus, earth, mars]

    while running: 
        clock.tick(60)
        WIN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for planets in solar_bodies:
            planets.update_position(solar_bodies)
            planets.draw(WIDTH, HEIGHT, WIN, FONT)

        pygame.display.update()
    pygame.quit()

main()
