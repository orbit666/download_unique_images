import requests
import os
import time
import hashlib

def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def get_image_hash(image_bytes):
    return hashlib.md5(image_bytes).hexdigest()

def download_unique_images(url, save_path, max_attempts=1000, delay=0.5):
    create_directory(save_path)
    hash_set = set()
    saved_count = 0

    for i in range(1, max_attempts + 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
                image_data = response.content
                img_hash = get_image_hash(image_data)

                if img_hash not in hash_set:
                    ext = response.headers["Content-Type"].split("/")[-1]
                    filename = f"image_{saved_count:03d}.{ext}"
                    filepath = os.path.join(save_path, filename)
                    with open(filepath, "wb") as f:
                        f.write(image_data)

                    hash_set.add(img_hash)
                    saved_count += 1
                    print(f"[{i}/{max_attempts}] ✅ 新图片已保存：{filename}")
                else:
                    print(f"[{i}/{max_attempts}] ⚠️ 重复图片，跳过")
            else:
                print(f"[{i}/{max_attempts}] ⚠️ 非图片内容，跳过")
        except Exception as e:
            print(f"[{i}/{max_attempts}] ❌ 出错: {e}")
        
        time.sleep(delay)

    print(f"\n🎉 下载完成！共保存唯一图片 {saved_count} 张\n")

if __name__ == "__main__":
    IMAGE_URL = "https://www.loliapi.com/acg/pc/"  #设置随机api的网址
    SAVE_DIR = "unique_images" #目录
    ATTEMPTS = 1000   # 可调成你想要的尝试次数（例如 5000）
    DELAY_SEC = 0.5   # 每次请求间隔时间（秒）

    download_unique_images(IMAGE_URL, SAVE_DIR, ATTEMPTS, DELAY_SEC)
