import os
import glob
import shutil

home = "D:\FB-PRO"
feature_dir = os.path.join(home, "features_ocr")
image_dir_mask = os.path.join(home, "img_mask")
copy_dir = os.path.join(home, "copy")

features = glob.glob(os.path.join(feature_dir, '*_info.npy'))
features += glob.glob(os.path.join(feature_dir, '**', '*_info.npy'))
features = [i.split('\\')[3][0:5] for i in list(features)]

images_mask = glob.glob(os.path.join(image_dir_mask, '*.png'))
images_mask += glob.glob(os.path.join(image_dir_mask, '**', '*.png'))
images_mask = [i.split('\\')[3][0:5] for i in list(images_mask)]

res = []
for img in images_mask:
    if img not in features:
        res.append(img)

# print(len(res))

def copy_search_file(srcDir, desDir):
    ls = os.listdir(srcDir)
    for line in ls:
        if line[0:5] in res:
            filePath = os.path.join(srcDir, line)
            if os.path.isfile(filePath):
                # print(filePath)
                shutil.copy(filePath, desDir)

copy_search_file(image_dir_raw, copy_dir)