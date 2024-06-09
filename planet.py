import pygame 
import math

class Planet: 
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, width, height, win, font):
        x = self.x * self.SCALE + width/2
        y = self.y * self.SCALE + height/2

        if len(self.orbit) > 2: 
            updated_points = []
            for point in self.orbit: 
                x, y = point
                x = x * self.SCALE + width / 2
                y = y * self.SCALE + height / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun: 
            distance_text = font.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, "white")
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
    
    def attraction(self, other): 
        other_x, other_y = other.x, other.y
        distance_x = other.x - self.x
        distance_y = other.y - self.y 
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        if other.sun: 
            self.distance_to_sun = distance
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, planets): 
        total_fx = total_fy = 0
        for body in planets: 
            if self == body: 
                continue
            fx, fy = self.attraction(body)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))