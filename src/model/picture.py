class Picture:
    """This class is a model of a picture.
    """

    def __init__(self) -> None:
        """New picture.
        """
        # picture name
        self._name = ''
        # picture source (url or local file)
        self._source = ''
        # where the converted picture must save
        self._save = ''
        # it is used to switch online and local
        self._online = False

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        self._source = source

    @property
    def save(self) -> str:
        return self._save

    @save.setter
    def save(self, save: str) -> None:
        self._save = save

    @property
    def online(self) -> bool:
        return self._online

    @online.setter
    def online(self, online: bool) -> None:
        self._online = online
