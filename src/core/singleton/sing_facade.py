from src.core.facade.facade import Facade


class SingFacade:
    """Singleton pattern to Facade instance. Use
    it to access facade and all backend project.
    It is used to economize data instances.
    """

    _facade = None

    @classmethod
    def facade(cls) -> Facade:
        """It returns if there's Facade instance, else
        it creates and returns it.

        Returns:
            Facade: instance of Facade.
        """
        if not cls._facade:
            cls._facade = Facade()
        return cls._facade
