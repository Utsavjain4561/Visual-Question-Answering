from keras.callbacks import ModelCheckpoint,TensorBoard
import argparse
from model import build_model
from prepare_data import setup

# Support command-line options
parser = argparse.ArgumentParser()
parser.add_argument('--big-model', action='store_true', help='Use the bigger model with more conv layers')
parser.add_argument('--use-data-dir', action='store_true', help='Use custom data directory, at /data')
args = parser.parse_args()

if args.big_model:
  print('Using big model')
if args.use_data_dir:
  print('Using data directory')

# Prepare data
train_X_ims, train_X_seqs, train_Y, test_X_ims, test_X_seqs, test_Y, im_shape, vocab_size, num_answers, _, _, _ = setup(args.use_data_dir)

print('\n--- Building model...')
model = build_model(im_shape, vocab_size, num_answers, args.big_model)
checkpoint = ModelCheckpoint('model_1.h5', save_best_only=True)
tensorboard = TensorBoard(log_dir='./Graph',histogram_freq=0,write_graph=True,write_images=True)
print('\n--- Training model...')
model.fit(
  [train_X_ims, train_X_seqs],
  train_Y,
  batch_size=38575,
  validation_data=([test_X_ims, test_X_seqs], test_Y),
  shuffle=True,
  epochs=8,
  callbacks=[checkpoint,tensorboard],
)
