import numpy as np
arr_img = np.zeros((150, 200), np.uint8)
_img_100 = arr_img.copy(); _img_100[:, :] = 100 # gray 100
_img_200 = arr_img.copy(); _img_200[:, :] = 200 # gray 180
_img_255 = arr_img.copy(); _img_255[:, :] = 255 # gray 255

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 4); axes[0].set_title("arr_img")
axes[0].imshow(arr_img, cmap='gray', vmin=0, vmax=255)
axes[1].set_title("_img_100")
axes[1].imshow(_img_100, cmap='gray', vmin=0, vmax=255)
axes[2].set_title("_img_200")
axes[2].imshow(_img_200, cmap='gray', vmin=0, vmax=255)
axes[3].set_title("_img_255")
axes[3].imshow(_img_255, cmap='gray', vmin=0, vmax=255)
plt.show()