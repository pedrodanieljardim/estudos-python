import pygame, random

# inicializa a pygame
pygame.init()

# define cores no formato RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# tamanho da janela
window_size = [800, 600]

# inicializa a janela
window = pygame.display.set_mode(window_size)

# seta um título para a janela
pygame.display.set_caption('Rocket Game')

# carrega uma imagem
img_rocket = pygame.image.load('rocket.png')

# posição da imagem
rocket_pos = [window_size[0], random.randint(0, window_size[1])]

speed = 1 # velocidade
score = 0 # pontuação do game

def score_text(score):
	font = pygame.font.Font(None, 30)
	text = font.render('Score: ' + str(score) + ' - Velocidade: ' + str(speed) + 'x', 1, BLACK)
	return text

def update_position(match = False):

	global rocket_pos, speed, score

	# atualiza a posição no eixo horizontal
	rocket_pos[0] -= speed

	# verifica se a imagem saiu dos limites da tela
	if (rocket_pos[0] + img_rocket.get_rect().size[0]) <= 0 or match:

		# atualiza as posições da imagem
		rocket_pos[0] = window_size[0]
		rocket_pos[1] = random.randint(img_rocket.get_rect().size[0],
										window_size[1] - img_rocket.get_rect().size[0])

		speed += 1 # incrementa a velocidade

		if speed > 20:
			speed = 1

		# verifica se não foi clique do mouse
		if not match:
			# diminui a pontuação
			if score > 0:
				score -= 1

done = True # flag para o loop principal da aplicação
rocket = None # serve para verificar colisão

# loop principal da aplicação
while done:

	# obtém os eventos da fila
	for event in pygame.event.get():
		# verifica o tipo do evento
		if event.type == pygame.QUIT: # evento para sair
			done = False # atualiza a flag para sair do loop
		if event.type == pygame.MOUSEBUTTONDOWN: # evento de clique do mouse
			# verifica se clicou na imagem
			if rocket.collidepoint(event.pos):
				score += 1 # incrementa o score
				update_position(True) # atualiza a posição
			else:
				# se errou o clique, diminui a pontuação
				if score > 0:
					score -= 1

	# preenche o fundo da janela com a cor branca
	window.fill(WHITE)

	# desenha a imagem
	rocket = window.blit(img_rocket, rocket_pos)

	# desenha o texto
	window.blit(score_text(score), (0, 0))

	# atualiza a tela
	pygame.display.update()

	# delay de 1/10 segundos
	pygame.time.delay(100)

	# atualiza a posição
	update_position()

pygame.quit()