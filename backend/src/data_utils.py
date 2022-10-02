"""
The utility functions for image/video streaming
"""
import numpy as np
import cv2 as cv
from typing import List
import logging
logger = logging.getLogger(__name__)


def test(t: str) -> List:
    """The test function for image/video streaming
    Args:
        t (str): input string to
    Returns:
        List: multiple input string for 3 times
    """

    return [t]*3


def img_source_init(source_type: str, path: str = None):
    # fetch img from video stream/path
    # return the obj for fetch video in buffer.
    logging.info(f'Image Source: {source_type}')
    if source_type == "camera":
        return _img_init_camera()
    if source_type == "file":
        return _img_init_file(path)


def _img_init_camera(device_id: int = 0, frameWidth: int = 320, frameHeight: int = 240):
    cap = cv.VideoCapture(device_id)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    # cap.set(10,150)
    return cap


def _img_init_file(path: str, frameWidth: int = 320, frameHeight: int = 240):
    cap = cv.VideoCapture(path)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    return cap


def animpath_dict_init(animation_folder: str):
    # map the arUco markerId to an animation
    # TODO: read mapping from file
    animpath_dict = {
        (1, 2, 3, 4): f'{animation_folder}/roc.mp4',
        (5, 6, 7, 8): f'{animation_folder}/final.mp4'
    }
    return animpath_dict


def anim_dict_init(animpath_dict):
    anim_dict = {}
    for key, _ in animpath_dict.items():
        anim_dict[key] = cv.VideoCapture(animpath_dict[key])

    return anim_dict
