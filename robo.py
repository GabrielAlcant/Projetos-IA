# Importe as bibliotecas Pygame e NumPy
import pygame
import numpy as np

# Defina as constantes para o tamanho da tela, tamanho da célula, cor de fundo, quadros por segundo e número de quartos
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL_SIZE = 40
BG_COLOR = (255, 255, 255)
FPS = 60
NUM_ROOMS = 6

# Defina uma classe Room com um método de inicialização que define as coordenadas, status sujo e cor do quarto. Ele também possui um método de desenho para desenhar o quarto na tela.
class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirty = np.random.choice([True, False])  # Define aleatoriamente se o quarto está sujo ou não
        self.color = (255, 255, 255) if self.dirty else (200, 200, 200)  # Define a cor do quarto com base no estado de sujeira

    def draw(self, screen):
        rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)  # Cria um retângulo para representar o quarto
        pygame.draw.rect(screen, self.color, rect)  # Desenha o retângulo na tela com a cor apropriada

# Defina uma classe Robot com um método de inicialização que define as coordenadas, raio e cor do robô. Ele também possui um método de desenho para desenhar o robô na tela e os métodos sense e clean para detectar e limpar quartos sujos.
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = CELL_SIZE // 2  # Define o raio do robô com base no tamanho da célula
        self.color = (255, 0, 0)  # Define a cor do robô como vermelho
        self.cleaned_rooms = 0  # Contador para quartos limpos pelo robô

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x * CELL_SIZE + self.radius, self.y * CELL_SIZE + self.radius), self.radius)  # Desenha o robô como um círculo na tela

    def sense(self, rooms):
        return rooms[self.x][self.y].dirty  # Retorna o estado de sujeira do quarto atual em que o robô está

    def clean(self, rooms):
        rooms[self.x][self.y].dirty = False  # Marca o quarto atual como limpo
        rooms[self.x][self.y].color = (200, 200, 200)  # Atualiza a cor do quarto para refletir seu estado limpo
        self.cleaned_rooms += 1  # Incrementa o contador de quartos limpos

# Defina uma função para gerar uma lista de quartos com base na constante NUM_ROOMS. Ele cria uma instância Room para cada célula da grade e os adiciona a cada linha antes de adicionar a linha à lista final.
def generate_rooms():
    rooms = []
    for i in range(NUM_ROOMS):
        row = []
        for j in range(NUM_ROOMS):
            room = Room(i, j)  # Cria uma instância de Room com as coordenadas atuais
            row.append(room)  # Adiciona o quarto à linha atual
        rooms.append(row)  # Adiciona a linha à lista de quartos
    return rooms

# Defina uma função de desenho que preenche a tela com a cor de fundo, chama o método de desenho para cada quarto e chama o método de desenho para o robô.
def draw(screen, rooms, robot):
    screen.fill(BG_COLOR)  # Preenche a tela com a cor de fundo
    for row in rooms:
        for room in row:
            room.draw(screen)  # Desenha cada quarto na tela
    robot.draw(screen)  # Desenha o robô na tela
    pygame.display.update()  # Atualiza a tela para mostrar as mudanças

# Defina uma função de busca em profundidade que receba a lista de quartos e a instância do robô. Ela inicializa um conjunto vazio para os quartos visitados e uma lista para manter o registro do caminho do robô. Em seguida, retira as coordenadas do final do caminho e as adiciona ao conjunto de quartos visitados. Define as coordenadas do robô para a coordenada retirada e verifica se o quarto está sujo. Se estiver, o robô o limpa. Em seguida, obtém os quartos vizinhos e os adiciona à pilha se ainda não tiverem sido visitados. A função também chama a função "draw" para atualizar a tela a cada novo movimento.
def depth_first_search(rooms, robot):
    visited = set()  # Conjunto de quartos visitados
    stack = [(robot.x, robot.y)]  # Pilha para rastrear o caminho do robô

    while stack:
        x, y = stack.pop()  # Remove as coordenadas do final do caminho
        visited.add((x, y))  # Adiciona as coordenadas aos quartos visitados

        robot.x = x  # Define as coordenadas do robô para a coordenada retirada
        robot.y = y

        if robot.sense(rooms):  # Verifica se o quarto atual está sujo
            robot.clean(rooms)  # Limpa o quarto, se estiver sujo

        neighbors = get_neighbors(x, y, rooms)  # Obtém os quartos vizinhos
        for neighbor in neighbors:
            if neighbor not in visited:  # Adiciona vizinhos não visitados à pilha
                stack.append(neighbor)
        
        draw(screen, rooms, robot)  # Atualiza a tela para mostrar o movimento do robô
        pygame.time.delay(200)  # Pausa para uma melhor visualização dos movimentos

    robot.color = (0, 255, 0)  # Define a cor do robô para verde após a conclusão
    draw(screen, rooms, robot)
    pygame.time.delay(1000)

# Defina uma função para obter os quartos vizinhos de uma coordenada dada. Ele verifica se o quarto vizinho está dentro dos limites da grade e retorna uma lista de coordenadas vizinhas válidas.
def get_neighbors(x, y, rooms):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < NUM_ROOMS - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < NUM_ROOMS - 1:
        neighbors.append((x, y + 1))
    return neighbors

# Define a função principal que cria a lista de quartos e a instância do robô. Em seguida, ela chama a função de busca em profundidade com essas entradas.
def main():
    rooms = generate_rooms()  # Gera a lista de quartos
    robot = Robot(np.random.randint(NUM_ROOMS), np.random.randint(NUM_ROOMS))  # Cria uma instância de Robot com coordenadas aleatórias
    depth_first_search(rooms, robot)  # Executa a busca em profundidade

# Inicialize o Pygame e defina o tamanho da tela e a legenda. Em seguida, chame a função principal e encerre o Pygame.
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Robô Aspirador')
    clock = pygame.time.Clock()

    main()

    pygame.quit()
