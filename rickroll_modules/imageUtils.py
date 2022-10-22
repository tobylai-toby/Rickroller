import mimetypes,base64,os
from io import BytesIO
from svglib import svglib
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
basedir=os.path.dirname(os.path.abspath(__file__))
# svglib.find_font("微软雅黑")
# svglib.find_font("Microsoft YaHei")
#registerFont(TTFont("Microsoft YaHei",os.path.join(basedir,"assets","HarmonyOS_Sans_SC_Light.ttf")))
def image_to_base64(path):
    with open(path, 'rb') as img:
        b64encode = base64.b64encode(img.read())
        s = b64encode.decode()
        tp=mimetypes.guess_type(f"file:///{path}")
        return f'data:{tp[0]}/{tp[1]};base64,{s}'

def pilimage2b64(img,coding="utf-8"):
    img_format=img.format
    if img_format is None:
        img_format="JPEG"
    format_str="JPEG"
    if img_format.lower() == 'png':
        format_str = 'PNG'
    if img_format.lower() == 'gif':
        format_str = 'gif'
    if img.mode == "P":
        img = img.convert('RGB')
    if img.mode == "RGBA":
        format_str = 'PNG'
        img_format = 'PNG'

    output_buffer = BytesIO()
    img.save(output_buffer, format=format_str)
    byte_data = output_buffer.getvalue()
    return f'data:image/{img_format.lower()};base64,{base64.b64encode(byte_data).decode(coding)}'

def svg2jpg(svgpath,jpgpath):
    drawing = svg2rlg(svgpath)
    renderPM.drawToFile(drawing, jpgpath, fmt="JPG")

