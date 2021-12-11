from PIL import Image
from PIL import ImageEnhance

path = r"/Users/ameyashukla/Ameya Shukla Personal/Ameya/Ameya.jpg"

img = Image.open(path)
img.show()

# Brightness
curr_br = ImageEnhance.Brightness(img)
new_br = 4
img_new_br = curr_br.enhance(new_br)
img_new_br.show()

# Color
curr_color = ImageEnhance.Color(img)
new_color = 4
img_new_color = curr_color.enhance(new_color)
img_new_color.show()

# Contrast
curr_contrast = ImageEnhance.Contrast(img)
new_contrast = 4
img_new_contrast = curr_contrast.enhance(new_contrast)
img_new_contrast.show()

# Sharpness
curr_sharpness = ImageEnhance.Sharpness(img)
new_sharpness = 4
img_new_sharpness = curr_sharpness.enhance(new_sharpness)
img_new_sharpness.show()

