import cv2
import imutils
import joblib
import numpy as np
from PIL import Image
from imutils.object_detection import non_max_suppression
from skimage.feature import hog
from skimage.transform import pyramid_gaussian
import SVM_EdgeDetection
import SVM_solvepicture


# 本文件主要实现了SVM检测的主要功能部分
# 并提供了接口函数 SVM_detect(image) 以便调用

def pred(image, model_path="weights/models.dat"):
    print("SVM：开始识别")
    setwidth = min(800, max(400, image.shape[1]))
    setheight = min(1200, max(600, image.shape[0]))
    # image = cv2.resize(image, (256, 256))
    image = imutils.resize(image, width=setwidth, height=setheight)
    image_copy = image  # 保存一份原图的副本

    # 进行边缘检测
    print("SVM：边缘检测")

    print("image.shape: ", image.shape)

    smoothed_image = SVM_EdgeDetection.smooth(image)

    gradients, direction = SVM_EdgeDetection.get_gradient_and_direction(smoothed_image)

    nms = SVM_EdgeDetection.NMS(gradients, direction)

    image = SVM_EdgeDetection.double_threshold(nms, 40, 100)

    # cv2.imshow('edge', image)
    # cv2.waitKey(0)

    size = (200, 250)  # 指的是min_window_size

    step_size = (round(setwidth / 40), round(setheight / 60))
    downscale = 1.25

    # List to store the detections
    detections = []

    # The current scale of the image

    def sliding_window(image, window_size, step_size):
        for y in range(0, image.shape[0], step_size[1]):
            for x in range(0, image.shape[1], step_size[0]):
                yield x, y, image[y: y + window_size[1], x: x + window_size[0]]

    model = joblib.load(model_path)  # 指定用于svm检测的模型
    scale = 0

    print("SVM：开始滑动窗口检测")
    for im_scaled in pyramid_gaussian(image, downscale=downscale):
        # The list contains detections at the current scale
        if im_scaled.shape[0] < size[1] or im_scaled.shape[1] < size[0]:
            break
        for (x, y, window) in sliding_window(im_scaled, size, step_size):
            if window.shape[0] != size[1] or window.shape[1] != size[0]:
                continue

            fd = hog(window, orientations=9, pixels_per_cell=(8, 8), visualize=False, cells_per_block=(3, 3))
            fd = fd.reshape(1, -1)
            pred = model.predict(fd)
            if pred == 1:

                if model.decision_function(fd) > 0.8:
                    detections.append(
                        (int(x * (downscale ** scale)), int(y * (downscale ** scale)), model.decision_function(fd),
                         int(size[0] * (downscale ** scale)),
                         int(size[1] * (downscale ** scale))))

        scale += 1

    clone = image_copy
    rects = np.array([[x, y, x + w, y + h] for (x, y, _, w, h) in detections])
    sc = [score[0] for (x, y, score, w, h) in detections]
    print("sc: ", sc)
    sc = np.array(sc)
    print("SVM：非极大值抑制")
    pick = non_max_suppression(rects, probs=sc, overlapThresh=0.5)
    for (x1, y1, x2, y2) in pick:
        cv2.rectangle(clone, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(clone, 'crack', (x1 - 2, y1 - 2), 1, 2.5, (0, 255, 0), 3)

    print("SVM：准备检测结果")
    if np.size(sc) == 0:
        # 获取图像的宽高
        height, width = image.shape[:2]
        # 设置要放置的文本内容
        text = 'No crack'
        # 设置字体、比例尺寸、颜色、线宽等参数
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2.5
        font_thickness = 3
        textcolor = (0, 255, 0)
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        # 计算文本放置位置在图片中心
        text_x = int((width - text_size[0]) / 2)
        text_y = int((height + text_size[1]) / 2)
        # 在图片上放置文本
        cv2.putText(clone, text, (text_x, text_y), font, font_scale, textcolor, font_thickness)

    print("SVM：识别结束")

    return clone


def SVM_detect(image, model_path='weights/models.dat'):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    print("SVM：读取原始图像")
    r_image = pred(image, model_path)
    print("SVM：返回结果图像")
    return r_image


def SVM_detect_default(img_path='..\\data\\test1.jpg', save=1, save_path="..\\detect\\exp\\svmresult.jpg",
                       model_path='weights/models.dat'):
    # image = Image.open('F:\\0大三上\\软件工程\\课程设计_土木合作项目\\课程设计_目前选定的算法\\crack-detector_2.0\\test_image\\new.jpg')
    image = Image.open(img_path)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    print("SVM：读取原始图像")
    r_image = pred(image, model_path)
    if save:
        print("SVM：保存检测结果")
        image_to_save = Image.fromarray(np.uint8(r_image))
        # save_path = "..\\detect\\exp\\svmresult.jpg"
        # 保存图像到指定路径
        image_to_save.save(save_path)
    print("SVM：返回结果图像")
    return r_image


# 下面测试一下默认接口函数 SVM_detect_default() 的效果
if __name__ == "__main__":
    r_image = SVM_detect_default()
    cv2.imshow('Detection', r_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 测试图片名称
# F:\0大三上\软件工程\课程设计_土木合作项目\课程设计_目前选定的算法\crack-detector_2.0\test_image\new.jpg
