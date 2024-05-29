import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='C:/Coding/Own/Python/Google-OCR/adroit-booth-424814-j5-2ba92fa29155.json'


def detect_labels(path):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels:")

    for label in labels:
        print(label.description,end=' ')

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

detect_labels('C:/Coding/Own/Python/Google-OCR/images/image4.jpg')