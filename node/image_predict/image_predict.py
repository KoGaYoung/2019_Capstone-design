import matplotlib
import numpy as np
import os
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
import operator
from keras.models import load_model
from keras.preprocessing import image
import base64
import ast
import sys

def recommand(predictions, class_dict):
    # Recommend top 3
    predictions = predictions[0].tolist()
    predict = []
    for i in range(len(predictions)):
        predict.insert(i, [i, predictions[i]])

    predict2 = sorted(predict, key=lambda x: x[1], reverse=True)

    recommend1 = str([name for name, target in class_dict.items() if target == predict2[0][0]])
    recommend2 = str([name for name, target in class_dict.items() if target == predict2[1][0]])
    recommend3 = str([name for name, target in class_dict.items() if target == predict2[2][0]])
    re_str = recommend1[2:len(recommend1)-2]+","+recommend2[2:len(recommend2)-2]+","+recommend3[2:len(recommend3)-2]
    return re_str

# base64.txt -> image -> save folder
remove_str = 'data:image/png;base64,'

image_path = '/Users/heosanghun/Desktop/capston/node/image_predict/predict_image/12/out.png'
g = open(image_path, 'wb')
g.write(base64.b64decode(sys.argv[1][len(remove_str):]))
g.close()


model1 = load_model('/Users/heosanghun/Desktop/capston/node/image_predict/model.h5')
model1.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Print test prediction

f2 = open('/Users/heosanghun/Desktop/capston/node/image_predict/label_dict.txt')
label_dict = eval(f2.read())
f2.close()

batchsize = 64
image_size = (255, 255)

pred_gen = ImageDataGenerator().flow_from_directory(
    '/Users/heosanghun/Desktop/capston/node/image_predict/predict_image/',
    class_mode='categorical',
    batch_size=batchsize,
    target_size=image_size
)
predictions = model1.predict_generator(pred_gen)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
import operator
index, value = max(enumerate(predictions[0]), key=operator.itemgetter(1))
pred_result = [name for name, target in label_dict.items() if target == index]

#recommand_top3
re_list = recommand(predictions, label_dict)
print(re_list)
