"""Module for creating EMNIST test support files."""
from pathlib import Path
import shutil

import numpy as np

import sys
sys.path.append('/home/sidorkoda/workspace/full-stack-ml-course/laba1')

from datasets import EmnistDataset
import util as util

SUPPORT_DIRNAME = Path(__file__).parents[0].resolve() / "emnist"


def create_emnist_support_files():
    shutil.rmtree(SUPPORT_DIRNAME, ignore_errors=True)
    SUPPORT_DIRNAME.mkdir()

    dataset = EmnistDataset()
    dataset.load_or_generate_data()

    for ind in list(range(4, dataset.x_test.shape[0], 10000)):
        image = dataset.x_test[ind]
        label = dataset.mapping[np.argmax(dataset.y_test[ind])]
        print(ind, label)
        util.write_image(image, str(SUPPORT_DIRNAME / f"{label}.png"))


if __name__ == "__main__":
    create_emnist_support_files()
