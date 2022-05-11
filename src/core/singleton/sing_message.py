from src.core.message.message import Message


class SingMessage:
    """Singleton class to Message model, it access data to
    inform user what happens with data into back-end.
    """

    _message = None

    @classmethod
    def message(cls) -> Message:
        """It returns a message class instance if there's else
        create and return it.

        Returns:
            Message: instance of Message.
        """
        if not cls._message:
            cls._message = Message()
        return cls._message
