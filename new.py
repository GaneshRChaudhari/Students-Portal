from PIL import Image, ImageDraw, ImageFont

# Image dimensions
width = 800
height = 600

# Create a blank image with a white background
image = Image.new('RGB', (width, height), 'white')

# Create a drawing object to draw on the image
draw = ImageDraw.Draw(image)

# Load a system font (you can replace 'arial.ttf' with an available font on your system)
font = ImageFont.load_default()

# Draw a computer screen
screen_color = (220, 220, 220)
screen_x1, screen_y1, screen_x2, screen_y2 = 100, 100, 700, 500
draw.rectangle([screen_x1, screen_y1, screen_x2, screen_y2], fill=screen_color, outline='black')

# Create a code snippet
code = [
    "def main():",
    "    print('Hello, World!')",
    "",
    "if __name__ == '__main__':",
    "    main()"
]

text_color = 'black'
x, y = 120, 120
line_height = 20

for line in code:
    draw.text((x, y), line, fill=text_color, font=font)
    y += line_height

# Save the image to a file
image.save('computer_programming_image.png')
image.show()
