import json
from tests.utils.utils import (
    download_mkdir, remove_download, download_path
)
from src.core.singleton.sing_facade import SingFacade as SFCD
from src.model.picture import Picture
from os.path import isdir, isfile


picture = Picture()


def test_create_download() -> None:
    # creating download directory in .tests
    remove_download()
    download_mkdir()
    assert isdir(download_path())


def test_online_success() -> None:
    # image url success case
    from tests.utils.utils import image_urls
    picture.online = True
    result = None
    for image in image_urls():
        picture.name = ''
        picture.save = download_path()
        picture.source = image
        result = SFCD.facade().swap_picture_url(picture=picture)
        result = json.loads(result)
        assert result['success']


def test_online_success_name() -> None:
    # image url success case with edited filename
    from tests.utils.utils import image_urls
    file = 'img-{}.jpg'
    ct = 1
    for image in image_urls():
        picture.save = download_path()
        picture.source = image
        picture.name = file.format(ct)
        result = SFCD.facade().swap_picture_url(picture=picture)
        result = json.loads(result)
        assert result['success']
        ct += 1


def test_local_success() -> None:
    # image path success case
    from tests.utils.utils import image_locals
    picture.online = False
    result = None
    for image in image_locals():
        picture.name = ''
        picture.save = download_path()
        picture.source = image
        result = SFCD.facade().swap_picture_local(picture=picture)
        result = json.loads(result)
        assert result['success']


def test_local_success_name() -> None:
    # image path success case with edited filename
    from tests.utils.utils import image_locals
    file = 'img-{}.jpg'
    ct = 1
    for image in image_locals():
        picture.save = download_path()
        picture.source = image
        picture.name = file.format(ct)
        result = SFCD.facade().swap_picture_local(picture=picture)
        result = json.loads(result)
        assert result['success']
        ct += 1


# failures tests

def test_online_fail() -> None:
    # image url fail case
    from tests.utils.utils import image_urls
    picture.online = True
    result = None
    for image in image_urls():
        picture.name = ''
        picture.save = download_path()
        picture.source = image + 't'
        result = SFCD.facade().swap_picture_url(picture=picture)
        result = json.loads(result)
        assert result['warning'] or result['error']


def test_online_fail_name() -> None:
    # image url fail case with edited filename
    from tests.utils.utils import image_urls
    file = 'img-{}.jpg'
    ct = 1
    for image in image_urls():
        picture.save = download_path()
        picture.source = image + 't'
        picture.name = file.format(ct)
        result = SFCD.facade().swap_picture_url(picture=picture)
        result = json.loads(result)
        assert result['warning'] or result['error']
        ct += 1


def test_local_fail() -> None:
    # image path fail
    from tests.utils.utils import image_locals
    picture.online = False
    for image in image_locals():
        picture.name = ''
        picture.save = download_path()
        picture.source = image + 't'
        result = SFCD.facade().swap_picture_local(picture=picture)
        result = json.loads(result)
        print(result)
        assert result['warning'] or result['error']


def test_local_fail_name() -> None:
    # image path fail with edited filename
    from tests.utils.utils import image_locals
    picture.online = False
    file = 'img-{}.jpg'
    ct = 1
    for image in image_locals():
        picture.save = download_path()
        picture.source = image + 't'
        picture.name = file.format(ct)
        result = SFCD.facade().swap_picture_local(picture=picture)
        result = json.loads(result)
        assert result['warning'] or result['error']
        ct += 1


# end of tester

def test_clear_picture() -> None:
    # end of test
    picture.save = ''
    picture.source = picture.name = ''
    picture.online = False
