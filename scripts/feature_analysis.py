import numpy as np
import pandas as pd
from geometry import *

def collectFaceComponents(facial_points):
    # Function to collect landmarks points, grouped, as polygons\shapes
    faceShape = np.concatenate((facial_points[0:17],facial_points[[78,74,79,73,80,71,70,69,76,75,77,0]])) 
    leftEye = np.concatenate((facial_points[36:42],np.array([facial_points[36]])))
    rightEye = np.concatenate((facial_points[42:47],np.array([facial_points[42]])))
    leftIBrow = facial_points[17:22]
    rightIBrow = facial_points[22:27]
    noseLine = facial_points[27:31]
    noseArc = facial_points[31:36]
    upperLip = facial_points[[50,51,52,63,62,61,50]]
    lowerLip = facial_points[[67,66,65,56,57,58,67]]
    faceComponents = {
            "face_shape":faceShape,
            "left_eye":leftEye,
            "right_eye":rightEye,
            "left_i_brow":leftIBrow,
            "right_i_brow":rightIBrow,
            "nose_line":noseLine,
            "nose_arc":noseArc,
            "upper_lip":upperLip,
            "lower_lip":lowerLip
            }
    return faceComponents


def measure_features(facial_points):
    # Geometrically analyze & measure facial features & return a Series of measurements
    
    # Initialize facial features/components
    faceComponents = collectFaceComponents(facial_points)
    face_shape = faceComponents["face_shape"]
    leftEye, rightEye = faceComponents["left_eye"], faceComponents["right_eye"]
    left_ibrow, right_ibrow = faceComponents["left_i_brow"], faceComponents["right_i_brow"]
    nose_line, nose_arc = faceComponents["nose_line"], faceComponents["nose_arc"]
    upper_lip, lower_lip = faceComponents["upper_lip"], faceComponents["lower_lip"]
    
    # Features
    
