import argparse
import os
from os.path import join as os_join
import cv2 as cv
import numpy as np
from data_utils import test, img_source_init, animpath_dict_init, anim_dict_init
from detector import feature_calculate, mark_match, animate_fetch, animate_display
import logging
import copy
logger = logging.getLogger(__name__)


def main_loop(img_src, animpath_dict, anim_dict):
    animation_list = []
    prevMD = None
    prevAL = None

    while img_src.isOpened():
        success, img = img_src.read()
        if success:
            # step 1: calculate mark features
            feature_list = feature_calculate(img)

            # step 2: match mark using feature patterns
            mark_dict = mark_match(img, feature_list)
            if prevMD == None:
                prevMD = copy.deepcopy(mark_dict)

            if len(mark_dict["markerCorners"]) < 4:
                mark_dict = prevMD
            else:
                prevMD = copy.deepcopy(mark_dict)

            # step 3: fetch corresponding animation using marks
            animation_list = animate_fetch(mark_dict, animpath_dict, anim_dict)
            if prevAL == None:
                prevAL = copy.deepcopy(animation_list)

            if len(mark_dict["markerCorners"]) < 4:
                animation_list = prevAL
            else:
                prevAL = copy.deepcopy(animation_list)

            # step 4: draw new image, replace the patch.
            img_animated = animate_display(img, mark_dict, animation_list)

            cv.imshow("Result", img_animated)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    cv.destroyAllWindows()


def main(args):
    proj_path = args.proj_path
    test_path = args.test_path
    animation_folder = os_join(test_path, 'test_fixture')
    mark_type = args.mark_type
    source_type = args.source_type

    # init image source
    img_src = img_source_init(source_type)

    # init match_dict,
    # which is the map from arUco markerId to the animation file
    animpath_dict = animpath_dict_init(animation_folder)

    # init capture dictionary,
    # which keeps track of the current video frame
    anim_dict = anim_dict_init(animpath_dict)

    # into loop
    main_loop(img_src, animpath_dict, anim_dict)

    # dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
    # for i in range(1, 21):
    #     markerImage = np.zeros((500, 500), dtype=np.uint8)
    #     markerImage = cv.aruco.drawMarker(dictionary, i, 200, markerImage, 1)
    #     cv.imwrite( os_join(test_path, f'marker{i}.png'), markerImage)


if __name__ == '__main__':

    file_path = os.path.dirname(os.path.abspath(__file__))
    proj_path = os.path.dirname(file_path)
    test_path = os_join(proj_path, 'test')

    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=str, help='Number of')
    parser.add_argument('--source_type', type=str,
                        help='The source type of img {camera, file, ...}', default='camera')
    parser.add_argument('--mark_type', type=str,
                        help='The feature type of mark {aruco, surf, ...}', default='aruco')
    parser.add_argument('--filepath', type=str,
                        help='The path of the file/network source video', default="")
    # parser.add_argument('--is_markless', action='store_true', default=False,)

    ############################
    # CONFIGURE ARGUMENTS HERE #
    ############################
    args = parser.parse_args()
    args.proj_path = proj_path
    args.test_path = test_path
    print(args)

    main(args)
