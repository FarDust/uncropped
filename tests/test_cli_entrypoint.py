import os
from pathlib import Path

from entrypoints.cli import cli_entrypoint


def test_cli_debug(cli_runner):
    output_path = "output"
    input_dir = "test_img"
    output_filename = "test"
    expected_path = Path(
        f"{output_path}/{output_filename}").with_suffix(".png")
    result = cli_runner.invoke(
        cli_entrypoint, ["-d", "-o", output_path, input_dir, output_filename]
    )
    assert result.exit_code == 0
    assert expected_path.exists()
    os.remove(str(expected_path))


def test_cli(cli_runner):
    output_path = "output"
    input_dir = "test_img"
    output_filename = "test"
    expected_path = Path(
        f"{output_path}/{output_filename}").with_suffix(".png")
    result = cli_runner.invoke(
        cli_entrypoint, ["-o", output_path, input_dir, output_filename]
    )
    assert result.exit_code == 0
    assert expected_path.exists()
    os.remove(str(expected_path))
