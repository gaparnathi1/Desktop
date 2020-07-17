import qrcode
# example data
data = input("Enter The Text for generate QR code: ")   #"https://www.thepythoncode.com"
# output file name
filename = input("Enter The file with Extenstion (.png): ")
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)