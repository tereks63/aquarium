from typing import Any
from fish import Fish
from sprite import Sprite
import pygame as pg
import random


class Food(Sprite):
    def destroy(self):
        del self 
    def set_dest_range(self,a: int ,b: int):
        self.dest_pos = random.randint(a,b)
    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.rect.y < self.dest_pos:
    
            self.rect.y += 4
    
        return super().update(*args, **kwargs)
    def check_collision(self,fish: Fish):
        left_x1 = self.rect.x 
        right_x1 = self.rect.x + self.rect.width
        up_y1 = self.rect.y
        down_y1 = self.rect.y + self.rect.height
        left_x2 = fish.rect.x 
        right_x2 =fish.rect.x + fish.rect.width
        up_y2 =fish.rect.y
        down_y2 = fish.rect.y + fish.rect.height
    
    

        if (((left_x2 <= right_x1 <= right_x2)
            or (left_x2 <= left_x1 <= right_x2))
            and(((down_y2 <=up_y1 <=up_y2)or (down_y2 <=down_y1 <=up_y2)))):
            return  True
        return False
    
