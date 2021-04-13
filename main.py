import os
from pathlib import Path

from cv2 import imread, imwrite
from alive_progress import alive_bar
from halo import Halo
from spinners import Spinners
from click import command, argument, option

images = list()


@command()
@argument("path_str", required=True)
@argument("output_file_name", required=True)
@option(
    "--save_files",
    "-s",
    "save_files",
    flag_value="debug",
    default=False,
    help="Set if store intermediate images files",
)
@option(
    "--debug",
    "-d",
    "debug",
    flag_value="debug",
    default=False,
    help="Activate debug prompts",
)
@option(
    "--output",
    "-o",
    "output",
    default="./",
    help="Defines output directory, set as current directory as default",
)
def cli_entrypoint(path_str, output_file_name, debug, save_files, output):
    path = Path(path_str).absolute()
    output_path = Path(output).absolute()
    output_file_name = Path(output_file_name).name
    assert path.exists
    if os.path.isdir(path):
        with Halo(text="Loading images", spinner=Spinners.dots.value):
            for file in path.iterdir():
                images.append(imread(str(file)))
    save_img(images[-1], output_path, output_file_name)


def save_img(img, output_path: Path, filename: str):
    if not output_path.is_dir():
        os.mkdir(str(output_path))
    image_filename = Path(output_path, filename)
    if image_filename.suffix == "":
        image_filename = image_filename.with_suffix(".png")

    imwrite(str(image_filename), img)


if __name__ == "__main__":
    cli_entrypoint()