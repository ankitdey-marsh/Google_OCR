from google.cloud import vision
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='C:/Coding/Own/Python/Google-OCR/adroit-booth-424814-j5-2ba92fa29155.json'

def detect_document(path):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = "".join([symbol.text for symbol in word.symbols])
                    print(str(" {}".format(word_text)).strip()+' ', end="")


    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )


