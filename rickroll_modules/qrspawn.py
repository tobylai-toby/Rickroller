import qrcode
from .imageUtils import pilimage2b64

def make_qr(data):
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=2,border=0)
    qr.add_data(data)
    qr.make(fit=True)
    return pilimage2b64(qr.make_image())