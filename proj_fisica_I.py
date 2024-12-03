import pygame
import numpy as np

# Inicializar o PyGame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle do Carrinho")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Física do Carrinho
g = 9.81  # Gravidade
mass = 1.0  # Massa do carrinho
friction = 0.02  # Atrito na pista
initial_height = 200  # Altura inicial (ajustável em pixels)
energy_loss = 0.99  # Coeficiente para simular perda de energia

# Posição do loop
loop_center = (WIDTH * 2/3, HEIGHT - 150)
loop_radius = 100

# Variáveis do carrinho
cart_x = 100
cart_y = HEIGHT - initial_height
cart_radius = 20
on_loop = False  # Indica se o carrinho está no loop
is_angle_0 = True  # Para indicar o ângulo inicial no loop
is_loop_0 = True # Para indicar o primeiro loop
speed = 3  # Velocidade do carrinho [15, 10, 3]
current_height = initial_height  # Altura atual

# Função para calcular velocidade com energia
def calculate_velocity(h_initial, h_current, speed):
    # Energia potencial inicial -> Energia cinética atual com perda
    energy_total = mass * g * h_initial + 0.5 * mass * speed**2
    h_current_energy = energy_total / (mass * g)
    if h_current_energy < h_current:
        h_current_energy = h_current  # Não ultrapassa o limite
    v = np.sqrt(2 * g * (h_current_energy - h_current))
    return v

# Loop do jogo
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar o movimento do carrinho
    if not on_loop:
        # Movimento na pista reta
        speed = calculate_velocity(initial_height, current_height, speed)
        cart_x += speed  # Velocidade baseada na energia
        cart_y = HEIGHT - 50  # Posição fixa na reta
        
        #print("cart_x:", cart_x)
        #print("loop_c:", loop_center[0])
        # Detectar entrada no loop
        if (abs(cart_x - loop_center[0]) < 10) and is_loop_0:
            on_loop = True
            is_loop_0 = False

    else:
        # Movimento no loop circular
        angle = np.arccos((cart_x - loop_center[0]) / loop_radius)
        if cart_y > loop_center[1]:  # Ajustar o ângulo para a parte inferior
            angle = 2 * np.pi - angle
            if is_angle_0:
                angle_0 = angle
                is_angle_0 = False

        # Atualizar posição com base na velocidade angular
        speed = calculate_velocity(initial_height, current_height, speed) * energy_loss
        angle += speed / loop_radius  # Velocidade angular proporcional
        cart_x = loop_center[0] + loop_radius * np.cos(angle)
        cart_y = loop_center[1] - loop_radius * np.sin(angle)

        # Sair do loop
        if abs(angle - angle_0) < 0.02:
            #print("entrou2")
            on_loop = False

    # Desenhar a pista
    pygame.draw.line(screen, BLACK, (100, HEIGHT - 50), (WIDTH - 100, HEIGHT - 50), 3)  # Linha reta
    pygame.draw.circle(screen, BLACK, loop_center, loop_radius, 3)  # Loop

    # Desenhar o carrinho
    pygame.draw.circle(screen, RED, (int(cart_x), int(cart_y)), cart_radius)

    # Mostrar informações de energia
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Velocidade: {speed:.2f} m/s", True, GREEN)
    screen.blit(text, (10, 10))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()