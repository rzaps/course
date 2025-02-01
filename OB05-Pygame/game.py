import pygame
import random

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH = 800
HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race")

# Часы
clock = pygame.time.Clock()

# Загрузка изображений
player_img = pygame.image.load('player.png')  # Замените на путь к вашему изображению
enemy_img = pygame.image.load('enemy.png')    # Замените на путь к вашему изображению

# Размеры машин
CAR_WIDTH = 50
CAR_HEIGHT = 100

# Параметры дороги
ROAD_WIDTH = 400
ROAD_X = (WIDTH - ROAD_WIDTH) // 2

# Класс для дороги
class Road:
    def __init__(self, road_x, road_width):
        self.x = road_x
        self.width = road_width
        self.speed = 10
        self.y1 = 0
        self.y2 = -HEIGHT  # Вторая полоса будет начинаться за экраном
        self.curbs = []  # Список поребриков (красные и белые прямоугольники)
        self.lines = []  # Разделительные полосы

        # Генерация полос по краям дороги
        for y in range(0, HEIGHT, 60):  # Каждый 20 пикселей
            # Слева
            color_left = RED if (y // 60) % 2 == 0 else WHITE
            self.curbs.append({'color': color_left, 'x': self.x - 10, 'y': y,
                               'width': 20, 'height': 60})
            # Справа
            color_right = RED if ((y + 10) // 60) % 2 == 0 else WHITE
            self.curbs.append({'color': color_right, 'x': self.x +
                                                          self.width, 'y': y,
                               'width': 20, 'height': 60})

        # Генерация разделительных полос
        for y in range(-HEIGHT, HEIGHT * 2, 60):  # Каждые 40 пикселей
            self.lines.append({'x': self.x + self.width // 2 - 5, 'y': y,
                               'width': 5, 'height': 20})

    def move(self):
        self.y1 += self.speed
        self.y2 += self.speed

        # Когда одна полоса выходит из экрана, переносим её вниз
        if self.y1 > HEIGHT:
            self.y1 = -HEIGHT
        if self.y2 > HEIGHT:
            self.y2 = -HEIGHT

        # Перемещение поребриков
        for curb in self.curbs:
            curb['y'] += self.speed
            if curb['y'] > HEIGHT:
                curb['y'] = -20  # Перемещаем поребрики вверх, когда они выходят за экран

        # Перемещение разделительных полос
        for line in self.lines:
            line['y'] += self.speed
            if line['y'] > HEIGHT:
                line['y'] = -40  # Перемещаем полосы вверх, когда они выходят за экран

    def draw(self):
        pygame.draw.rect(screen, GRAY, (self.x, 0, self.width, HEIGHT))  # Дорога
        pygame.draw.rect(screen, WHITE, (self.x, 0, 10, HEIGHT))  # Левая граница
        pygame.draw.rect(screen, WHITE, (self.x + self.width - 10, 0, 10, HEIGHT))  # Правая граница

        # Отображаем полосы (поребрики)
        for curb in self.curbs:
            pygame.draw.rect(screen, curb['color'], (curb['x'], curb['y'], curb['width'], curb['height']))

        # Отображаем разделительные полосы
        for line in self.lines:
            pygame.draw.rect(screen, WHITE, (line['x'], line['y'], line['width'], line['height']))


# Класс для игрока
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

        # Ограничение движения игрока в пределах дороги
        if self.x < ROAD_X + 10:
            self.x = ROAD_X + 10
        elif self.x > ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10:
            self.x = ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - CAR_HEIGHT:
            self.y = HEIGHT - CAR_HEIGHT

    def draw(self):
        screen.blit(player_img, (self.x, self.y))

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -5
            elif event.key == pygame.K_RIGHT:
                self.x_change = 5
            elif event.key == pygame.K_UP:
                self.y_change = -5
            elif event.key == pygame.K_DOWN:
                self.y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.y_change = 0


# Класс для врага
class Enemy:
    def __init__(self, x, y, min_speed, max_speed):
        self.x = x
        self.y = y
        self.speed = random.randint(min_speed, max_speed)  # Случайная скорость
        self.image = enemy_img
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self):
        self.y += self.speed
        self.x += random.randint(-1, 1)  # Немного случайного отклонения по горизонтали

        # Ограничиваем движение врагов по горизонтали
        if self.x < ROAD_X + 10:
            self.x = ROAD_X + 10
        elif self.x > ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10:
            self.x = ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10

        # Если враг выходит за пределы экрана, сбрасываем его
        if self.y > HEIGHT:
            self.y = -CAR_HEIGHT  # Снова сверху
            self.x = random.randint(ROAD_X + 10, ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10)

        self.rect.topleft = (self.x, self.y)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


# Класс для управления всеми врагами
class EnemyManager:
    def __init__(self, num_enemies, min_speed, max_speed):
        self.enemies = []
        self.num_enemies = num_enemies
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.create_enemies()

    def create_enemies(self):
        for _ in range(self.num_enemies):
            while True:
                x_pos = random.randint(ROAD_X + 10, ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10)
                y_pos = random.randint(-HEIGHT, -CAR_HEIGHT)
                new_enemy = Enemy(x_pos, y_pos, self.min_speed, self.max_speed)

                # Проверяем на столкновение с другими врагами
                if not self.check_collision(new_enemy):
                    self.enemies.append(new_enemy)
                    break

    def check_collision(self, new_enemy):
        for enemy in self.enemies:
            if new_enemy.rect.colliderect(enemy.rect):
                return True
        return False

    def resolve_collisions(self):
        for i, enemy1 in enumerate(self.enemies):
            for enemy2 in self.enemies[i + 1:]:
                if enemy1.rect.colliderect(enemy2.rect):
                    # Если столкновение обнаружено, отталкиваем врагов на 40 пикселей
                    if enemy1.x < enemy2.x:
                        enemy1.x -= 10  # Отталкиваем влево
                        enemy2.x += 10  # Отталкиваем вправо
                    else:
                        enemy1.x += 10  # Отталкиваем вправо
                        enemy2.x -= 10  # Отталкиваем влево

                    # Ограничиваем движение врагов по горизонтали
                    if enemy1.x < ROAD_X + 10:
                        enemy1.x = ROAD_X + 10
                    elif enemy1.x > ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10:
                        enemy1.x = ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10
                    if enemy2.x < ROAD_X + 10:
                        enemy2.x = ROAD_X + 10
                    elif enemy2.x > ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10:
                        enemy2.x = ROAD_X + ROAD_WIDTH - CAR_WIDTH - 10

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()
        self.resolve_collisions()

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.draw()


# Основная функция игры
def game_loop():
    player = Player(WIDTH * 0.45, HEIGHT * 0.8)
    road = Road(ROAD_X, ROAD_WIDTH)
    enemy_manager = EnemyManager(5, 2, 5)  # 5 врагов с разной скоростью (от 2 до 5)

    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Управление игроком
            player.handle_keys(event)

        player.move()

        # Фон
        screen.fill(BLACK)

        # Отрисовка дороги
        road.move()
        road.draw()

        # Обновление и отрисовка врагов
        enemy_manager.move_enemies()
        enemy_manager.draw_enemies()

        # Отрисовка игрока
        player.draw()

        # Увеличение очков
        score += 1

        # Проверка столкновений с врагами
        for enemy in enemy_manager.enemies:
            if player.y < enemy.y + CAR_HEIGHT and player.y + CAR_HEIGHT > enemy.y:
                if player.x < enemy.x + CAR_WIDTH and player.x + CAR_WIDTH > enemy.x:
                    game_over = True

        pygame.display.update()
        clock.tick(60)

    # После завершения игры
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 50))
    pygame.display.update()
    pygame.time.wait(3000)  # Ждем 3 секунды перед закрытием


# Запуск игры
game_loop()
pygame.quit()
