import cv2
import mediapipe as mp
import time
import itertools as it


class FaceMesh:
    def __init__(self):
        self.flag = 0
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh()
        self.array_prev = [[0, 0] for self.k in range(468)]

    def face_track(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            self.ret, self.frame = self.cap.read()
            self.frameRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.height, self.width, _ = self.frame.shape

            # Face Landmarks

            self.result = self.face_mesh.process(self.frameRGB)
            if self.result.multi_face_landmarks:
                for self.facial_landmarks in self.result.multi_face_landmarks:
                    for self.i in range(468):
                        self.pt1 = self.facial_landmarks.landmark[self.i]
                        self.x = int(self.pt1.x * self.width)
                        self.y = int(self.pt1.y * self.height)
                        if abs(self.x - self.array_prev[self.i][0]) > 2 or abs(self.y - self.array_prev[self.i][1]) > 2:
                            cv2.circle(self.frame, (self.x, self.y), 1, (0, 0, 255), -1)
                            self.flag = 1
                        else:
                            cv2.circle(self.frame, (self.x, self.y), 1, (0, 255, 0), -1)
                        self.array_prev[self.i][0] = self.x
                        self.array_prev[self.i][1] = self.y
                    self.flag = 0

            cv2.imshow("Cam", cv2.flip(self.frame, 1))
            self.key = cv2.waitKey(1)

            if self.key == ord("q"):
                break
        self.cap.release()
        cv2.destroyAllWindows()



