import cv2
import glob
import joblib
import numpy as np
import os
from skimage.feature import hog
from sklearn.svm import LinearSVC

# 本程序用于使用已经准备好的数据集neg和pos，训练支持向量机模型


train_data = []
train_labels = []
pos_im_path = 'data/pos/'  # pos训练集的路径，现在是本HOG_SVM文件夹下的data文件夹
neg_im_path = 'data/neg/'  # neg训练集的路径
model_path = 'weights/models1.dat'  # 模型保存的路径
# Load the positive features
for filename in glob.glob(os.path.join(pos_im_path, "*.jpg")):
    fd = cv2.imread(filename, 0)
    fd = hog(fd, orientations=9, pixels_per_cell=(8, 8), visualize=False, cells_per_block=(3, 3))
    train_data.append(fd)
    train_labels.append(1)

# Load the negative features
for filename in glob.glob(os.path.join(neg_im_path, "*.jpg")):
    fd = cv2.imread(filename, 0)
    fd = hog(fd, orientations=9, pixels_per_cell=(8, 8), visualize=False, cells_per_block=(3, 3))
    train_data.append(fd)
    train_labels.append(-1)

train_data = np.float32(train_data)
train_labels = np.array(train_labels)
print('Data Prepared........')
print('Train Data:', len(train_data))
print('Train Labels (1,-1)', len(train_labels))
print('Classification with SVM')

model = LinearSVC()
print('Training...... Support Vector Machine')
model.fit(train_data, train_labels)
joblib.dump(model, model_path)
print('Model saved : {}'.format(model_path))
