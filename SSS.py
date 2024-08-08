import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 2000, 1600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Solar System Simulation')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SUN_COLOR = (255, 255, 0)
PLANET_COLORS = [
    (192, 192, 192),  # Mercury
    (255, 204, 0),    # Venus
    (0, 0, 255),      # Earth
    (255, 102, 0),    # Mars
    (255, 255, 0),    # Jupiter
    (0, 255, 255),    # Saturn
    (173, 216, 230),  # Uranus
    (0, 0, 139),      # Neptune
    (255, 192, 203)   # Pluto (dwarf planet)
]

# Define the Sun
sun_position = (width // 2, height // 2)
sun_radius = 50

# Define planets with realistic distances and speeds scaled down
planets = [
    {'color': PLANET_COLORS[0], 'distance': 50, 'radius': 4, 'angle': 0, 'speed': 0.1},  # Mercury
    {'color': PLANET_COLORS[1], 'distance': 75, 'radius': 6, 'angle': 0, 'speed': 0.085}, # Venus
    {'color': PLANET_COLORS[2], 'distance': 100, 'radius': 8, 'angle': 0, 'speed': 0.07},  # Earth
    {'color': PLANET_COLORS[3], 'distance': 130, 'radius': 6, 'angle': 0, 'speed': 0.05},  # Mars
    {'color': PLANET_COLORS[4], 'distance': 180, 'radius': 14, 'angle': 0, 'speed': 0.03}, # Jupiter
    {'color': PLANET_COLORS[5], 'distance': 230, 'radius': 12, 'angle': 0, 'speed': 0.02}, # Saturn
    {'color': PLANET_COLORS[6], 'distance': 280, 'radius': 10, 'angle': 0, 'speed': 0.015},# Uranus
    {'color': PLANET_COLORS[7], 'distance': 330, 'radius': 10, 'angle': 0, 'speed': 0.01}, # Neptune
    {'color': PLANET_COLORS[8], 'distance': 380, 'radius': 6, 'angle': 0, 'speed': 0.007}  # Pluto
]

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update planet positions
    for planet in planets:
        planet['angle'] += planet['speed']
        x = sun_position[0] + planet['distance'] * math.cos(planet['angle'])
        y = sun_position[1] + planet['distance'] * math.sin(planet['angle'])
        planet['position'] = (x, y)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the Sun
    pygame.draw.circle(screen, SUN_COLOR, sun_position, sun_radius)

    # Draw the planets
    for planet in planets:
        pygame.draw.circle(screen, planet['color'], (int(planet['position'][0]), int(planet['position'][1])), planet['radius'])

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)