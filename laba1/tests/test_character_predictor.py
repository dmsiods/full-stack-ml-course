"""Tests for CharacterPredictor class."""
import os
from pathlib import Path
import unittest

import sys
sys.path.append('/home/sidorkoda/workspace/full-stack-ml-course/laba1')

from character_predictor import CharacterPredictor

SUPPORT_DIRNAME = Path(__file__).parents[0].resolve() / "support" / "emnist"

os.environ["CUDA_VISIBLE_DEVICES"] = ""


class TestCharacterPredictor(unittest.TestCase):
    """Tests for the CharacterPredictor class."""

    def test_filename(self):
        """Test that CharacterPredictor correctly predicts on a single image, for serveral test images."""
        predictor = CharacterPredictor()

        for filename in SUPPORT_DIRNAME.glob("*.png"):
            pred, conf = predictor.predict(str(filename))
            print('===================')
            print(filename, type(filename))
            print(f"Prediction: {pred} at confidence: {conf} for image with character {filename.stem}")
            self.assertEqual(pred, filename.stem)
            self.assertGreater(conf, 0.1)
