import os
from . import imageUtils, qrspawn
basedir=os.path.dirname(os.path.abspath(__file__))
svg=""
with open(os.path.join(basedir,"assets","spawn.svg"),encoding="utf-8")as fp:
    svg=fp.read()
name_tags = [
    """<tspan id="tspan21156" x="314.55869" y="574.99433" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:47.7046px;font-family:'Microsoft YaHei';-inkscape-font-specification:'Microsoft YaHei';fill:#ffffff;fill-opacity:1;stroke-width:1.08168">{name1}</tspan>""",
    """<tspan id="tspan21156" x="314.55869" y="551.14203" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:47.7046px;font-family:'Microsoft YaHei';-inkscape-font-specification:'Microsoft YaHei';fill:#ffffff;fill-opacity:1;stroke-width:1.08168">{name2_l1}</tspan>
    <tspan id="tspan21156" x="314.55869" y="610.77278" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:47.7046px;font-family:'Microsoft YaHei';-inkscape-font-specification:'Microsoft YaHei';fill:#ffffff;fill-opacity:1;stroke-width:1.08168">{name2_l2}</tspan>"""
]
def makeWechatRollSvg(name,pic,qrdata,m,d,max_len_per_line=14):
    names=[]
    if len(name)>max_len_per_line:
        names.append(name[:max_len_per_line])
        if len(name[max_len_per_line:])>max_len_per_line-1:
            names.append(f"{name[max_len_per_line:max_len_per_line*2]}…")
        else:
            names.append(name[max_len_per_line:])
    name_tag=""
    if len(names):
        name_tag=name_tags[1].format(name2_l1=names[0],name2_l2=names[1])
    else:
        name_tag=name_tags[0].format(name1=name)
    return svg.format(name_tags=name_tag, m=m, d=d, qrcode=qrspawn.make_qr(qrdata), pic=imageUtils.image_to_base64(pic))