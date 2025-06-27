# main.py (com pausa por espaço após acerto)
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 1280, 720
FPS = 60
FONT = pygame.font.SysFont("Comic Sans MS", 48)
SMALL_FONT = pygame.font.SysFont("Comic Sans MS", 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
BLUE = (30, 144, 255)

OBJETOS = [
    ("Maçã", "imagens/maca.png"), 
    ("Bola", "imagens/bola.jpg"), 
    ("Cachorro", "imagens/cachorro.jpg"),
    ("Livro", "imagens/livro.jpg"),
    ("Banana", "imagens/banana.jpg"),
    ("Carro","imagens/carro.jpg")
    ]
imagens = {nome: pygame.image.load(caminho) for nome, caminho in OBJETOS}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Educativo Infantil")
clock = pygame.time.Clock()

mensagem = ""
cor_mensagem = GREEN
aguardando_proximo = False


def desenhar_imagem(nome_objeto, x, y):
    imagem = imagens[nome_objeto]
    imagem = pygame.transform.scale(imagem, (150, 150))  # Redimensiona para caber
    rect = imagem.get_rect(center=(x, y))
    screen.blit(imagem, rect)

def nova_rodada():
    alvo = random.choice(OBJETOS)
    opcoes = random.sample(OBJETOS, 3)
    if alvo not in opcoes:
        opcoes[random.randint(0, 2)] = alvo
    random.shuffle(opcoes)
    return alvo, opcoes

alvo, opcoes = nova_rodada()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if aguardando_proximo:
                if event.key == pygame.K_SPACE:
                    print("Próximo jogador iniciado")
                    alvo, opcoes = nova_rodada()
                    mensagem = ""
                    aguardando_proximo = False

            else:
                tecla = event.key
                index_tecla = {pygame.K_a: 0, pygame.K_s: 1, pygame.K_d: 2}.get(tecla, -1)
                if index_tecla != -1:
                    if opcoes[index_tecla][0] == alvo[0]:

                        mensagem = "Muito bem!"
                        cor_mensagem = GREEN
                        aguardando_proximo = True
                    else:
                        mensagem = "Tente novamente!"
                        cor_mensagem = RED

    titulo = FONT.render(f"Toque: {alvo[0]}", True, BLACK)
    screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 50))

    spacing = WIDTH // 4

    for i, (nome_objeto, _) in enumerate(opcoes):
        x = spacing * (i + 1)
        y = HEIGHT - 200
        desenhar_imagem(nome_objeto, x, y)


    if mensagem:
        label = FONT.render(mensagem, True, cor_mensagem)
        screen.blit(label, (WIDTH//2 - label.get_width()//2, HEIGHT//2 - 100))

    if aguardando_proximo:
        pausa = SMALL_FONT.render("Aguardando próximo colega... Pressione [ESPAÇO]", True, BLACK)
        screen.blit(pausa, (WIDTH//2 - pausa.get_width()//2, HEIGHT//2 + 10))

    pygame.display.flip()
    clock.tick(FPS)
