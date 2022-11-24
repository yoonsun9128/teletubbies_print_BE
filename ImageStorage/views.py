from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import tensorflow_hub as hub
import PIL

def load_image(image_path, image_size=(512, 256)):
    image_path = image_path[1:]
    print("윤선", image_path)
    img = tf.io.decode_image(
    tf.io.read_file(image_path),
    channels=3, dtype=tf.float32)[tf.newaxis, ...]
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    return img

def style(input_img, choice_filter):
    print("머신러닝", input_img)
    print("머신러닝", choice_filter)
# load images
    original_image = load_image(input_img)
    style_image = load_image(f'/media/{choice_filter}')

    style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='VALID')

    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    output = hub_module(tf.constant(original_image), tf.constant(style_image))
    stylized_photo = output[0]
    print(stylized_photo, 'testtest')
    result = export_image(stylized_photo)
    print("ㅇㅇㅇ",result)
    return result


def export_image(tf_img):
    tf_img = tf_img*255
    tf_img = np.array(tf_img, dtype=np.uint8)
    if np.ndim(tf_img)>3:
        assert tf_img.shape[0] == 1
        img = tf_img[0]
    return PIL.Image.fromarray(img)

    # 저장하는 코드
    # export_image(stylized_photo).save("output.png")
