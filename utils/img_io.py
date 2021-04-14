import os
from pathlib import Path

from halo import Halo
from spinners import Spinners
from cv2 import imread, imwrite


def load_images(path: Path):
    images = list()
    assert path.exists
    if os.path.isdir(path):
        with Halo(text="Loading images", spinner=Spinners.dots.value):
            for file in path.iterdir():
                images.append(imread(str(file)))
    return images


def save_img(img, output_path: Path, filename: str):
    if not output_path.is_dir():
        os.mkdir(str(output_path))
    image_filename = Path(output_path, filename)
    if image_filename.suffix == "":
        image_filename = image_filename.with_suffix(".png")

    imwrite(str(image_filename), img)
