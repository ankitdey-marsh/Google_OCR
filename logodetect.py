import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='C:/Coding/Own/Python/Google-OCR/adroit-booth-424814-j5-2ba92fa29155.json'

def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print("Logos:")

    for logo in logos:
        print(logo.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )