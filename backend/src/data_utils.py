"""
The utility functions for image/video streaming
"""
import numpy as np
import cv2 as cv
from typing import List
import logging
logger = logging.getLogger(__name__)

def test(t:str) -> List:
    """The test function for image/video streaming

    Args:
        t (str): input string to

    Returns:
        List: multiple input string for 3 times
    """
    
    return [t]*3


def img_source_init(source_type:str):
    # fetch img from video stream/path
    # return the obj for fetch video in buffer.
    logging.info(f'Image Source: {source_type}')
    if source_type == "camera":
        return _img_int_camera()
    


def _img_int_camera(device_id: int = 0, frameWidth:int = 320, frameHeight:int = 240):
    cap = cv.VideoCapture(device_id)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    # cap.set(10,150)
    return cap

    

