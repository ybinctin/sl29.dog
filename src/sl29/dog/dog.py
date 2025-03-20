"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass


class Dog:
    """
    Une classe représentant un chien.

    Attributes:
        _race (str): La race du chien (protected).
        _sex (str): Le sexe du chien (protected).
        name (str): Le nom du chien (public).
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race  # Attribut protégé pour la race
        self._sex = sex    # Attribut protégé pour le sexe
        self.name = name   # Attribut public pour le nom

    @property
    def race(self) -> str:
        """
        Retourne la race du chien.

        Returns:
            str: La race du chien.
        """
        return self._race

    @property
    def sex(self) -> str:
        """
        Retourne le sexe du chien

        Returns:
            str: Le sexe du chien.
        """
        return self._sex
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Méthode d'affichage de la classe
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"

if __name__ == "__main__":
    pass