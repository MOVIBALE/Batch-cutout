import os
from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def select_folder():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

def start_rembg():
    # 获取输入文件夹路径
    input_folder = folderPath.get()
    # 设置输出文件夹路径，并确保文件夹存在
    output_folder = os.path.join(input_folder, 'rembg_output')
    os.makedirs(output_folder, exist_ok=True)
    # 获取所有扩展名为 .png、.jpg 或 .jpeg 的图片文件列表
    images = [f for f in os.listdir(input_folder) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
    # 计算图片数量
    num_images = len(images)
    # 将进度条最大值设置为图片数量
    progress_bar.configure(maximum=num_images)
    # 对于每张图片，执行以下操作：
    for i, image_name in enumerate(images):
        # 获取图片路径
        input_path = os.path.join(input_folder, image_name)
        # 打开图片并进行背景移除
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        # 保存处理后的图片到输出文件夹
        output_path = os.path.join(output_folder, image_name)
        output_image.save(output_path)
        # 更新进度条并刷新窗口
        progress_bar.step(1)
        window.update()

# 创建GUI窗口
window = tk.Tk()
window.title("批量抠图")

# 创建输入文件夹选择按钮
folderPath = tk.StringVar()
select_folder_button = tk.Button(text="选择文件夹", command=select_folder)
select_folder_button.pack()

# 创建开始按钮
start_button = tk.Button(text="开始", command=start_rembg)
start_button.pack()

# 创建进度条
progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=200)
progress_bar.pack()

window.mainloop()