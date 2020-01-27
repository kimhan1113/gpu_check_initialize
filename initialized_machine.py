# import os
#
# os.environ['CUDA_VISIBLE_DEVICES'] ='0'
#
# import tensorflow as tf
#
# with tf.Graph().as_default():
#     gpu_options = tf.GPUOptions(allow_growth = True)
#
import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0' #use GPU with ID=0
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5 # maximun alloc gpu50% of MEM
config.gpu_options.allow_growth = True #allocate dynamically
sess = tf.Session(config = config)