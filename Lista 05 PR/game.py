# Configurações primordiais:
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Python")
large = 1280
height = 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode((large, height))

# Cores em RGB:
black = 0, 0 ,0
white = 255, 255, 255
green = 0, 255, 0
blue = 0, 0, 255

# Parâmetros da cobra:
square_size = 20
speed_game = 10

# Geração de comida:
def generate_food():
    food_x = round(random.randrange(0, large - square_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - square_size) / 20.0) * 20.0
    return food_x, food_y

# Função do desenho da Comida:
def draw_food(sized,food_x, food_y ):
    pygame.draw.rect(screen, green, [food_x, food_y, sized, sized])

# Função do Art Attack da Cobra:
def art_snake(sized, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], sized, sized])

# Função Art Attack do Score:
def art_score(score):
    source = pygame.font.SysFont("Segoe UI Black", 30)
    text = source.render(f"Pontos: {score}", True, blue)
    screen.blit(text, [0, 0])
    
def selection_speed(glitt):
    if glitt == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    elif glitt == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
    elif glitt == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
    elif glitt == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0
        
    return speed_x, speed_y
    
# Infinite Loop:
def play_game():
    end_game = False
    
    x = large / 2
    y = height / 2
    speed_x = 0
    speed_y = 0
    
    size_snake = 1
    pixels = []
    
    food_x, food_y = generate_food()  
    
    while not end_game:
        screen.fill(black)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end_game = True
            elif evento.type == pygame.KEYDOWN:
                speed_x, speed_y = selection_speed(evento.key)
                
        # Desenho da comida:       
        draw_food(square_size, food_x, food_y,)
        
        # Andamento da Cobra:
        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]

        art_snake(square_size, pixels)

        # Verifica se bateu no próprio corpo:
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True
                print("Fim de Jogo!")
        
        # Art Attack do Score
        art_score(size_snake -1)
        
        # Verifica se bateu na parede:
        if x < 0 or x>= large or y < 0 or y >= height:
            end_game = True
            print("Fim de jogo!")

        x += speed_x
        y += speed_y

        # Ganhando o jogo:
        if size_snake == 31:
            end_game = True
            print("Parabéns! Você ganhou!")
        
        # Atualização da comida:
        if x == food_x and y == food_y:
            size_snake += 1
            food_x, food_y = generate_food()

        # Atualização da tela:
        pygame.display.update()
        clock.tick(speed_game)

play_game()