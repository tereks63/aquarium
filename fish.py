
import random
import pygame as pg
from sprite import Sprite



class Fish(Sprite):
    bounds = (0,800,0,800)
    field_of_view = 100
    def __init__(self, path: str,
                 size: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 speed: pg.Vector2,
                 *groups):
        super().__init__(path, size, pos, *groups)
        self.speed = speed
        dir = self.speed
        self.field_of_view = Fish.field_of_view
        angle = dir.angle_to(pg.Vector2(1,0))
        self._rotate(angle)

    def update(self, foods:pg.sprite.Group):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
        min_r = 1000
        curent_food = None
        for food in foods:
            d_x = self.rect.x - food.rect.x
            d_y = self.rect.y - food.rect.y
            r = pow(pow(d_x,2) + pow(d_y,2), 0.5)
            if r <= self.field_of_view:
                if r < min_r:
                    min_r = r
                    curent_food = food
        if curent_food:
            self.look_to(pg.Vector2(curent_food.rect.x,curent_food.rect.y))
                    
        
        if self.calc_distance_to_bounds():
            new_angle = random.randint(60, 180) * random.choice([-1,1])
            new_dir = self.speed.rotate(new_angle)
            self.change_direction(new_dir)
            dir = self.speed
            angle = dir.angle_to(pg.Vector2(1,0))
            self._rotate(angle)

    def change_direction(self, dir: tuple[int | float, int | float]):
        angle = self.speed.angle_to(dir)
        self.speed = self.speed.rotate(angle)
        angle = dir.angle_to(pg.Vector2(1,0))
        self._rotate(angle)
        
    def calc_distance_to_bounds(self):
        check_left = abs(Fish.bounds[0] - self.rect.centerx) <= 20
        check_right = abs(Fish.bounds[1] - self.rect.centerx) <= 20
        check_bottom = abs(Fish.bounds[3] - self.rect.centery) <= 20
        check_top = abs(Fish.bounds[2] - self.rect.centery) <= 20
        if check_left or check_right or check_bottom  or check_top:
            return True
        return False
    
    def draw(self, surface: pg.Surface):
        super().draw(surface)
        pg.draw.rect(surface,(255,0,0), self.rect, 10)
        surface.blit(self.image, self.rect)

    def _rotate (self, angle: float):
        x, y = self.rect.x, self.rect.y
        self.image = pg.transform.rotate(self._buffer_image, angle)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def look_to(self, target: pg.Vector2):
        dx = target.x - self.rect.x
        dy = target.y - self.rect.y
        self.change_direction(pg.Vector2(dx, dy))



 

