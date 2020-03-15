"""
The example below shows how a carpark fitted with IOT can use this project to detect an incoming car
"""

import settings

if __name__ == "__main__":
    
    security = LookU('cars.xml', 'car1.mp4')

    while True:

        security.read_frame()


        security.detect_objects()

        security.mark_objects()

        if security.object_detected():

            # your call back function here
