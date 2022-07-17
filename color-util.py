from PIL import Image

img = Image.open('website-design-colors-bright-and-lively-more-text.PNG')
pixels = img.load() 
width, height = img.size
colors = []

for col in range(height):
    for row in range(width):
        r, g, b, a = pixels[row, col]
        colors.append(f"#{r:02x}{g:02x}{b:02x}")


unique_colors = list(set(colors))
print(unique_colors)