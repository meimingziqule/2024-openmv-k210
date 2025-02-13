import sensor
import image
import time

# 初始化摄像头
sensor.reset()
sensor.set_pixformat(sensor.RGB565)  # 使用灰度图像
sensor.set_framesize(sensor.QVGA)       # 设置图像大小为QVGA (320x240)
sensor.skip_frames(time=2000)           # 等待摄像头稳定
set_window_flag = 1
# 设置阈值，用于检测黑色色块
threshold = (0, 10, -128, 127, -128, 127)  # 黑色阈值

while(True):
    # 获取图像
    img = sensor.snapshot()

    # 寻找黑色色块
    blobs = img.find_blobs([threshold], pixels_threshold=100, area_threshold=100)
    if set_window_flag == 1:
        if blobs:
            # 找到最大的黑色色块
            largest_blob = max(blobs, key=lambda b: b.pixels())
    
            # 获取外接框的坐标
            x, y, w, h = largest_blob.x(), largest_blob.y(), largest_blob.w(), largest_blob.h()
    
            # 设置窗口
            sensor.set_windowing((x, y, w, h))
            set_window_flag = 0
            # 在图像上绘制外接框
            img.draw_rectangle(x, y, w, h, color=255)