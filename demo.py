from rickroll_modules import wechatRoll
from rickroll_modules import imageUtils
with open("res.svg","w",encoding="utf-8")as fp:
    fp.write(wechatRoll.makeWechatRollSvg(
        "tobylai的小屋",
        "parrot.png",
        "https://www.bilibili.com/video/BV1uT4y1P7CX",
        10,29
))
# imageUtils.svg2jpg("res.svg","res.jpg")