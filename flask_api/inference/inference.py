import tensorflow as tf
import os
import efficientnet.tfkeras as efn
import tensorflow_addons as tfa
from efficientnet.tfkeras import EfficientNetB4
#to prevent model load errors when inference is done on system where training is not done.
from efficientnet.tfkeras import EfficientNetB4
import numpy as np
def predictions(model_path,images_path):
    HEIGHT,WIDTH = 128,128
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1/255.)
    labels = {'complex': 0,
        'frog_eye_leaf_spot': 1,
        'healthy': 2,
        'powdery_mildew': 3,
        'rust': 4,
        'scab': 5}
    test_generator = datagen.flow_from_directory(
            directory=images_path,
            target_size=(HEIGHT,WIDTH),
            color_mode="rgb",
            batch_size=1,
            class_mode=None,
            shuffle=False,
            seed=42)
    model=tf.keras.models.load_model(model_path)
    test_generator.reset()
    STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
    pred=model.predict(test_generator,steps=STEP_SIZE_TEST,verbose=1)
    pred=np.round(pred*100,decimals=2)
    print(pred[1])
    predoutput=[]
    for a in pred:
        output=""
        for b,c in zip(list(labels.keys()),a):
            output=output + "{} : {:.2f} ".format(b,c)
        predoutput.append(output)
    result={os.path.basename(img_name):p for img_name,p in zip(test_generator.filenames,predoutput)}
    return result


if __name__ == '__main__':
    predictions(model_path="F:/Vision Box/code/visionary-farm/disease_prediction/apple/models/best_model.h5",images_path="F:/Vision Box/a")
