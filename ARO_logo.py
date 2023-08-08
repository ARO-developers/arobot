from PIL import Image
import numpy as np


def generate_tiles():
    filepath = "./ARO_logo-removebg-preview_1.png"  # downscaled and cropped image, so it has 128x64
    test = "./test002.png"  # testing image ("./test001.png", "./test002.png")
    im_height = 64
    im_width = 128
    tile_height = 16
    tile_width = 16

    imp = Image.open(filepath)
    im = np.array(imp)

    final = []

    # And here starts the nasty code: ...A lot of things happening here...
    for i in range(im_height // tile_height):
        for j in range(im_width // tile_width):
            tile = []
            final_tile = []
            for h in range(tile_height):
                tile_row = []
                for w in range(tile_width):
                    tile_row.append(im[tile_height * i + h][tile_width * j + w])
                tile.append(tile_row)
            # ^^^ This part generates smaller arrays (images) ^^^
            for row in tile:
                for pix in row:
                    hex_pix = (pix[0] << 16) + (pix[1] << 8) + pix[2]
                    final_tile.append(hex_pix)
            # ^^^ This part extracts the colors from the tiles ^^^
            final.append(final_tile)
    return final


output = generate_tiles()
# print(imp)
print(output)
print(f"final length: {len(output)}")
