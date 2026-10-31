import cv2
import time
camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascade + "haarcascade_frontalface_default.xml") 

smile_detector = cv2.cascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

eye_detector = cv2.cascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

while True:
    success, frame = camera.read()

    if not success or frame is None:
        break

    detector_sorriso = False
    ectectou_olhos = False

    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,scaleFactor=1.1,minNeighbors=1.1,minSize=(100,100)
    )

    for (x,y,w,h) in  faces:
        eye_region_gray = gray[y:y + h //2, x:x + w]
        face_gray = gray[y:y + h, x:x + w]

        cv2.rectangle(frame, (x,y) (x+w, y+h), (0,255,0), 2)

        eyes = eye_detector.detecMultiScla(
            eye_region_gray, scaleFactor=1.1, minNeighbors=10, miniSize=(25,25))  
        
        smiles = smile_detector.detecMultiScla(
            face_gray, scaleFactor=1.7, minNeighbors=20, miniSize=(25,25))  

        if len(eyes) > 0:
            detectou_olhos = True
    
        if len(smiles) > 0:
            detectou_sorriso = True

    if detectou_sorriso :
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_SPRING)
        cv2.putText(frame, "camara detectada", (20,80),cv2.FRONT_HERSHEY_DUPLEX, 1.5,(255,255,255),3)
        print("Sorriso nao detetado!")

    elif  detectou_olhos:
        edges = cv2.canny(frame,100,200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        print("Olhos nao detetado!")

    else :
        frame = cv2.cvColor(frame, cv2.COLOR_BAYER_BG2GRAY)
 

    cv2.imshow("Visão Computacional em Python !! :D ", frame)

    if cv2.waitKey(1) == 27:
        break



camera.release()
cv2.destroyAllWindows()