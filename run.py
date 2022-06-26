import os
import sys
import matplotlib.pyplot as plt
from tf_pose import common
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def pose_estimate(image_path):
    image = common.read_imgfile(image_path, None, None)
    if image is None:
        print("NO Image found")
        sys.exit(-1)
    else:
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
        return image


if __name__ == '__main__':

    w,h = 432,368

    e = TfPoseEstimator(get_graph_path('mobilenet_v2_small'), target_size=(w, h))

    # estimate human poses from a single image !
    image = pose_estimate('./images/ski.jpg')
    try:

        fig = plt.figure()
        a = fig.add_subplot(3, 1, 1)
        a.set_title('Result')

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        image = pose_estimate('./images/p1.jpg')
        a = fig.add_subplot(3, 1, 2)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        image = pose_estimate('./images/p3_dance.png')
        a = fig.add_subplot(3, 1, 3)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        image = pose_estimate('./images/COCO_val2014_000000000357.jpg')
        a = fig.add_subplot(4, 1, 4)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # bgimg = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_BGR2RGB)
        # bgimg = cv2.resize(bgimg, (e.heatMat.shape[1], e.heatMat.shape[0]), interpolation=cv2.INTER_AREA)

        # # show network output
        # a = fig.add_subplot(2, 2, 2)
        # plt.imshow(bgimg, alpha=0.5)
        # tmp = np.amax(e.heatMat[:, :, :-1], axis=2)
        # plt.imshow(tmp, cmap=plt.cm.gray, alpha=0.5)
        # plt.colorbar()

        # tmp2 = e.pafMat.transpose((2, 0, 1))
        # tmp2_odd = np.amax(np.absolute(tmp2[::2, :, :]), axis=0)
        # tmp2_even = np.amax(np.absolute(tmp2[1::2, :, :]), axis=0)

        # a = fig.add_subplot(2, 2, 3)
        # a.set_title('Vectormap-x')
        # # plt.imshow(CocoPose.get_bgimg(inp, target_size=(vectmap.shape[1], vectmap.shape[0])), alpha=0.5)
        # plt.imshow(tmp2_odd, cmap=plt.cm.gray, alpha=0.5)
        # plt.colorbar()

        # # a = fig.add_subplot(2, 2, 4)
        # a.set_title('Vectormap-y')
        # # plt.imshow(CocoPose.get_bgimg(inp, target_size=(vectmap.shape[1], vectmap.shape[0])), alpha=0.5)
        # plt.imshow(tmp2_even, cmap=plt.cm.gray, alpha=0.5)
        # plt.colorbar()
        plt.show()
    except Exception as e:
        cv2.imshow('result', image)
        cv2.waitKey()
