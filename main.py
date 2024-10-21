from PIL import Image


image = Image.open('monro.jpg')

red, green, blue = image.split()


coordinates = (100, 0, red.width, red.height)
cropped_red_left = red.crop(coordinates)

coordinates = (50, 0, red.width - 50, red.height)
cropped_red_center = red.crop(coordinates)

blended_red = Image.blend(cropped_red_left, cropped_red_center, 0.5)


coordinates = (0, 0, blue.width - 100, blue.height)
cropped_blue_right = blue.crop(coordinates)

coordinates = (50, 0, blue.width - 50, blue.height)
cropped_blue_center = blue.crop(coordinates)

blended_blue = Image.blend(cropped_blue_right, cropped_blue_center, 0.5)


coordinates = (50, 0, green.width - 50, green.height)
cropped_green_center = green.crop(coordinates)


drunk_monroe = Image.merge("RGB", (blended_red, cropped_green_center, blended_blue))
drunk_monroe.save('drunk_monroe_normal.jpg')

drunk_monroe.thumbnail((80, 80))
drunk_monroe.save('drunk_monroe_mini.jpg')