#    forehead height, middle face height, lower face height,
#    jaw shape, left eye area, right eye area, eye to eye distance,
#    eye to eyebrow distance, upper lip height, lower lip height,
#    eyebrows distance, nose length, nose width, nose arc,
#    eyebrow detector1, eyebrow detector2,
#    eye slope detector1, eye slope detector2, eyebrow slope
        
    
    
    # Forehead height (Distance from Top forehead Eyebrow)
    # Use 3 points & avg them, to reduce any position/coordinates errors
    threeMiddleXForeheadPoints = facial_points[[70,71,80]]
    averageY =  np.average(threeMiddleXForeheadPoints[:,1])
    
    # Top edge point of eyebrow
    middle_right_ibrow = right_ibrow[2,1]
    forehead_height = middle_right_ibrow - averageY  # << Final result
    
    ##################################################################
    
    # Jaw width (as classes, not actual measurements)
    # Jaw Classes = Face shape = [Square, Round, Oval, Triangle, Heart, Oblong]
    measurement_1 = sum_slopes(face_shape[[8,9,10,11,12]], True)
    measurement_2 = sum_slopes(face_shape[[4,5,6,7,8]], True)
    measurement_3 = abs(sum_difference(face_shape[[8,9,10,11,12]]))
    measurement_4 = abs(sum_difference(face_shape[[4,5,6,7,8]]))
    
    # Find a relation between measurements to maximize margin between different classes
    jaw_width = (((measurement_1*measurement_3)/2) * ((abs(measurement_2)*abs(measurement_4))/2)) / 1000
    
    # Get angle of chin & jaw
    jaw_angle = angle_of_3points(face_shape[8],face_shape[5], face_shape[11])
    
    # Find a relation between jaw angle & jaw width
    jaw_class = (jaw_width / jaw_angle) * 100 # << Final result
    

    ##################################################################

    # Eyes Areas
    left_i_area = shape_area(leftEye) # << Final result
    right_i_area = shape_area(rightEye) # << Final result
    
    ##################################################################
    
    # eye to eye distance
    eye2eye_distance = np.min(rightEye[:,0]) - np.max(leftEye[:,0]) # << Final result
    
    ##################################################################
    
    # Eye to Eyebrow distance (left side + right side) / 2
    left_i2ibrow_distance = np.min(leftEye[:,1]) - left_ibrow[2,1]
    right_i2ibrow_distance = np.min(rightEye[:,1]) - right_ibrow[2,1]
    eye2eyebrow_distance = (left_i2ibrow_distance + right_i2ibrow_distance) / 2 # << Final result
    
    ##################################################################
    
    # Lips height
    upper_lip_height = np.max(upper_lip[:,1]) - np.min(upper_lip[:,1]) # << Final result
    lower_lip_height = np.max(lower_lip[:,1]) - np.min(lower_lip[:,1]) # << Final result
    
    ##################################################################
    
    # Eyebrows distance (the space between eyebrows) 
    eyebrows_distance = right_ibrow[0,0] - left_ibrow[4,0] # << Final result
    
    ##################################################################
    
    # Nose length
    nose_length = np.max(nose_line[:,1]) - np.min(nose_line[:,1]) # << Final result
    
    ##################################################################
    
    # Nose Width & Arc angle
    nose_width = nose_arc[4, 0] - nose_arc[0,0] # << Final result
    nose_arc_angle = angle_of_3points(nose_arc[2], nose_arc[0], nose_arc[4]) # << Final result
    
    ##################################################################
    
    # Middle-face height (from eyebrow edge to nose end)
    right_ibrow_y = right_ibrow[2,1]
    middle_face_height = nose_line[3, 1] - right_ibrow_y # << Final result
    
    ##################################################################
    
    # Lower-face height (from nose tip to chin)
    face_bottom_y = np.max(face_shape[:,1])
    lower_face_height = face_bottom_y - nose_arc[2,1] # << Final result
    
    ##################################################################
    
    # Left / Right Eyebrow class: [Straight, Arched, Angled]
    lefteyeside = leftEye[3]
    righteyeside = rightEye[0]
    
    # Determine to measure left or right eyebrow, based on
    # distance between nose bottom-point & eyes angle-point 
    noseTip = nose_line[nose_line.shape[0]-1]
    nose_eye_diff = abs(noseTip[0]-lefteyeside[0]) - abs(noseTip[0]-righteyeside[0])
    ibrow_position = "right" if nose_eye_diff <= 3 else "left"
    clear_ibrow = faceComponents[ibrow_position+"_i_brow"]
    
    # If the clear eyebrow is left, reverse points order for correct results
    if ibrow_position == "left":
        clear_ibrow = clear_ibrow[::-1]
        
    # AngleX is the difference between straight eyebrows and other types
    angleX = angle_of_3points(clear_ibrow[2],clear_ibrow[0],clear_ibrow[4]) # << Final result(1)
 
    # arched_angled_EQ is the value representing difference between curved & angled eyebrows
    arched_angled_EQ = math.ceil(((equation1(clear_ibrow)) * (equation2(clear_ibrow)) * (equation3(clear_ibrow))) * (equation4(clear_ibrow)) / 100) # << Final result(2)

    ##################################################################

    # left/right eye slope
    lefteyecenter = eyeCenter(leftEye[[1,2,4,5]])
    righteyecenter = eyeCenter(rightEye[[1,2,4,5]])
    
    ##################################################################
    
    # Eye sides slopes shape: [Upward, Downward, Straight]
    lefteyeslope = slope(leftEye[0],lefteyecenter)
    righteyeslope = slope(righteyecenter,rightEye[3]) 
    
    ##################################################################
    
    # Eye sides difference (Difference on y-axis between eye edge-point & center point)
    lefteyediff = diff_Yaxis(leftEye[0],lefteyecenter)
    righteyediff = diff_Yaxis(righteyecenter, rightEye[3])
        
    # Left eye slope & diff, right eye slope & diff
    leftpair = (lefteyeslope*-1,righteyeslope)
    rightpair = (lefteyediff,righteyediff*-1)
    totalpair = np.add(leftpair,rightpair)
    
    eyeSlopeDetector1 = totalpair[0] # << Final result(1)
    eyeSlopeDetector2 = totalpair[1] # << Final result(2)
    
    ##################################################################
    
    # Left or Right eyebrow slope (can be classified into: [Downward, Upward, straight])
    x,y = clear_ibrow[0][0], np.average(clear_ibrow[[0,1],1])
    ibrow_tip = np.array((x,y))
    ibrow_slope = slope(ibrow_tip, clear_ibrow[2]) # << Final result
    
    ##################################################################
    
    measures = {
            "forehead height" : int(round(forehead_height)),
            "middle face height" : middle_face_height,
            "lower face height" : lower_face_height,
            "jaw shape" : jaw_class,
            "left eye area" : left_i_area,
            "right eye area" : right_i_area,
            "eye to eye dist": eye2eye_distance,
            "eye to eyebrow dist" : eye2eyebrow_distance,
            "upper lip height" : upper_lip_height,
            "lower lip height" : lower_lip_height,
            "eyebrows distance" : eyebrows_distance,
            "nose length" : nose_length,
            "nose width": nose_width,
            "nose arc" : int(round(nose_arc_angle)),
            "eyebrow shape detector 1" : int(round(angleX)),
            "eyebrow shape detector 2" : arched_angled_EQ,
            "eye slope detector1" : eyeSlopeDetector1,
            "eye slope detector2" : eyeSlopeDetector2,
            "eyebrow slope" : ibrow_slope,
            }
    
    # Some detectors can be better used after clustering, such:
    # Jaw shape: [Square, Oblong, Triangle, Round, Heart, Oval]
    # Eyebrow shape detector 1 & 2 : [Straight, Arched, Angled]
    # Eye slope detector 1 & 2: [Upward, Downward, Straight]
    
    return pd.Series(measures, name="Face features measures")

def normalize_points(dat, out_range=(-1, 1)):
    # Normalize the coordinates between [-1, 1]
    domain = [np.min(dat, axis=0), np.max(dat, axis=0)]

    def interp(x):
        return out_range[0] * (1.0 - x) + out_range[1] * x

    def uninterp(x):
        b = 0
        if (domain[1] - domain[0]) != 0:
            b = domain[1] - domain[0]
        else:
            b =  1.0 / domain[1]
        return (x - domain[0]) / b

    return interp(uninterp(dat))


def scale_points(orgImgShape, faceImgShape, points):
    # Function to scale the points values of landmarks coordination between
    # X-axis scaled on [0-250]
    # Y-axis scaled on [0-190]
    
    # Get the minimum and maximum coordinations in the two dimensions
    minX = np.min(points[:,0])
    minY = np.min(points[:,1])
    points[:,0] -= minX
    points[:,1] -= minY

    # Scale the values in (190, 250) (width, height), resonable values for human face
    points[:,0] = normalize_points(points[:,0], out_range=(0, 190))
    points[:,1] = normalize_points(points[:,1], out_range=(0, 250))
    return points