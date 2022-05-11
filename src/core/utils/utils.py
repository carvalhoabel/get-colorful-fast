from os.path import isdir, isfile
from requests import get
from requests.exceptions import MissingSchema
from src.model.picture import Picture


def instanceok(picture) -> bool:
    """Check class instance of an object, it must be Picture.

    Args:
        picture (object): object to check.

    Returns:
        bool: True if it is a Picture else False.
    """
    return isinstance(picture, Picture)


def isdirect(direct: str) -> bool:
    """It checks if str is a directory path.
    It checks Picture().save param.

    Args:
        direct (str): str to check directory.

    Returns:
        bool: True if it is a directory else False.
    """
    return False if not isinstance(direct, str) else isdir(direct)


def isitfile(file: str) -> bool:
    """It cheks if a str is a path to a local file.
    It checks Picture().source param.

    Args:
        file (str): str to check file.

    Returns:
        bool: True if it is a file else False.
    """
    return False if not isinstance(file, str) else isfile(file)


def isiturl(url: str) -> bool:
    """It checks if a str is a url from internet.
    It checks Picture().source param.

    Args:
        url (str): str to check url.

    Returns:
        bool: True if it is a URL else False.
    """
    try:
        codes = get(url=url).status_code
        return False if not isinstance(url, str) else codes == 200
    except MissingSchema:
        return False


def get_name(wordpath: str) -> str:
    """It takes a name of file from a url or local path file.
    It get the file name from param Picture().source with a goal
    to set into Picture().name if it isnot empty.

    Args:
        wordpath (str): str to get file name.

    Returns:
        str: filename and extension.
    """
    if not isinstance(wordpath, str):
        return ''
    if '/' not in wordpath:
        return ''
    else:
        wordpath = list(wordpath)
        wordpath.reverse()
        wordpath = wordpath[: wordpath.index('/')]
        wordpath.reverse()
        wordpath = ''.join(wordpath)
    return '' if '.' not in wordpath else wordpath


def get_error_success(key: str) -> dict:
    """This fuction is for return a model msg to
    success or error messages.

    Args:
        key (str): key to a dict.

    Returns:
        dict: a dict_keys(text, title) if key in dc_msg else None.
    """
    dc_msg = {
        'success': {
            'text': 'Success! {} Image Converted', 
            'title': 'Success - {} Image'
        },
        'error': {
            'text': 'Error! {} Image Not Converted',
            'title': 'Error - {} Image'
        },
    }
    return dc_msg[key] if key in dc_msg else None
