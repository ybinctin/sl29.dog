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
        self._mother = None
        self._father = None
        self._puppies = []

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

    @property
    def mother(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.

        Returns:
            Optional[Dog]: La mère du chien ou None.
        """
        return self._mother
    
    @property
    def father(self) -> Optional['Dog']:
        """
        Retourne le père du chien ou None.

        Returns:
            Optional[Dog]: Le père du chien ou None.
        """
        return self._father
    
    @property
    def puppies(self):
        """
        Retourne les enfants du chien ou une liste vide.

        Returns:
            type list
        """
        return self._puppies

    def mate(self, other: 'Dog') -> 'Dog':
        """
        Fait s'accoupler deux chiens et retourne un chiot.

        Args:
            other (Dog): L'autre chien avec lequel s'accoupler.

        Returns:
            Dog: Le chiot issu de l'accouplement.

        Raises:
            MatingError: Si les deux chiens sont de même sexe.
        """
        if self._sex == other._sex :
            raise MatingError("Les deux chiens sont du même sexe, accouplement impossible.")
        else:  
            father = self if self.sex == "M" else other
            mother = self if self.sex == "F" else other

            if father.race == mother.race:
                race = father.race
            else:
                race = "bâtard"
            
            sexe = random.choice(["M", "F"])
            
            chiot = Dog(race, sexe, "Matthieu")

            chiot._father = father.name
            chiot._mother = mother.name

            mother.puppies.append(chiot.__str__())
            father.puppies.append(chiot.__str__())
        return chiot

    def bark(self, entier=1) -> str:
        return "Woff"*entier

    def chew(self, stuff):
        nv_stuff = stuff[:-1]
        return nv_stuff    

    def __str__(self) -> str:
        """
        Méthode d'affichage de la classe

        Returns:
            str: Les informations du chien.
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"