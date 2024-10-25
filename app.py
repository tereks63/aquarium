import pygame as pg

from UI.text_label import TextLabel
import aquarium
from sprite import Sprite


class App():
    def __init__(self,size:tuple[float],fps:int,name:str):
        pg.init()

        pg.display.init()
        self.running = True
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(name)
        
        self.fps=fps
        self.clock = pg.time.Clock()

    def start(self):
        self.aquarium = aquarium.Aquarium(5,"Sprites/fishes", 9,800,800)
        self.background = Sprite("Sprites/background.png", (800, 800), (0, 0))
        self.text_label = TextLabel(pos = pg.Vector2(100,100), size = pg.Vector2(200,70))
        self.text_label._background = False
        self.text_label.text_color(pg.Color(255,0,0))
        self.text_label.font_size(30)
        self.text_label.set_text("wosappppppppppppp")

    def main_loop(self):
        while self.running:
            self.background.draw(self.screen)
            self.aquarium.update(self.screen)
            self.text_label.draw(self.screen)
        
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.running = False
                if e.type == pg.MOUSEBUTTONDOWN:
                    x,y = pg.mouse.get_pos()
                    self.aquarium.add_food(pg.Vector2(x,y))
                    

            pg.display.update()
            self.clock.tick(self.fps) 


        