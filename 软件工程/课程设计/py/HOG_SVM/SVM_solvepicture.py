import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt


# 本文件提供对图像进行各种处理的函数

# 算法1: 对比度增强
def contrast_enhancement(image, alpha=1.5, beta=10):
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return enhanced_image


# 算法2: 直方图均衡化
def histogram_equalization(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    equalized_image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return equalized_image


# 算法3: 颜色增强
def color_enhancement(image, alpha=1.2, beta=10):
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return enhanced_image


# 算法4: 锐化
def sharpening(image, alpha=1.5):
    kernel = np.array([[-1, -1, -1], [-1, 9 + alpha, -1], [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image


# 算法5: 去噪
def denoising(image, strength=10):
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, strength, strength, 7, 21)
    return denoised_image


# 算法6: 多尺度 Retinex
def multi_scale_retinex(image, sigma_list=[15, 80, 250]):
    retinex = np.zeros_like(image)
    for sigma in sigma_list:
        retinex += np.log1p(image.astype(np.float32)) - np.log1p(cv2.GaussianBlur(image, (0, 0), sigma))
    retinex = (retinex / len(sigma_list)).astype(np.uint8)
    return retinex


# 算法7: 伽马校正
def gamma_correction(image, gamma=1.5):
    gamma_corrected = np.clip((image / 255.0) ** gamma * 255.0, 0, 255).astype(np.uint8)
    return gamma_corrected


# 算法8: 形态学变换
def morphological_transform(image, operation=cv2.MORPH_CLOSE, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    transformed_image = cv2.morphologyEx(image, operation, kernel)
    return transformed_image


# 算法9: 边缘增强
def edge_enhancement(image, sigma=1.0):
    blurred_image = cv2.GaussianBlur(image, (0, 0), sigma)
    edge_enhanced = cv2.addWeighted(image, 2.0, blurred_image, -1.0, 0)
    return edge_enhanced


# 算法10: 自适应对比度增强
def adaptive_contrast_enhancement(image, clip_limit=3.0, tile_size=8):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_size, tile_size))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    enhanced_image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return enhanced_image


# 算法11: 频域滤波
def frequency_domain_filter(image, filter_type="lowpass", d0=30):
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    if filter_type == "lowpass":
        mask[crow - d0:crow + d0, ccol - d0:ccol + d0] = 1
    elif filter_type == "highpass":
        mask[:crow - d0, :] = 1
        mask[crow + d0:, :] = 1
        mask[:, :ccol - d0] = 1
        mask[:, ccol + d0:] = 1

    f_shift = f_shift * mask
    f_ishift = np.fft.ifftshift(f_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back


# 算法12: 色彩空间转换
def color_space_conversion(image, conversion=cv2.COLOR_BGR2GRAY):
    converted_image = cv2.cvtColor(image, conversion)
    return converted_image


# 算法13: 霓虹效果
def neon_effect(image):
    neon = cv2.GaussianBlur(image, (21, 21), 0)
    neon = cv2.addWeighted(image, 1.5, neon, -0.5, 0)
    return neon


# 算法14: 卡通效果
def cartoon_effect(image, d=9, sigmaColor=9, sigmaSpace=7):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

    color = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


# 算法15: 油画效果
def oil_painting_effect(image, size=5, dynRatio=0.7):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
    _, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    oil = cv2.xphoto.createOilPaintingFilter(dynRatio=dynRatio, size=size)
    oil_painting = oil.filter(image, mask)
    return oil_painting


# 主函数
def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Advanced Image Enhancement Algorithms")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("output_image", help="Path to save the output image")
    parser.add_argument("--contrast", action="store_true", help="Apply contrast enhancement")
    parser.add_argument("--histeq", action="store_true", help="Apply histogram equalization")
    parser.add_argument("--coloren", action="store_true", help="Apply color enhancement")
    parser.add_argument("--sharpen", action="store_true", help="Apply image sharpening")
    parser.add_argument("--denoise", action="store_true", help="Apply denoising")
    parser.add_argument("--retinex", action="store_true", help="Apply multi-scale Retinex")
    parser.add_argument("--gamma", action="store_true", help="Apply gamma correction")
    parser.add_argument("--morph", action="store_true", help="Apply morphological transformation")
    parser.add_argument("--edge", action="store_true", help="Apply edge enhancement")
    parser.add_argument("--adaptive_contrast", action="store_true", help="Apply adaptive contrast enhancement")
    parser.add_argument("--freq_filter", action="store_true", help="Apply frequency domain filtering")
    parser.add_argument("--freq_filter_type", default="lowpass", choices=["lowpass", "highpass"],
                        help="Frequency domain filter type")
    parser.add_argument("--freq_filter_d0", type=int, default=30, help="Cutoff frequency for frequency domain filter")
    parser.add_argument("--color_conversion", action="store_true", help="Apply color space conversion")
    parser.add_argument("--neon_effect", action="store_true", help="Apply neon effect")
    parser.add_argument("--cartoon_effect", action="store_true", help="Apply cartoon effect")
    parser.add_argument("--oil_painting_effect", action="store_true", help="Apply oil painting effect")

    args = parser.parse_args()

    # 读取输入图像
    image = cv2.imread(args.input_image)

    # 应用选定的算法
    if args.contrast:
        image = contrast_enhancement(image)

    if args.histeq:
        image = histogram_equalization(image)

    if args.coloren:
        image = color_enhancement(image)

    if args.sharpen:
        image = sharpening(image)

    if args.denoise:
        image = denoising(image)

    if args.retinex:
        image = multi_scale_retinex(image)

    if args.gamma:
        image = gamma_correction(image)

    if args.morph:
        image = morphological_transform(image)

    if args.edge:
        image = edge_enhancement(image)

    if args.adaptive_contrast:
        image = adaptive_contrast_enhancement(image)

    if args.freq_filter:
        image = frequency_domain_filter(image, args.freq_filter_type, args.freq_filter_d0)

    if args.color_conversion:
        image = color_space_conversion(image)

    if args.neon_effect:
        image = neon_effect(image)

    if args.cartoon_effect:
        image = cartoon_effect(image)

    if args.oil_painting_effect:
        image = oil_painting_effect(image)

    # 显示和保存处理后的图像
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Enhanced Image')
    plt.subplot(1, 2, 2), plt.hist(image.ravel(), 256, [0, 256]), plt.title('Histogram')
    plt.show()

    cv2.imwrite(args.output_image, image)
    print(f"Output image saved at {args.output_image}")


if __name__ == "__main__":
    main()
