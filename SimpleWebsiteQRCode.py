import qrcode 
import qrcode.image.svg
import os


def get_output_location():
    directory = input("Input folder path for QR Code output: ")
    fileName = input("Input a filename for QR Code: ").split(".")[0]
    return os.path.join(directory,fileName)
    
if __name__ == "__main__":
    outputPath = get_output_location() + ".png"
    qr = qrcode.QRCode(version=10)
    websiteUrl = input("Insert URL for website: ")
    qr.add_data(websiteUrl)
    qr.make()
    image = qr.make_image()
    image.save(outputPath)

