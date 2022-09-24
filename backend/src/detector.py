import cv2 as cv
import numpy as np 




def feature_calculate(img):
    # Given the frame, calculate features
    
    dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
    parameters =  cv.aruco.DetectorParameters_create()
    markerCorners, markerIds, rejectedCandidates = cv.aruco.detectMarkers(img, dictionary, parameters=parameters)
    print('markerCorners', markerCorners)
    print('markerIds', markerIds)
    # print('rejectedCandidates', rejectedCandidates)
    res_dict = {
        'markerCorners': markerCorners, 
        'markerIds': markerIds, 
        'rejectedCandidates':rejectedCandidates,
    }
    return res_dict

def mark_match(img, feature_list):
    # Given the feature, match markers return the match ID
    return feature_list

def animate_fetch(mark_list, animation_folder):
    # I/O bound warning
    # given the match ID, fetch the animation data
    # match for lenna
    animate_list = []
    print(animation_folder)
    
    # im = cv.imread(f'{animation_folder}/lenna.png', cv.IMREAD_UNCHANGED)
    cap = cv.VideoCapture(f'{animation_folder}/func.mp4')
    success, im = cap.read()
    while (success):
        animate_list.append(im)
        success, im = cap.read()
    
    return animate_list
def animate_display(img, mark_dict, animation_list):
    # given the animate data, generate synthesized image (AR)
    img_animation = animation_list.pop()
    
    
    height, width, depth = img_animation.shape
    pts_src = np.array(
        [
            [0, 0], # Top left
            [width-1, 0],# Top right
            [width-1, height-1],# bottom right
            [0, height-1],# bottom left
        ]
    ).astype(int)
    
    markerCorners = mark_dict['markerCorners']
    markerIds = mark_dict['markerIds']

    if len(markerCorners) > 0:
        mark = markerCorners[0] # assume only one
        pts_dst = mark[0]
        print(pts_dst.shape)

        # [       
        #         [
        #             [519.,  35.],
        #             [578.,  28.],
        #             [590.,  90.],
        #             [530.,  98.]
        #         ]
        #  ]

        # Calculate Homography
        h, status = cv.findHomography(pts_src, pts_dst)

        # Warp source image to destination based on homography
        warped_image = cv.warpPerspective(img_animation, h, (img.shape[1],img.shape[0]))

        # Prepare a mask representing region to copy from the warped image into the original frame.
        mask = np.zeros([img.shape[0], img.shape[1]], dtype=np.uint8);
        cv.fillConvexPoly(mask, np.int32(pts_dst), (255, 255, 255), cv.LINE_AA);

        # Erode the mask to not copy the boundary effects from the warping
        element = cv.getStructuringElement(cv.MORPH_RECT, (3,3));
        mask = cv.erode(mask, element, iterations=3);

        # Copy the mask into 3 channels.
        warped_image = warped_image.astype(float)
        mask3 = np.zeros_like(warped_image)
        for i in range(0, 3):
            mask3[:,:,i] = mask/255

        # Copy the masked warped image into the original frame in the mask region.
        warped_image_masked = cv.multiply(warped_image, mask3)
        frame_masked = cv.multiply(img.astype(float), 1-mask3)
        im_out = cv.add(warped_image_masked, frame_masked)
        return im_out.astype(np.uint8)
    
    return img


