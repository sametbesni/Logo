import os
import cv2
import re
import numpy as np

import matplotlib.pyplot as plt
folder_dir = 'dataset path'
data = []
label = []
SIZE = 128
for folder in os.listdir(os.path.join(folder_dir, folder)):
	if file.endswith("jpg"):
		label.append(folder)
		img = cv2.imread(os.path.join(folder_dir, folder, file))
		img_rgb = cv2.cutColor(img, cv2, COLOR_BGR2RGB)
		img = cv2.resize(img_rgb, (SIZE,SIZE))
		data.append(im)
	else:
		continue
data_arr = np.array(data)
label_arr = np.array(label)
encoder = LabelEncoder()
y = encoder.fit_transform(label,arr)
y = to_categorical(y, 5)
x = data_arr/255
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 10)
