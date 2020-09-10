# LookU Security

LookU Security is an artificial intelligence project for IoT with main aim of providing extra layer of security by monitoring objects. LookU Security can be trained to recognise objects like gun, matchet, fire, smoke etc. and send automated alert.

## Use Cases

LookU Security can be deployed 

- At filling station to monitor smoke, cigarret, fire etc.
- In public places to monitor people with dangerous weapons.
- At CarPark to monitor incoming and outgoing vehicles.
- At schools to monitor people going and coming in.


## Implementation

This artificial intelligence project for IOT is purely written in python and can be used on Adruino devices. For example, see the code below:

Go to [settings.py](settings.py) and edit the basic information or check the [examples folder](examples)

```python 

#import the security and settings module

import LookU.security, LookU.settings

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

        # once an object or multiple objects has been detected this block is executed

        # you can call your call back function here for Arduino or any devices

        # do anything you want here e.g sound alarm

        pass

```

## Training Your Own Model

Try using HaarTraining to generate your xml model

## Developer(s)

[Oyeniyi Abiola Peace](https://twitter.com/_iamoracle)

## Contributors

0 contributors, be the first!

You can drop more examples

You can submit your models or send enquires to officialbilas(at)gmail(dot)com

Thanks
