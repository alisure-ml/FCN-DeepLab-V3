import argparse
import numpy as np

IMG_MEAN = np.array((104.00698793, 116.66876762, 122.67891434), dtype=np.float32)

BATCH_SIZE = 4
BN_WEIGHT_DECAY = 0.9997
CKPT = 0
DATA_DIRECTORY = 'C:\\ALISURE\\Data\\voc\\VOCdevkit\\VOC2012'
DATA_NAME = 'VOC12'
IGNORE_LABEL = 255
INPUT_SIZE = 513
LEARNING_RATE = 0.01
MOMENTUM = 0.9
NUM_CLASSES = 21
NUM_GPUS = 1
NUM_LAYERS = 101
NUM_STEPS = 100  # 600000
NUM_TRAIN = 1464
NUM_VAL = 1449
POWER = 0.9
RANDOM_SEED = 1234
RESTORE_FROM = None
SAVE_NUM_IMAGES = 1
SAVE_PRED_EVERY = 2  # 1000
SNAPSHOT_DIR = './snapshots'
SPLIT_NAME = 'train'
WEIGHT_DECAY = 1e-4

parser = argparse.ArgumentParser(description="DeepLabV3")
parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="number of image")
parser.add_argument("--bn-weight-decay", type=float, default=BN_WEIGHT_DECAY, help="parameter for batch norm.")
parser.add_argument("--ckpt", type=int, default=CKPT, help="Checkpoint to restore.")
parser.add_argument("--data-dir", type=str, default=DATA_DIRECTORY, help="Path to the directory dataset.")
parser.add_argument("--data-name", type=str, default=DATA_NAME, help="Name of the dataset.")
parser.add_argument("--freeze-bn", action="store_true", help="Whether to freeze batch norm params.")
parser.add_argument("--ignore-label", type=int, default=IGNORE_LABEL, help="label to ignore during the training.")
parser.add_argument("--input-size", type=int, default=INPUT_SIZE, help="height and width of images.")
parser.add_argument("--learning-rate", type=float, default=LEARNING_RATE, help="learning rate for polynomial decay.")
parser.add_argument("--momentum", type=float, default=MOMENTUM, help="Momentum component of the optimiser.")
parser.add_argument("--not-restore-last", action="store_true", help="Whether to not restore last (FC) layers.")
parser.add_argument("--num-classes", type=int, default=NUM_CLASSES, help="Number of classes to predict (including background).")
parser.add_argument("--num-gpus", type=int, default=NUM_GPUS, help="Number of GPUs to use.")
parser.add_argument("--num-layers", type=int, default=NUM_LAYERS, help="Number of layes in ResNet).")
parser.add_argument("--num-steps", type=int, default=NUM_STEPS, help="Number of training steps.")
parser.add_argument("--power", type=float, default=POWER, help="Decay parameter to compute the learning rate.")
parser.add_argument("--random-mirror", action="store_true", help="Whether to randomly mirror the inputs during the training.")
parser.add_argument("--random-scale", action="store_true", help="Whether to randomly scale the inputs during the training.")
parser.add_argument("--random-seed", type=int, default=RANDOM_SEED, help="Random seed to have reproducible results.")
parser.add_argument("--restore-from", type=str, default=RESTORE_FROM, help="Where restore model parameters from.")
parser.add_argument("--save-num-images", type=int, default=SAVE_NUM_IMAGES, help="How many images to save.")
parser.add_argument("--save-pred-every", type=int, default=SAVE_PRED_EVERY, help="Save summaries and checkpoint every often.")
parser.add_argument("--snapshot-dir", type=str, default=SNAPSHOT_DIR, help="Where to save snapshots of the model.")
parser.add_argument("--split-name", type=str, default=SPLIT_NAME, help="Split name.")
parser.add_argument("--weight-decay", type=float, default=WEIGHT_DECAY, help="Regularisation parameter for L2-loss.")

args = parser.parse_args()
