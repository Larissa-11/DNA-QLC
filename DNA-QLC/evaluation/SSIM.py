import cv2
import numpy as np


def ssim(img1, img2):
    C1 = (0.01 * 255) ** 2
    C2 = (0.03 * 255) ** 2
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())
    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1 ** 2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2 ** 2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def calculate_ssim(img1, img2):
    '''calculate SSIM
  the same outputs as MATLAB's
  img1, img2: [0, 255]
  '''
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')


img1 = cv2.imread("../images/Mona Lisa.jpg", 0)
ss_all = []
for iteration in range(0,10,1):
    str_i = str(iteration)
    input_path = "../Data/new/error2/" + "Yin-Yang" + str_i + ".jpg"
    # input_path = "../Data/new/error2/" + "Grass" + str_i + ".jpg"
    img2 = cv2.imread(input_path, 0)
    ss = calculate_ssim(img1, img2)
    ss_all.extend([ss])
    print(str_i+"SSIM:%.3f" %(ss))
print("平均数:%.3f" %(np.mean(ss_all)))

# input_path = "../Data/compression/ReButterfly.JPEG"
# img2 = cv2.imread(input_path, 0)
# ss = calculate_ssim(img1, img2)
# print("SSIM:%.3f" %(ss))