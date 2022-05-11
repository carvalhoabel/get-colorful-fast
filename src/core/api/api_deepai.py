import json
from src.model.picture import Picture
from requests import (
    post as deep_ai,
    get as get_img,
    codes as found,
)


class APIDeepAI:
    """This class has the function to just make
    requests from an extern API.
    """

    # API URL
    URLAPI = 'https://api.deepai.org/api/colorizer'

    def __init__(self) -> None:
        """New APIDeepAI.
        """
        pass

    def picture_url(self, picture: Picture) -> bool:
        """This mathod takes an image from internet,
        grey scale and transform it.

        Args:
            picture (Picture): Picture instance.

        Returns:
            bool: True if it be a success else False.
        """
        response = deep_ai(
            self.URLAPI,
            data={
                'image': picture.source,
            },
            headers={'api-key': '6d8ff185-4701-4545-82f5-a81c4352f453'}
        )
        return self._manager_deeper(response=response, picture=picture)

    def picture_local(self, picture: Picture) -> bool:
        """This mathod takes an image from a local storage,
        grey scale and transform it.

        Args:
            picture (Picture): Picture instance.

        Returns:
            bool: True if it be a success else False.
        """
        response = deep_ai(
            self.URLAPI,
            files={
                'image': open(picture.source, 'rb'),
            },
            headers={'api-key': '6d8ff185-4701-4545-82f5-a81c4352f453'}
        )
        return self._manager_deeper(response=response, picture=picture)

    # private method - a manager to download types

    def _manager_deeper(self, response: json, picture: Picture) -> bool:
        """This method is a manager to download local and online.

        Args:
            response (json): response from a post method.
            picture (Picture): instance of Picture.

        Returns:
            bool: True if success else False.
        """
        response = response.json()
        if 'id' not in response:
            return False
        else:
            picture.source = response['output_url']
            picture.save = f'{picture.save}/{picture.name}'
        return self._make_download(picture=picture)

    # private method to make download from image

    def _make_download(self, picture: Picture) -> bool:
        """This method is used to try make download from image and
        return a boolean value to inform user.

        Args:
            picture (Picture): instance of Picture.

        Returns:
            bool: True if downloaded else False.
        """
        response = get_img(url=picture.source, stream=True)
        if response.status_code == found.OK:
            with open(file=picture.save, mode='wb') as writer:
                for byte in response.iter_content(chunk_size=256):
                    writer.write(byte)
            return True
        else:
            return False
