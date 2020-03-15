import cv2

from os import path

import exceptions

import sys


class LookU():

    """
    LookU security can be used to monitor objects
    """

    def __init__(self, model, video_source):

        self.__load_model(model)

        self.__capture_video(video_source)

    def __load_model(self, model):
        """
        load the model if model not found raise error
        """

        # checks if model exist

        if not path.isfile(model):
            raise exceptions.ModelException("model not found ")

        # load the model
        self.model = cv2.CascadeClassifier(model)

    def __capture_video(self, input):
        """
        captures video from any source e.g video or camera\n

        0 - means in-built camera
        """

        # checks if video source exists

        if not path.isfile(input):
            raise exceptions.VideoException("video source not found ")

        # load video source

        self.video = cv2.VideoCapture(input)

    def read_frame(self):
        """
        read frame from video
        """

        # reads the video into a frame

        r, self.frame = self.video.read()

    def detect_objects(self):
        """
        detects all objects in frame
        """

        self.objects = self.model.detectMultiScale(
            cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY),
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

    def mark_objects(self):
        """
        draw rectangle over detected objects
        """

        # Draw a rectangle around the objects
        for (x, y, w, h) in self.objects:
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    
    def object_detected(self):

        if len(self.objects) > 0:

            return True

        return False