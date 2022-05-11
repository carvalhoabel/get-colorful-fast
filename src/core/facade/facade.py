import json
from src.model.picture import Picture
from src.core.service.service import Service


class Facade:
    """Project Facade Class to access back-end.
    """

    _service = Service()

    def __init__(self) -> None:
        """New Facade.
        """
        pass

    def swap_picture_url(self, picture: Picture) -> json:
        """This function takes a grey scale picture url and swap to colorful.

        Args:
            picture (Picture): Picture instance with all required data.

        Returns:
            json: A json with all need information.
        """
        return self._service.swap_picture_url(picture=picture)

    def swap_picture_local(self, picture: Picture) -> json:
        """This function takes a grey scale picture local file and swap to colorful.

        Args:
            picture (Picture): Picture instance with all required data.

        Returns:
            json: A json with all need information.
        """
        return self._service.swap_picture_local(picture=picture)
