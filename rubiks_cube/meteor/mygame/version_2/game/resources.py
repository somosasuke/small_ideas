import pyglet

pyglet.resource.path = ['C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/meteor/mygame/recursos']
pyglet.resource.reindex()

def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

player_image = pyglet.resource.image("player.png")
center_image(player_image)
bullet_image = pyglet.resource.image("bullet.png")
center_image(bullet_image)
asteroid_image = pyglet.resource.image("asteroid.png")
center_image(asteroid_image)
