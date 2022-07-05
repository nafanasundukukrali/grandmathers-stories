import os

import pygame
from math import cos, sin

WIDTH = 600  # ширина игрового окна
HEIGHT = 500  # высота игрового окна
FPS = 100  # частота кадров в секунду

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (175, 238, 238)


class BubbleSprite:
    """
    Спрайт шарика с воздухом
    """

    def __init__(self, surface, start_x=100):
        self.surface = surface
        self.i = 0
        self.x = start_x
        self.r = 7
        self.y = self.surface.get_rect().height - 10

        self.r_w = self.r//3
        self.x_w = self.r//3
        self.y_w = -self.r//10

        self.x_counter = 0
        self.df = 1

    def draw(self):
        """
        Отрисовывание шарика
        """

        # Контур шарика
        self.y = (self.y - 1 if self.y >= 0 else self.surface.get_rect().height - 10)

        if self.x_counter < 10:
            self.x_counter += 1
        else:
            self.df *= -1
            self.x_counter = 0

        self.x += self.df
        pygame.draw.circle(self.surface, BLUE, (self.x, self.y), self.r, 1)

        # Вращающаяся тень
        if self.i <= 360 and self.x_counter % 5 == 0:
            self.i += 3
        elif self.i > 360:
            self.i = 0

        angle = self.i * (3.14 / 180)
        x = self.x_w * cos(angle) + self.x_w * sin(angle)
        y = self.y_w * sin(angle) - self.y_w * cos(angle)

        pygame.draw.circle(self.surface, BLUE, (self.x + x, self.y + y), self.r_w)


class FishSprite(pygame.sprite.Sprite):
    """
    Спрайт рыбки
    """

    def __init__(self, start_x=50, start_y=100):
        super(FishSprite, self).__init__()
        self.images = self.load_images('./fish')
        self.fish_count = 0
        self.index = 0
        self.df = 1
        self.image = self.images[self.index]
        self.rect = pygame.Rect(start_x, start_y, 0, 0)
        self.pos_x = start_x
        self.pos_y = start_y

    @staticmethod
    def load_images(path):
        """
        Загрузка изображений
        """

        images = []

        for image in os.listdir(path):
            image_py = pygame.image.load(os.path.join(path, image)).convert_alpha()
            image_py = pygame.transform.scale(image_py, (100, 60))
            image_py = pygame.transform.flip(image_py, True, False)
            images.append(image_py)

        return images

    def update(self):
        """
        Обновление спрайта
        """

        if self.fish_count % 5 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.fish_count = 1
        else:
            self.fish_count += 1

        if self.rect.x + self.image.get_width() >= WIDTH or self.rect.x <= 0:
            self.df *= -1

            for i in range(len(self.images)):
                self.images[i] = pygame.transform.flip(self.images[i], True, False)

            self.image = pygame.transform.flip(self.image, True, False)

        self.rect.move_ip(self.df, 0)


def make_gradient(input_surface: pygame.Surface, angle_direction: int, colour_1: pygame.Color,
                  colour_2: pygame.Color):
    """
    Функция для рисования градиента на фоне
    """

    inverse_rotated_input = pygame.transform.rotate(input_surface, -angle_direction)
    gradient_size = inverse_rotated_input.get_rect().size

    # Создаётся и красится маленькая поверхность
    pixel_width = 2
    colour_pixels_surf = pygame.Surface((pixel_width, 1), flags=pygame.SRCALPHA)
    colour_pixels_surf.fill(colour_1, pygame.Rect((0, 0), (1, 1)))
    colour_pixels_surf.fill(colour_2, pygame.Rect((1, 0), (1, 1)))

    # Создаётся новая поверхность нужных размеров, маленькая натягивается на неё
    gradient_surf = pygame.Surface(gradient_size, flags=pygame.SRCALPHA)

    scale = float(max(gradient_size[0] / pixel_width, gradient_size[1]))
    zoomed_surf = pygame.transform.rotozoom(colour_pixels_surf, 0, scale)
    pygame.transform.scale(zoomed_surf, gradient_size, gradient_surf)

    # Поворот поверхности
    gradient_surf = pygame.transform.rotate(gradient_surf, angle_direction)

    return gradient_surf


surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

pygame.display.set_caption("Fish")
clock = pygame.time.Clock()

# Вода
background = pygame.Surface((WIDTH, HEIGHT * 2 / 3))
background = make_gradient(background, 90, pygame.Color("#06246F"), pygame.Color("#5DC8CD"))

# Песок
bottom = pygame.Surface((WIDTH, HEIGHT / 3))
bottom = make_gradient(bottom, 90, pygame.Color("#1D766F"), pygame.Color("#06246F"))

# Рыбки
fish_1 = FishSprite(start_y=HEIGHT//2)
fish_2 = FishSprite(10, HEIGHT//2 - 45)
fish_3 = FishSprite(10, HEIGHT//2 + 45)

fish_sprites_1 = pygame.sprite.Group(fish_1)
fish_sprites_2 = pygame.sprite.Group(fish_2)
fish_sprites_3 = pygame.sprite.Group(fish_3)

# Пузырьки с воздухом
bubble_1 = BubbleSprite(surface)
bubble_2 = BubbleSprite(surface, WIDTH - 100)
bubble_3 = BubbleSprite(surface, WIDTH - 50)
bubble_4 = BubbleSprite(surface, 50)

running = True

while running:
    time_delta = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.blit(background, (0, 0))
    surface.blit(bottom, (0, HEIGHT * 2 / 3))

    fish_sprites_1.update()
    fish_sprites_1.draw(surface)
    fish_sprites_2.update()
    fish_sprites_2.draw(surface)
    fish_sprites_3.update()
    fish_sprites_3.draw(surface)

    bubble_1.draw()
    bubble_2.draw()
    bubble_3.draw()
    bubble_4.draw()

    pygame.display.update()

pygame.quit()
