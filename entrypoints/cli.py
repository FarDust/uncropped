from pathlib import Path

from click import command, argument, option
from utils.img_io import load_images, save_img


@command()
@argument("path_str", required=True)
@argument("output_file_name", required=True)
@option(
    "--save_files",
    "-s",
    "save_files",
    flag_value=True,
    default=False,
    help="Set if store intermediate images files",
)
@option(
    "--debug",
    "-d",
    "debug",
    flag_value=True,
    default=False,
    help="Activate debug prompts",
)
@option(
    "--output",
    "-o",
    "output_dir",
    default="./",
    help="Defines output directory, set as current directory as default",
)
def cli_entrypoint(path_str, output_file_name, debug, save_files, output_dir):
    path = Path(path_str).absolute()
    output_path = Path(output_dir).absolute()
    output_file_name = Path(output_file_name).name
    images = load_images(path)
    save_img(images[-1], output_path, output_file_name)
