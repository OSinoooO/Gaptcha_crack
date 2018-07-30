from PIL import Image
import tesserocr, requests

# 图片下载链接
image_url = 'http://my.cnki.net/elibregister/CheckCode.aspx'
# 图片保存路径
image_path = 'image/captcha.jpg'

def image_download():
    """
    图片下载
    """
    response = requests.get(image_url)
    with open(image_path, 'wb') as f:
        f.write(response.content)

def get_image():
    """
    用Image获取图片文件
    :return: 图片文件
    """
    image = Image.open(image_path)
    return image

def image_grayscale_deal(image):
    """
    图片转灰度处理
    :param image:图片文件
    :return: 转灰度处理后的图片文件
    """
    image = image.convert('L')
    return image

def image_thresholding_method(image):
    """
    图片二值化处理
    :param image:转灰度处理后的图片文件
    :return: 二值化处理后的图片文件
    """
    # 阈值
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 图片二值化，此处第二个参数为数字一
    image = image.point(table, '1')
    return image


def captcha_tesserocr_crack(image):
    """
    图像识别
    :param image: 二值化处理后的图片文件
    :return: 识别结果
    """
    image.show()
    result = tesserocr.image_to_text(image)
    return result


if __name__ == '__main__':
    image_download()
    image = get_image()
    img1 = image_grayscale_deal(image)
    img2 = image_thresholding_method(img1)
    print(captcha_tesserocr_crack(img2))
