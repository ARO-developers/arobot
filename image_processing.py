from PIL import Image
import numpy as np


def generate_tiles():
    filepath = "./ARO_logo-removebg-preview_1.png"  # downscaled and cropped image, so it has 128x64
    test = "./test002.png"  # testing image ("./test001.png", "./test002.png")

    imp = Image.open(filepath)
    im = np.array(imp)
    imp.close()

    final = []

    for row in im:
        final_row = []
        for pix in row:
            final_pix = (pix[0] << 16) + (pix[1] << 8) + pix[2]
            final_row.append(final_pix)
        final.append(final_row)
    return final


output = generate_tiles()
# print(imp)
print(output)
print(f"final size: {len(output[0])}x{len(output)}")
