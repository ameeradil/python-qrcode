import qrcode

url = input("Enter your URL: ")

img = qrcode.make(url)
img.save("qrcode.svg")

print('Congrats! Your qr code is generated')
