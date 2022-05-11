from typing import Generator
from pathlib import Path
from os import mkdir
from shutil import rmtree
from os.path import isdir


ROOTDIRNAME = 'get-colorful'


def current_dir() -> str:
    return Path(__name__).parent.absolute().__str__()


def root_dir() -> str:
    direct = current_dir()
    index = direct.index(ROOTDIRNAME) + len(ROOTDIRNAME)
    return direct[: index]


def download_mkdir() -> None:
    if not isdir(f'{root_dir()}/tests/download'):
        mkdir(f'{root_dir()}/tests/download')


def remove_download() -> None:
    if isdir(f'{root_dir()}/tests/download'):
        rmtree(f'{root_dir()}/tests/download')


def image_urls() -> Generator:
    images = (
        'https://static-img.zz.pt/history/imgS620I12397T20201121185301.jpg',
        'https://static-img.zz.pt/history/imgS620I12395T20201028165723.jpg',
    )
    for img in images:
        yield img


def image_locals() -> Generator:
    images = (
        f'{root_dir()}/tests/images/img1954.jpg',
        f'{root_dir()}/tests/images/img1962.jpg',
    )
    for img in images:
        yield img


def download_path() -> str:
    return f'{root_dir()}/tests/download'
