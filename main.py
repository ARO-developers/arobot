import event, time, cyberpi
from ARO_logo import generate_tiles

# initialize variables

tiles = generate_tiles()  # if PIL or Numpy not installed, replace this with pre-generated list sent in discord
sprites = []
for h in range(32):
    sprites.append(cyberpi.sprite())


# Hope it works :)
@event.is_press('a')
def is_btn_press():
    for i in range(len(sprites)):
        sprites[i].draw_pixel(tiles[i])
    count = 0
    for j in (40, 56, 72, 88):  # positioning the sprites
        for k in (8, 24, 40, 56, 72, 88, 104, 120):
            sprites[count].move_to(k, j)
            sprites[count].show()
            count += 1
    cyberpi.screen.render()

# TODO: Test it and maybe make the code more readable. And there's definitely space for optimization and improvement.
