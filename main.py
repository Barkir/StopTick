from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.videoplayer import VideoPlayer
from kivymd.app import MDApp
from plyer import filechooser

import serial
import cv2
import mediapipe as mp

prev_time = 0
s = serial.Serial("COM3")

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


class CamApp(BoxLayout, Screen):

    def __init__(self, **kwargs):
        super(CamApp, self).__init__(**kwargs)
        CamApp.selected = ''
        self.orientation = "vertical"
        self.img1 = Image()
        self.add_widget(self.img1)
        self.btn = Button(text='>>>>>>>>>>')
        self.file_chooser = Button(text='choose file')
        self.add_widget(self.btn)
        self.add_widget(self.file_chooser)

        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh()
        self.array_prev = [[0, 0] for k in range(468)]

        self.btn.bind(on_press=self.screen_transition)
        self.file_chooser.bind(on_release=self.filer)

        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/60.0)

    def update(self, dt):
        global prev_time
        global s
        ret, frame = self.capture.read()
        # for i in range(6):
        #     res = str(s.readline())[2:-5]
        #     arr.append(int(res))
        #     print(res)
        # val = max(arr)

        height, width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb_frame)

        # if Clock.get_time() > prev_time + 1 and result.multi_face_landmarks:
        #     sm.get_screen("player").play()

        # if result.multi_face_landmarks:
        #     for facial_landmarks in result.multi_face_landmarks:
        #         n = 0
        #         for i in range(0, 468):
        #             pt1 = facial_landmarks.landmark[i]
        #             x = int(pt1.x * width)
        #             y = int(pt1.y * height)
        #             if abs(x - self.array_prev[i][0]) > 2 or abs(y - self.array_prev[i][1]) > 2:
        #                 cv2.circle(frame, (x, y), 2, (0, 0, 250), -1)
        #                 self.array_prev[i][0] = x
        #                 self.array_prev[i][1] = y
        #                 n += 1
        #             else:
        #                 cv2.circle(frame, (x, y), 2, (0, 250, 0), -1)
        #                 self.array_prev[i][0] = x
        #                 self.array_prev[i][1] = y
        #         if n >= 10:
        #             sm.get_screen("player").stop()
        #             prev_time = Clock.get_time()
        #             print(prev_time)

        if s.inWaiting() > 0:
            s.flushInput()
            sm.get_screen("player").stop()
            prev_time = Clock.get_time()
            # print(prev_time)

        if Clock.get_time() > prev_time + 1:
            sm.get_screen("player").play()

        buf1 = cv2.flip(frame, -1)
        cv2.imshow("CV2 Image", cv2.flip(frame, 1))
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1

    def screen_transition(self, *args):
        self.manager.current = 'player'

    def filer(self, _):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            sm.get_screen('player').videoplayer.source = selection[0]


class KivyPlayer(BoxLayout, Screen):

    def __init__(self, **kwargs):
        super(KivyPlayer, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.videoplayer = VideoPlayer(source='chebuu.mp4')


        self.add_widget(self.videoplayer)
        self.btn = Button(size_hint=(1, .1), text='<<<<<<<<<<')
        self.add_widget(self.btn)

        self.btn.bind(on_press=self.screen_transition)

        self.videoplayer.state = "stop"
        self.videoplayer.options = {"eos": "loop"}

    def stop(self):
        self.videoplayer.state = "pause"
        # print(self.videoplayer.state)
        # time.sleep(0.5)

    def play(self):
        self.videoplayer.state = "play"
        print(self.videoplayer.state)
        # time.sleep(0.5)

    def screen_transition(self, *args):
        self.manager.current = 'cam'




class MainApp(App):
    def build(self):
        global sm
        sm = ScreenManagement()
        sm.add_widget(CamApp(name="cam"))
        sm.add_widget(KivyPlayer(name="player"))
        return sm


if __name__ == '__main__':
    MainApp().run()
