from PIL import Image

# Open the image
img = Image.open('Gemini_Generated_Image_uio330uio330uio3.png')

# Get dimensions
width, height = img.size

# Calculate half dimensions using proper centering to avoid side cropping
half_width = (width + 1) // 2  # Ceiling division for width
half_height = (height + 1) // 2  # Ceiling division for height

# Crop top-left quadrant
top_left = img.crop((0, 0, width // 2, height // 2))
top_left.save('image1.png')

# Crop top-right quadrant (preserves right edge)
top_right = img.crop((width // 2, 0, width, height // 2))
top_right.save('image2.png')

# Crop bottom-left quadrant
bottom_left = img.crop((0, height // 2, width // 2, height))
bottom_left.save('image3.png')

# Crop bottom-right quadrant (preserves right and bottom edges)
bottom_right = img.crop((width // 2, height // 2, width, height))
bottom_right.save('image4.png')

print("Image cropped into 4 parts: image1.png, image2.png, image3.png, image4.png")