import tensorflow as tf
from tensorflow.keras import models,layers
import matplotlib.pyplot as plt
import cv2
IMAGE_SIZE=256
BATCH_SIZE=32
dataset=tf.keras.preprocessing.image_dataset_from_directory(
    "dataset",
    shuffle=True,
    image_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE
)
class_name=dataset.class_names
# for image_batch, label_batch in dataset.take(1):

# test and validation split
# 80% training , 10% test 10% 

train_size = 0.8
len(dataset*train_size)