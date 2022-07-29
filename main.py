from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

window.title = "Minecraft"



def update():
    if held_keys['q']:
        application.quit()

app.run()