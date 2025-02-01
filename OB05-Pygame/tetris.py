import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 600  # Увеличили ширину для отображения следующей фигуры
BLOCK_SIZE = 30
GRID_WIDTH = 10  # Ширина игрового поля
GRID_HEIGHT = 20  # Высота игрового поля
SIDE_PANEL_WIDTH = 100  # Ширина боковой панели для следующей фигуры

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (0, 255, 255),  # Циан
    (255, 255, 0),  # Желтый
    (255, 165, 0),  # Оранжевый
    (0, 0, 255),    # Синий
    (0, 255, 0),    # Зеленый
    (128, 0, 128),  # Фиолетовый
    (255, 0, 0)     # Красный
]

# Фигуры и их повороты
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тетрис")

# Часы
clock = pygame.time.Clock()

# Класс для фигур
class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# Функция для создания сетки
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

# Функция для отрисовки сетки
def draw_grid(surface, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for y in range(GRID_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, y * BLOCK_SIZE), (GRID_WIDTH * BLOCK_SIZE, y * BLOCK_SIZE))
    for x in range(GRID_WIDTH):
        pygame.draw.line(surface, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT))

# Функция для отрисовки фигуры
def draw_piece(surface, piece, offset_x=0, offset_y=0):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface,
                    piece.color,
                    ((piece.x + x + offset_x) * BLOCK_SIZE, (piece.y + y + offset_y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )

# Функция для отрисовки следующей фигуры
def draw_next_piece(surface, piece):
    font = pygame.font.SysFont("comicsans", 20)
    label = font.render("Next Piece:", 1, WHITE)
    surface.blit(label, (GRID_WIDTH * BLOCK_SIZE + 10, 10))

    # Отрисовка следующей фигуры
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface,
                    piece.color,
                    (GRID_WIDTH * BLOCK_SIZE + 50 + x * BLOCK_SIZE, 50 + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )

# Функция для проверки столкновений
def valid_space(piece, grid):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                if piece.y + y >= GRID_HEIGHT or piece.x + x < 0 or piece.x + x >= GRID_WIDTH:
                    return False
                if grid[piece.y + y][piece.x + x] != BLACK:
                    return False
    return True

# Функция для очистки заполненных линий
def clear_rows(grid, locked_positions):
    cleared_rows = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if BLACK not in grid[y]:
            cleared_rows += 1
            del grid[y]
            grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
            for x in range(GRID_WIDTH):
                if (x, y) in locked_positions:
                    del locked_positions[(x, y)]
    return cleared_rows

# Основная функция игры
def main():
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_piece = Piece(random.choice(SHAPES))
    next_piece = Piece(random.choice(SHAPES))
    fall_time = 0
    fall_speed = 0.3
    score = 0

    running = True
    while running:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # Автоматическое падение фигуры
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                for y, row in enumerate(current_piece.shape):
                    for x, cell in enumerate(row):
                        if cell:
                            locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                current_piece = next_piece
                next_piece = Piece(random.choice(SHAPES))
                if not valid_space(current_piece, grid):
                    running = False

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece, grid):
                        for _ in range(3):
                            current_piece.rotate()

        # Отрисовка
        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_piece(screen, current_piece)
        draw_next_piece(screen, next_piece)
        pygame.display.update()

        # Очистка линий и обновление счета
        cleared_rows = clear_rows(grid, locked_positions)
        if cleared_rows > 0:
            score += cleared_rows * 100

    # Завершение игры
    pygame.quit()

# Запуск игры
if __name__ == "__main__":
    main()