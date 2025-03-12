from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PinRequest(BaseModel):
    keywords: str
    pin_type: str
    description_tone: str

# Title templates
title_templates = {
    "list": ["Top 10 {keywords} Ideas You Must Try!", "Best {keywords} Recipes for 2024"],
    "question": ["Looking for {keywords}? Here’s What You Need!"],
    "call-to-action": ["Try These {keywords} Today! Save This Pin Now!"],
    "audience-targeted": ["For {keywords} Lovers: You’ll Love These!"],
    "curiosity-driven": ["You Won’t Believe These {keywords} Hacks!"]
}

# Function to generate metadata
def generate_metadata(keywords, pin_type, description_tone):
    title = random.choice(title_templates.get(pin_type, title_templates["list"])).format(keywords=keywords)

    descriptions = {
        "formal": f"Discover the best {keywords} ideas that will elevate your experience. Save this Pin to keep it handy.",
        "casual": f"Looking for awesome {keywords}? Here are some must-try ideas! Don’t forget to Pin it.",
        "persuasive": f"If you love {keywords}, then you NEED to check this out. Click now for more!",
        "storytelling": f"Imagine waking up to the perfect {keywords}… Here’s how you can make it happen!"
    }

    description = descriptions.get(description_tone, descriptions["casual"])
    alt_text = f"A visually appealing image of {keywords}, perfect for Pinterest."

    return {"title": title, "description": description, "alt_text": alt_text}

@app.post("/generate")
def generate_pin_metadata(request: PinRequest):
    return generate_metadata(request.keywords, request.pin_type, request.description_tone)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
