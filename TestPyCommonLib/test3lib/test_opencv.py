# pip uninstall opencv-python-headless
# pip install opencv-python
import cv2

# # 打开视频流（摄像头）
# cap = cv2.VideoCapture(0)
#
# cap = cv2.VideoCapture(r"D:\opt\test.mp4")
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # 显示结果帧
#     cv2.imshow('Scanner', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # 按'q'键退出循环
#         break


# 识别二维码
image = cv2.imread(r'D:\opt\test.jpg')

# 检查图像信息
print(f"图像类型: {type(image)}")
print(f"图像形状: {image.shape}")
print(f"图像数据类型: {image.dtype}")

# 初始化二维码检测器
qr_decoder = cv2.QRCodeDetector()
# 检测二维码
data, bbox, _ = qr_decoder.detectAndDecode(image)

if data:
    print("检测到二维码：", data)

