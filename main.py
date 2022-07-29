from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from menu import mainmenu
app = Ursina()
Sky()
window.title = "Minecraft"

menu = mainmenu()

def update():
    if held_keys['q']:
        application.quit()

app.run()