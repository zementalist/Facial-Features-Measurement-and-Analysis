from detection import *
from geometry import *
from feature_analysis import *
import cv2
import os

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return images, filenames

def main():
    # Move opencv window
    winname = "Test"
    cv2.namedWindow(winname)
    cv2.moveWindow(winname, 40,30) 
    
    # Capture all images in current folder & their names
    images, filesnames = load_images_from_folder('.')
    
    # Detect & Visualize each image
    for i in range(0,len(images)):
        originalImage = images[i]
        cv2.imshow(winname, originalImage) 
        cv2.waitKey(0)
        
        # Detect eyes landmarks, to align the face later
        eyePoints = facial_landmarks(originalImage, eyeOnlyMode=True)
        
        if eyePoints is not None:
            
            # Align face and redetect landmarks
            image = align_face(originalImage, eyePoints)
            improved_landmarks = facial_landmarks(image, allowEnhancement=True)

            # Draw landmarks points (just for view)
            image = drawPoints(image, improved_landmarks, pointThickness=3)
 
            # Extract the face from the image & resize it
            image = cropFullFace(image, improved_landmarks)

            #cv2.imwrite(filesnames[i].replace('sample', 'output'), image)

            # (WidthxHeight) = (190, 250) is based on the best ration found after statistical result
            image = cv2.resize(image, (190,250), 0, 0, interpolation=cv2.INTER_LANCZOS4)
            
            # Scale points coordinates
            points = scale_points(originalImage.shape, image.shape, improved_landmarks)
    
            # Measures features
            measures = measure_features(improved_landmarks)
            print(measures)
            
            # Compare features, cluster & classify -> predict gender, personality, emotions.. whatever

    
            
            

main()