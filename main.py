import event, time, cyberpi
from image_processing import generate_tiles  # if PIL or Numpy not installed, comment this line

# initialize variables

im_array = generate_tiles()  # if PIL or Numpy not installed, replace this with pre-generated list sent in discord
sprite = cyberpi.sprite()
width = len(im_array[0])
height = len(im_array)


# Hope it works :)
@event.is_press('a')
def is_btn_press():
    if width > 128 or height > 128:
        print("Image is too large!")
        return
    pixels = []
    for row in im_array:
        pixels.extend(row)
    sprite.draw_pixel(pixels, width, height)
    sprite.rotate_to(angle=90)
    sprite.move_to(64, 64)
    sprite.show()
    cyberpi.screen.render()

# TODO: Test it and maybe make the code more readable. And there's definitely space for optimization and improvement.
