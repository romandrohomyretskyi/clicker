from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from random import randint

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class GameScreen(Screen):
    points = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self, *args):
        self.ids.animal.new_animal()

class Animal(Image):
    is_anim = False
    hp = None
    animal = None
    animal_index = 0
    LEVELS = ['Mercury', 'Venus', 'Earth', 'Mars',
              'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    ANIMAL = {
        'Mercury': {"source": 'assets/images/1.png', 'hp': 10},
        'Venus': {"source": 'assets/images/2.png', 'hp': 20},
        'Earth': {"source": 'assets/images/3.png', 'hp': 30},
        'Mars': {"source": 'assets/images/4.png', 'hp': 40},
        'Jupiter': {"source": 'assets/images/5.png', 'hp': 50},
        'Saturn': {"source": 'assets/images/6.png', 'hp': 60},
        'Uranus': {"source": 'assets/images/7.png', 'hp': 80},
        'Neptune': {"source": 'assets/images/8.png', 'hp': 100},
    }
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.points +=1
            self.hp -= 1
            if self.hp <= 0:
                self.new_animal()
                
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y = y-5, duration = 0.05) + \
                Animation(x=x, y = y, duration = 0.005)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)

    def new_animal(self):
        self.animal = self.LEVELS[randint(0, len(self.LEVELS)) - 1]
        self.source = self.ANIMAL[self.animal]['source']
        self.hp = self.ANIMAL[self.animal]['hp']
        self.keep_ratio = False  
        self.allow_stretch = True  



class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm

    if platform != 'android':
        Window.size = (400, 800)
        Window.left = 500
        Window.top = 100

if __name__ == '__main__':
    app = MainApp()
    app.run()

