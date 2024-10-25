import pygame as pg

class Area():
    def __init__(self,pos : pg.Vector2,
                    size: pg.Vector2,
                    color: pg.Color = None,
                    border_width: float = None,
                    border_color: pg.Color = None):
        
        self.rect = pg.Rect(pos,size)
        self.color = color if color else pg.Color(255,255,255)
        self.border_width = border_width if border_width else 0 
        self.border_color = border_color if border_color else color
        self.surface = pg.Surface(self.rect.size).convert_alpha()
        self._buffer_surface = self.surface.copy()
        self._background = True
        self.is_active = True

    def draw(self,surface:pg.Surface):
        if self.is_active:
            if self._background:
                pg.draw.rect(surface, self.color, self.rect)
            surface.blit(self.surface, self.rect)
            if self.border_width > 0 :
                pg.draw.rect(surface, self.border_color, self.rect, self.border_width)


    def update(self):
        if not self.is_active:
            return

    def move(self, pos: pg.Vector2):
        self.rect.x = pos.x
        self.rect.y = pos.y

    def set_size(self, size: pg.Vector2):
        self.rect.width = size.x
        self.rect.width = size.y
        self.surface = pg.transform.scale(self._buffer_surface, self.rect.size)
    