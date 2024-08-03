import cv2
import numpy as np
from object_detection import ObjectDetection
import math




#intialized object detection
od= ObjectDetection()


cap = cv2.VideoCapture("source_code\los_angeles.mp4")
count = 0
centre_points_prev_frame =[]
tracking_object ={}
track_id=0
while True:
    ret, frame = cap.read()
    count += 1
    if not ret:
        break
    #centre points current frame
    centre_points_cur_frame = []
    #detect on=bject on frame
    (class_id, scores, boxes)=od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cx = int((x + x+ w)/2)
        cy = int((y + y+ h)/2)
        centre_points_cur_frame.append((cx,cy))
        cv2.circle(frame, (cx, cy), 5, (0,0,255),-1)
        #print(f"Frame Number{count}",x, y, w, h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if count <=2 :
        for pt in centre_points_cur_frame:
            for pt2 in centre_points_prev_frame:
                distance = math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])
                if distance < 20:
                    tracking_object[track_id] = pt
                    track_id += 1
    else: 
        tracking_object_copy = tracking_object.copy()
        centre_points_cur_frame_copy = centre_points_cur_frame.copy()
        for object_id,pt2 in tracking_object_copy.items():
            object_exists = False
            for pt in centre_points_cur_frame_copy:
                distance = math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])
                if distance < 20:
                    tracking_object[object_id] = pt
                    object_exists = True
                    if pt in centre_points_cur_frame:
                        centre_points_cur_frame.remove(pt)
                    continue
            #remove ID if object is not detected
            if not object_exists:
                tracking_object.pop(object_id)
            #add ID
        for pt in centre_points_cur_frame:
            tracking_object[track_id] = pt
            track_id += 1
        #print("Tracking object",tracking_object)
        
    for object_id, pt in tracking_object.items():
        cv2.circle(frame, pt, 5, (0,0,255),-1)
        cv2.putText(frame, str(object_id), (pt[0],pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    #print("current frame",centre_points_cur_frame)
    
    cv2.imshow("frame", frame)

    #make a copy of the points
    centre_points_prev_frame = centre_points_cur_frame.copy()
    if cv2.waitKey(1) & 0xFF == ord('q') :
    
        break

cap.release()
cv2.destroyAllWindows()


