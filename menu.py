from ursina import *

class mainmenu(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        Tittle = Text('Zero',font = "fonts/Oswald-Regular.ttf",position=Vec2(-0.1,0.25),scale = 5)
        Practice = Button(color = color.white,text='Single Player',scale = (4,0.5),position=Vec2(-0.1,0.35))
        Multipplayer = Button(color = color.white,text='Multi Player',scale = (4,0.5),position=Vec2(-0.1,0.45))
        Quit = Button(color = color.white,text='Quit',scale = (4,0.5),position=Vec2(-0.1,0.55))
