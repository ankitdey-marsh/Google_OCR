import os
import handwriting as hw
import imagetotext as itt
import logodetect as ld
import label as lb

os.system('cls' if os.name == 'nt' else 'clear')
print("Enter 1 to detect text from handwriting")
print("Enter 2 to detect text from image")
print("Enter 3 to detect logo from image")
print("Enter 4 to detect labels from image ")
choice=int(input("Enter choice : "))
path=input("Enter path to image: ")
os.system('cls' if os.name == 'nt' else 'clear')
match choice:
    case 1:
        hw.detect_handwritten_ocr(path)
    case 2:
        itt.detect_document(path)
    case 3:
        ld.detect_logos(path)
    case 4:
        lb.detect_labels(path)
    case _:
        print("Invalid Choice")
