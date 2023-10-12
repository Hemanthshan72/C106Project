import cv2

vid = cv2.VideoCapture('walking.avi')
body_cascade = cv2.CascadeClassifier('C:/Users/HP/Downloads/Coding things/Class/Python/Project/106/haarcascade_fullbody.xml')

while True:
    
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = body_cascade.detectMultiScale(gray,1.1,5)
    for ( x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (255,0,0), 2)
    
    
    cv2.imshow('frame' , frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

vid.release()
cv2.destroyAllWindows()
