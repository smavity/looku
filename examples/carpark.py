"""
The example below shows how a carpark fitted with IOT can use this project to detect an incoming car

"""

#import might not work, if have to work your way around import
import LookU.code, LookU.settings

if __name__ == "__main__":


    #initialize LookU security with the model and source
    security = code.LookU(settings.model,settings.video_source)

    while True:
        
        #grabs a frame
        security.read_frame()

        #detects objects in frame
        security.detect_objects()

        #draw a rectangle around the object detected
        security.mark_objects()

        #if object is detected do something
        if security.object_detected():

            # your call back function here

            pass