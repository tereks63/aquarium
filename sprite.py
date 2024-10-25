import pygame as pg

class Sprite(pg.sprite.Sprite):
    def __init__(self, path: str, size: tuple[int | float, int | float], pos: tuple[int | float, int | float], *groups):
        super().__init__(*groups)
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(self.image, size)
        self._buffer_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))