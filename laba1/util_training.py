"""Function to train a model."""
from time import time

from tensorflow.keras.callbacks import EarlyStopping

# import sys
# sys.path.insert(1, '../text_recognizer')
# sys.path.append('/home/sidorkoda/workspace/full%20stack/fsdl-text-recognizer-project/lab1/text_recognizer')

from datasets.dataset import Dataset
from models.base import Model

EARLY_STOPPING = True


def train_model(model: Model, dataset: Dataset, epochs: int, batch_size: int, use_wandb: bool = False) -> Model:
    """Train model."""
    callbacks = []

    if EARLY_STOPPING:
        early_stopping = EarlyStopping(monitor="val_loss", min_delta=0.01, patience=3, verbose=1, mode="auto")
        callbacks.append(early_stopping)


    model.network.summary()

    t = time()
    _history = model.fit(dataset=dataset, batch_size=batch_size, epochs=epochs, callbacks=callbacks)
    print("Training took {:2f} s".format(time() - t))

    return model