import pygame
import sys

pygame.init()

vindu = pygame.display.set_mode((2000, 1080))
pygame.display.set_caption("level_1")

# Last inn bakgrunn og karakter
bg = pygame.image.load("BG.png")
P_M = pygame.image.load("Pink_Monster.png")

# Få dimensjonene til bakgrunn og vindu
bg_width, bg_height = bg.get_size()
vindu_width, vindu_height = vindu.get_size()

# Beregn startposisjon for sentrert bakgrunn
bg_x = (vindu_width - bg_width) // 2
bg_y = (vindu_height - bg_height) // 2

# Startposisjon for karakter
P_Mx, P_My = 50, 400

# Lage vindu
def oppdater_vindu(bg, Karakter, x, y):
    # Tegn bakgrunnen sentrert
    vindu.blit(bg, (bg_x, bg_y))
    # Tegn karakteren
    vindu.blit(Karakter, (x, y))
    pygame.display.update()

# Variabler for karakter bevegelse ved tastetrykk
P_M_Speed = 5

# Lager den "uendelige løkken" for events
Bevegelse = True
while Bevegelse:
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            Bevegelse = False
        if keys[pygame.K_RIGHT]:
            P_Mx += P_M_Speed
        if keys[pygame.K_LEFT]:
            P_Mx -= P_M_Speed
    oppdater_vindu(bg, P_M, P_Mx, P_My)

pygame.quit()
sys.exit()
