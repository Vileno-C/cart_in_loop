import pygame
import numpy as np

# Inicializar o PyGame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle do Carrinho")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Física do Carrinho
g = 9.81  # Gravidade
mass = 1.0  # Massa do carrinho
initial_height = 0  # Altura inicial (ajustável em pixels)
energy_loss = 0.99  # Coeficiente para simular perda de energia

# Posição do loop
loop_center = (WIDTH * 2 / 3, HEIGHT - 150)
loop_radius = 100

# Variáveis do carrinho
def reset_cart():
    return {
        "x": 100,
        "y": HEIGHT - initial_height,
        "radius": 20,
        "on_loop": False,
        "is_angle_0": True,
        "is_loop_0": True,
        "speed": 0,
        "current_height": initial_height
    }

cart = reset_cart()
paused = False
finished = False

# Função para calcular velocidade com energia
def calculate_velocity(h_initial, h_current, speed):
    energy_total = mass * g * h_initial + 0.5 * mass * speed**2
    h_current_energy = energy_total / (mass * g)
    h_current_energy = max(h_current_energy, h_current)  # Não ultrapassa o limite
    return np.sqrt(2 * g * (h_current_energy - h_current))

# Função para desenhar a tela de seleção de velocidade
def draw_speed_selection():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 36)
    text = font.render("Escolha a altura inicial do carrinho:", True, BLACK)
    screen.blit(text, (WIDTH // 3, HEIGHT // 3))
    options = ["1: Baixa (150 px)", "2: Média (300 px)", "3: Alta (450 px)"]
    for i, option in enumerate(options):
        text = font.render(option, True, BLACK)
        screen.blit(text, (WIDTH // 3, HEIGHT // 3 + 50 + i * 40))
    text = font.render("Pressione Enter para começar", True, RED)
    screen.blit(text, (WIDTH // 3, HEIGHT // 2 + 100))

# Função para atualizar o movimento do carrinho
def update_cart():
    global finished
    if not cart["on_loop"]:
        cart["speed"] = calculate_velocity(initial_height, cart["current_height"], cart["speed"])
        cart["x"] += cart["speed"]
        cart["y"] = HEIGHT - 50

        if abs(cart["x"] - loop_center[0]) < 10 and cart["is_loop_0"]:
            cart["on_loop"] = True
            cart["is_loop_0"] = False

        if cart["x"] > WIDTH - 50:
            finished = True
    else:
        angle = np.arccos((cart["x"] - loop_center[0]) / loop_radius)
        if cart["y"] > loop_center[1]:
            angle = 2 * np.pi - angle
            if cart["is_angle_0"]:
                cart["angle_0"] = angle
                cart["is_angle_0"] = False

        cart["speed"] = calculate_velocity(initial_height, cart["current_height"], cart["speed"]) * energy_loss
        angle += cart["speed"] / loop_radius
        cart["x"] = loop_center[0] + loop_radius * np.cos(angle)
        cart["y"] = loop_center[1] - loop_radius * np.sin(angle)

        if abs(angle - cart["angle_0"]) < 0.02:
            cart["on_loop"] = False

# Função para desenhar o carrinho e a pista
def draw_simulation():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (5, HEIGHT - 50), (WIDTH - 5, HEIGHT - 50), 3)
    pygame.draw.circle(screen, BLACK, loop_center, loop_radius, 3)
    pygame.draw.circle(screen, RED, (int(cart["x"]), int(cart["y"])), cart["radius"])

    font = pygame.font.SysFont(None, 24)
    kinetic_energy = 0.5 * mass * cart["speed"]**2
    potential_energy = mass * g * (HEIGHT - cart["y"])
    total_energy = kinetic_energy + potential_energy

    texts = [
        f"Velocidade: {cart['speed']:.2f} m/s",
        f"Energia Cinética: {kinetic_energy:.0f} J",
        f"Energia Potencial: {potential_energy:.0f} J",
        f"Energia Total: {total_energy:.0f} J"
    ]
    for i, line in enumerate(texts):
        text = font.render(line, True, BLUE)
        screen.blit(text, (10, 10 + i * 30))

# Função para exibir mensagens de pausa ou término
def draw_pause_or_finish():
    if paused or finished:
        font = pygame.font.SysFont(None, 48 if paused else 36)
        text = font.render("PAUSADO" if paused else "Simulação Finalizada!", True, RED if paused else BLACK)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        text = font.render("Pressione S para voltar ao início.", True, RED)
        screen.blit(text, (WIDTH // 3, HEIGHT // 3 + 50))


# Loop do jogo
running = True
selecting_speed = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_p:
                paused = not paused
            elif selecting_speed and event.key == pygame.K_RETURN and cart["speed"] > 0:
                selecting_speed = False
            elif (finished or paused) and event.key == pygame.K_s:
                cart = reset_cart()
                selecting_speed = True
                finished = False

            if selecting_speed:
                if event.key == pygame.K_1:
                    cart["speed"] = 3
                elif event.key == pygame.K_2:
                    cart["speed"] = 10
                elif event.key == pygame.K_3:
                    cart["speed"] = 15

    if selecting_speed:
        paused = False
        finished = False
        draw_speed_selection()
    elif not paused and not finished:
        update_cart()
        draw_simulation()

    draw_pause_or_finish()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
