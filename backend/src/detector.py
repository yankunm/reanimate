import cv2 as cv
import numpy as np


def feature_calculate(img):
    # Given the frame, calculate features
    dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
    parameters = cv.aruco.DetectorParameters_create()
    markerCorners, markerIds, rejectedCandidates = cv.aruco.detectMarkers(
        img, dictionary, parameters=parameters)
    print('markerCorners', markerCorners)
    print('markerIds', markerIds)
    # print('rejectedCandidates', rejectedCandidates)
    res_dict = {
        'markerCorners': markerCorners,
        'markerIds': markerIds,
        'rejectedCandidates': rejectedCandidates,
    }
    return res_dict


def mark_match(img, feature_list):
    # Given the feature, match markers return the match ID
    return feature_list


def animate_fetch(mark_dict, animpath_dict, anim_dict):
    # given the match ID, fetch the animation data
    # match for lenna
    animate_list = []
    # print(animation_folder)

    if (mark_dict['markerIds'] is None):
        return animate_list

    marker_id = list(np.concatenate(mark_dict['markerIds']).flat)
    marker_id = tuple(sorted(marker_id))
    if (marker_id not in anim_dict.keys()):
        return animate_list

    success, im = anim_dict[marker_id].read()
    if (not success):
        # restart the animation
        anim_dict[marker_id].release()
        anim_dict[marker_id] = cv.VideoCapture(animpath_dict[marker_id])
        success, im = anim_dict[marker_id].read()

    animate_list.append(im)

    return animate_list



def animate_display(img, mark_dict, animation_list):
    # print(mark_dict)

    if len(animation_list) == 0:
        return img 
    # given the animate data, generate synthesized image (AR)
    img_animation = animation_list.pop()

    height, width, depth = img_animation.shape
    pts_src = np.array(
        [
            [0, 0],  # Top left
            [width-1, 0],  # Top right
            [width-1, height-1],  # bottom right
            [0, height-1],  # bottom left
        ]
    ).astype(int)

    markerCorners = mark_dict['markerCorners']
    if mark_dict['markerIds'] is None:
        return img

    markerIds = mark_dict['markerIds'].flatten()

    refPts = []

    if len(markerCorners) == 4:
        for i in np.sort(markerIds).tolist():
            j = np.squeeze(np.where(markerIds == i))
            corner = np.squeeze(markerCorners[j])
            print(corner)
            refPts.append(corner)

        # refPts = np.sort(markerIds).tolist()
        # unpack our ArUco reference points and use the reference points to
        # define the *destination* transform matrix, making sure the points
        # are specified in top-left, top-right, bottom-right, and bottom-left
        # order
        (refPtTL, refPtTR, refPtBR, refPtBL) = refPts
        dstMat = [refPtTL[0], refPtTR[1], refPtBR[2], refPtBL[3]]
        dstMat = np.array(dstMat)
        # grab the spatial dimensions of the source image and define the
        # transform matrix for the *source* image in top-left, top-right,
        # bottom-right, and bottom-left order
        # (srcH, srcW) = img.shape[:2]
        # srcMat = np.array([[0, 0], [srcW, 0], [srcW, srcH], [0, srcH]])
        # compute the homography matrix and then warp the source image to the
        # destination based on the homography

        # Calculate Homography
        h, status = cv.findHomography(pts_src, dstMat)

        # Warp source image to destination based on homography
        warped_image = cv.warpPerspective(
            img_animation, h, (img.shape[1], img.shape[0]))

        # Prepare a mask representing region to copy from the warped image into the original frame.
        mask = np.zeros([img.shape[0], img.shape[1]], dtype=np.uint8)
        cv.fillConvexPoly(mask, np.int32(dstMat), (255, 255, 255), cv.LINE_AA)

        # Erode the mask to not copy the boundary effects from the warping
        element = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        mask = cv.erode(mask, element, iterations=3)

        # Copy the mask into 3 channels.
        warped_image = warped_image.astype(float)
        mask3 = np.zeros_like(warped_image)
        for i in range(0, 3):
            mask3[:, :, i] = mask/255

        # Copy the masked warped image into the original frame in the mask region.
        warped_image_masked = cv.multiply(warped_image, mask3)
        frame_masked = cv.multiply(img.astype(float), 1-mask3)
        im_out = cv.add(warped_image_masked, frame_masked)
        return im_out.astype(np.uint8)

    return img
