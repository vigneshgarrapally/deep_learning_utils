__Deep Learning Utilities__
===

 [Table of Contents](#table_of_contents)
* [Flask Module](#flask-module)
* [File Video Stream using Threading](#file-video-stream-using-threading)

----

## Flask Module:

* __Editing Configuration YAML File:__

    > Different pretrained models can be arranged in groups. For each item two keys has to be added.
    > 1. Path to pretrained model path/to/model.h5 
    > 2. Path to Inference Script path/to/script.py 

    
* __Start Flask Server__ :
    > Make sure current working directory is deep_learning_utils/flask_api
        python app.py

### File Video Stream Using Threading

    Generally, Encoding and decoding frames from Video is I/O bound operation. Though, python has GIL, creating a child thread for extracting frames will significantly improve the program speed as most of the Image processing Libraries have C extensions. 
Make sure current working directory is deep_learning_utils/read_video

    python read_frames_fast.py --video path_to_video.mp4



