import qrcode
qr = qrcode.QRCode(
	version=2,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=1
)
#设置二维码的大小
# qr.add_data("https://blog.csdn.net/caidewei121/")
qr.add_data('123123')
qr.make(fit=True)
img = qr.make_image()
img.save("demo.png")