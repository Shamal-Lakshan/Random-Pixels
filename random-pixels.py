# Importing the required libraries
import random
import uuid

from PIL import Image, ImageDraw

image_id = uuid.uuid1()


print("████████████████████████████████████████████████████████████████████████████")
print("█▄─▄▄▀██▀▄─██▄─▀█▄─▄█▄─▄▄▀█─▄▄─█▄─▀█▀─▄███▄─▄▄─█▄─▄█▄─▀─▄█▄─▄▄─█▄─▄███─▄▄▄▄█")
print("██─▄─▄██─▀─███─█▄▀─███─██─█─██─██─█▄█─█████─▄▄▄██─███▀─▀███─▄█▀██─██▀█▄▄▄▄─█")
print("▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀")
print()
print()
print(f'Processing image id: {image_id}')
print()
print(f'Processing Completed!')
print()
print(f'Check the output folder for {image_id}.png')

image = Image.new('RGB', (1920, 1080))
width, height = image.size


# Width of the generated rectangles
rectangle_width = 100

# Height of the generated rectangles
rectangle_height = 100

# Definning the number of rectangles
number_of_rectangles = random.randint(1500, 3000)

# Number of circles
number_of_circles = random.randint(1000, 1500)

# Creates the canvas
draw_image = ImageDraw.Draw(image)

# for x in range(number_of_circles):

# Drawing on the canvas
for i in range(number_of_rectangles):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_x_2 = random.randint(0, width)
    rectangle_y_2 = random.randint(0, height)

    rectangle_x_3 = rectangle_x_2 / 2
    rectangle_y_3 = rectangle_y_2 / 2



    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )


    rectangle_shape = [
        (rectangle_x, rectangle_y), (rectangle_x + rectangle_width / 2, rectangle_y + rectangle_height / 2)]

    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )


    rectangle_shape = [
        (rectangle_x - 10, rectangle_y + 5), (rectangle_x + rectangle_width / 5, rectangle_y + rectangle_height / 5)]

    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )

    rectangle_shape = [
        (rectangle_x_2, rectangle_y_2), (rectangle_x_2 + rectangle_width / 3, rectangle_y_2 + rectangle_height / 3)]

    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )


    rectangle_shape = [
        (rectangle_x_3, rectangle_y_3), (rectangle_x_3 + rectangle_width / 3, rectangle_y_3 + rectangle_height / 3)]

    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )


# Saves the image
image.save(f'./output/{image_id}.png')
