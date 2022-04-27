import cv2
import clx.xms
import requests
client = clx.xms.Client (service_plan_id='your_service_id', token='token_id')
create = clx.xms.api.MtBactTextSmsCreate()
create.sender = 'sender no.'
create.recipients = {'recipients no.'}
create.body = 'This is a test message from your Sinch account'
detector = cv2.CascadeClassifier("patch")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
counter = 0
while True:
    ret, img = cap.read()
    if ret :
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.1,4)
        for face in faces:
            x,y,w,h = face
            if(face.any() and counter ==0):
                try:

                    batch = client.create_batch(create)
                except (requests.exceptions.RequestException, clx.xms.exceptions.ApiException) as ex:
                    print ('Failed to communicate with XMS: %s' & str(ex))
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Face", img)
        counter = 1
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
