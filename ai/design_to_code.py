from PIL import Image
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def design_to_code(image_file):
    # Process the image (e.g., resize)
    image = Image.open(image_file.stream)
    image.save("temp.png")
    
    # Use GPT-4 Vision to geneate code
    response = openai.ChatCompletion.create(
        model = "gpt-4-vision-preview",
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Convert this design into HTML/CSS code."},
                    {"type": "image-url", "image_url": {"url": "temp.png"}},
                ],
            }
        ],
        max_tokens = 1000,
    )
    return response.choices[0].message.content 