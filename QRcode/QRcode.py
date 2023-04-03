'''

# Simple qr code generate
import qrcode

# make --> add data to qr
# save --> save qr as png 
image = qrcode.make("https://github.com/aryan19461")
image.save("qr_normal.png")


'''
# Advance qr --> font and border filling etc
import qrcode 

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H, # removes high level error
    box_size=15,
    version=1,
    border = 8,

)
qr.add_data("https://github.com/aryan19461")
qr.make(fit=True) # if data is already in qr code --> fit = True    
qr.make_image(fill_color="pink", back_color="Blue").save("qr_advance.png")

