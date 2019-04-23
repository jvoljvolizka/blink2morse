import cv2
import sys
#import pygame
#i'm using pygame beacause he is too cute but nobody likes him. I feel sad about that cute python library

cascPath = sys.argv[1]
eyecaspath = sys.argv[2]
faceCascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier(eyecaspath)
video_capture = cv2.VideoCapture(0)
i = 0
frameWidth = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
lockeyes = False
#(width, height) = (1000, 1000)
#screen = pygame.display.set_mode((width, height))
#pygame.display.flip()
#pygame.draw.line(screen, (255,0,255), (20,20), (70,80), 2)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    i = i + 1
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=2.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=4.2)
        for (ex,ey,ew,eh) in eyes:
            lockeyes = True
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            print(eyes.shape[0])

    if(lockeyes == True):
                cv2.putText(img = frame, text = "i can see your dark soul from these eyes and it's delicious",org = (0,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1,color = (0, 0, 0))



# Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

