"""CharacterPredictor class"""
from typing import Tuple, Union

import numpy as np

from models import CharacterModel
import util


class CharacterPredictor:
    """Given an image of a single handwritten character, recognizes it."""

    def __init__(self):
        self.model = CharacterModel()
        self.model.load_weights("laba1/weights/CharacterModel_EmnistDataset_mlp_weights.h5")

    def predict(self, image_or_filename: Union[np.ndarray, str]) -> Tuple[str, float]:
        """Predict on a single image."""
        if isinstance(image_or_filename, str):
            image = util.read_image(image_or_filename, grayscale=True)
        else:
            image = image_or_filename
        return self.model.predict_on_image(image)

    def evaluate(self, dataset):
        """Evaluate on a dataset."""
        return self.model.evaluate(dataset.x_test, dataset.y_test)
