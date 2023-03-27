import http.server
import socketserver
import os


def img_to_url(path):
    # 定义图片和链接的URL
    img_path = path
    # 使用Python生成HTML代码
    html = "<img src='{}' />".format(img_path)
    # 将HTML代码写入一个HTML文件
    with open("local_image_link.html", "w") as f:
        f.write(html)
    # 创建本地Web服务器

    # 打开生成的HTML文件
    os.system("open local_image_link.html")

    return url