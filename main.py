import cv2
import mediapipe as mp
import pyautogui
from PIL.ImageChops import screen

cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()
while True:
    _, frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ =frame.shape
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x * frame_w )
            y=int(landmark.y * frame_h )
            if (x > 640 or x<0):
                x = 640
            if (y > 360 or y<0):
                y = 360
            cv2.circle(frame,(x,y),3,(0,255,0))
            if id == 1:
                screen_x= int(landmark.x * screen_w )
                screen_y = int(landmark.y * screen_h)
                if(screen_x>1920):
                    screen_x=1910
                if(screen_y>1080):
                    screen_y=1070
                pyautogui.moveTo(screen_x,screen_y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
        clk=int((left[0].y - left[1].y) * 100)
        if ( clk <= 0):
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye tracker Cursor',frame)
    cv2.waitKey(1)
