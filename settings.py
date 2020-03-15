from os import path

working_directory = path.dirname(os.path.realpath(__file__))

# you can change you video source to any video file you want

# if you want to use camera uncomment the line below

# video_source = 0

# comment out the line below if you are using camera

video_source = path.join(working_directory, 'source/cars.mp4')

# the path to the model

model = path.join(working_directory, 'model/cars.xml')
