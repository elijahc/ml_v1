import numpy as np
from vgg19 import VGG19
from keras.preprocessing import image
from imagenet_utils import preprocess_input
from keras.models import Model

def DeepOracle():

    x = Convolution2D(16, 1, 1, activation='relu', border_mode='same', name='block1_conv1') (img_input)
    x = Convolution2D(32, 1, 1, activation='relu', border_mode='same', name='block1_conv2') (x)
    x = Convolution2D(2, 1, 1, activation='relu', border_mode='same', name='block1_conv3') (x)
    x = Convolution2D(1, 1, 1, activation='relu', border_mode='same', name='block1_conv4') (x)



def get_activations(layers):

    features = []
    base_model = VGG19(weights='imagenet')

    img_path = 'cat.jpg'
    img = image.load_img(img_path, target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    x = preprocess_input(x)

    for layer in layers:

        model = Model(input=base_model.input, output=base_model.get_layer(layer).output)
        feature_set = model.predict(x)

        features.extend([feature_set])

    for layer, features in zip(layers,features):
        print(layer,': ', features.shape)

    activations = features
    return activations


if __name__ == '__main__':
    blocks = [
            'block1_conv1',
            'block1_conv2',
            'block1_pool',
            'block2_pool',
            'block3_pool',
            'block4_pool',
            'block5_pool'
            ]
    layers = [
            'block2_conv1',
            'block5_conv1',
            'block5_conv2',
            'block5_conv4']
    input = get_activations(layers)
#print('features size: ',features.shape)

