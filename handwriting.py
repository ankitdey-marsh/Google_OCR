import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='C:/Coding/Own/Python/Google-OCR/adroit-booth-424814-j5-2ba92fa29155.json'

def detect_handwritten_ocr(path):
    """Detects handwritten characters in a local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision_v1p3beta1 as vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Language hint codes for handwritten OCR:
    # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.ImageContext(language_hints=["en-t-i0-handwrit"])

    response = client.document_text_detection(image=image, image_context=image_context)

    print(f"{response.full_text_annotation.text}")

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

