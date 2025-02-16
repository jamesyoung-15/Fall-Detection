import cv2
import zmq
import base64

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')

camera = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        (grabbed, frame) = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        footage_socket.send_string(base64.b64encode(buffer))
        
    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        print("End")
        break
