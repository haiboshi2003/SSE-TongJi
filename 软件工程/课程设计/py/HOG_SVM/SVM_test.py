import cv2
import SVM_predict
from PIL import Image

# 本程序用来测试 SVM检测模块 的最终执行效果
# 主要是测试接口函数 SVM_detect(image) 是否工作正常

if __name__ == "__main__":
    img = input('Input image filename:')
    image = Image.open(img)
    r_image = SVM_predict.SVM_detect(image)
    cv2.imshow('Detection', r_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# F:\0大三上\软件工程\课程设计_土木合作项目\课程设计_目前选定的算法\crack-detector_2.0\test_image\new.jpg
