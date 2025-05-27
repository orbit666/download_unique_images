# download_unique_images
随机api图片下载



对代码中下面的设置，可以改成自己想要下载的网址
    IMAGE_URL = "https://img.loliapi.cn/i/pc/img385.webp"  #设置随机api的网址
    SAVE_DIR = "unique_images" #目录
    ATTEMPTS = 1000   # 可调成你想要的尝试次数（例如 5000）
    DELAY_SEC = 0.5   # 每次请求间隔时间（秒）
使用方法


安装 Python；
将代码保存为 download_unique_images.py；
终端中运行：
bash
复制
编辑
python download_unique_images.py
