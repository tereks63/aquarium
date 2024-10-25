import pygame as pg
import random
import os
from fish import Fish
from food import Food

fish_sprite = []

def fetch_file_pathes(path: str):
    file_pathes = []
    try:
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                file_pathes.append(file_path)
        return file_pathes
    except Exception as e:
        print(e)


class Aquarium():
    def __init__(self,count, img_path, screen_width, float, screen_height: float):
        self.fishes = pg.sprite.Group()
        self.foods = pg.sprite.Group()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.img_pathes = fetch_file_pathes(img_path)
        for i in range(count):
            size = random.randint(25,100)
            speedex = random.randint(0,5)
            speedey = random.randint(0, 5)
            pos_y = random.randint(0, 800)
            pos_x = random.choice([0, 800])
            axolotl=Fish(random.choice(self.img_pathes), (size*2,size), (100,200),pg.Vector2(speedex,speedey))
            self.fishes.add(axolotl)

    def add_food(self, pos : pg.Vector2):
        food = Food("Sprites/food/EDA.png",
                    size=(10,10), pos=pos)
        food.set_dest_range(int(self.screen_height * 0.75), self.screen_height)
        self.foods.add(food)


    def update(self, screen: pg.Surface) -> None:
        self.foods.update()
        self.fishes.update(self.foods)
        self.fishes.draw(screen)
        self.foods.draw(screen)
        for food in self.foods:
            for fish in self.fishes:
                if food.check_collision(fish):
                    food.destroy()
                    