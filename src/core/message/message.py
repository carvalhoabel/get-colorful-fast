import json


class Message:
    """It class is a model of data to inform user about
    """

    def __init__(self) -> None:
        """New Message.

        Attributes Created:
            - warning: bool
            - error: bool
            - success: bool
            - text: str
            _ title: str

        Methods:
            - clear_msg() :: to clear data instance.
        """
        self._text = self._title = ''
        self._warning = self._error = self._success = False

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def warning(self) -> bool:
        return self._warning

    @warning.setter
    def warning(self, warning: bool) -> None:
        self._warning = warning

    @property
    def error(self) -> bool:
        return self._error

    @error.setter
    def error(self, error: bool) -> None:
        self._error = error

    @property
    def success(self) -> bool:
        return self._success

    @success.setter
    def success(self, success: bool) -> None:
        self._success = success

    def clear_msg(self) -> None:
        """This method has the function only delete
        all current data from it instance.
        """
        self.text = self.title = ''
        self.warning = self.error = self.success = False

    def get_json(self) -> json:
        """This method returns a json.

        Returns:
            json: json with desired data.
        """
        return json.dumps(
            {
                'title': self.title,
                'text': self.text,
                'warning': self.warning,
                'error': self.error,
                'success': self.success,
            }
        )
