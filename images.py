from PIL import Image
import numpy as np
import os
import time


def image(sta, end, depths=10):
    a = np.asarray(Image.open(sta).convert('L')).astype('float')
    depth = depths  # 深度的取值范围(0-100)，标准取10
    grad = np.gradient(a)  # 取图像灰度的梯度值
    grad_x, grad_y = grad  # 分别取横纵图像梯度值
    grad_x = grad_x * depth / 100.  # 对grad_x值进行归一化
    grad_y = grad_y * depth / 100.  # 对grad_y值进行归一化
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A
    vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.  # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
    dz = np.sin(vec_el)  # 光源对z 轴的影响
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    b = b.clip(0, 255)
    im = Image.fromarray(b.astype('uint8'))  # 重构图像
    im.save(end)


def main():
    xs = 10
    count = 0
    start_time = time.clock()
    startss = os.listdir(r"C:\Users\Administrator\Desktop\gugong")
    time.sleep(2)
    for starts in startss:
        start = ''.join(starts)
        count = count + 1
        sta = 'C:/Users/Administrator/Desktop/gugong/' + start
        end = 'C:/Users/Administrator/Desktop/gugong/' + 'HD_' + start
        image(sta=sta, end=end, depths=xs)

    end_time = time.clock()
    print("一共" + str(count) + "张图片！" + '\n程序运行了' + str(end_time - start_time) + '   秒')
    time.sleep(3)


main()
