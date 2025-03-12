class Dog:
    """
    Une classe représentant un chien.

    :param name: Le nom du chien.
    :param race: La race du chien.
    """

    def __init__(self, race: str, name: str = "") -> None:
        """
        Initialise un chien avec une race et un nom.

        :param race: La race du chien.
        :param name: Le nom du chien (optionnel, par défaut une chaîne vide).
        """
        self._name: str = name
        self._race: str = race

    def get_name(self) -> str:
        """
        Retourne le nom du chien.

        :return: Le nom du chien.
        """
        return self._name

    def get_race(self) -> str:
        """
        Retourne la race du chien.

        :return: La race du chien.
        """
        return self._race

