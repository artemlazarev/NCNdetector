import moondream as md
from PIL import Image

# Initialize with your API key
model = md.vl(api_key="YOUR_API_KEY")

# Load an image
image = Image.open("path/to/image.jpg")

# Ask a question
result = model.query(image, "What is in this image?")
print(result["answer"])