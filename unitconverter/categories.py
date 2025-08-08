# Copyright (c) 2022-2025 Mike Cunningham


from unitconverter.dimension import Dimension
from unitconverter.exceptions import DefinitionError, DimensionError


class Categories:
    """ Used to store and retrieve category names for common dimensions. """

    def __init__(self, categories: dict[str, Dimension] | None = None):
        """ Initialize dimension categories. """
        self._categories = {}

        # Add each category individually to validate them
        if categories:
            for name, dimension in categories.items():
                self.add_category(name, dimension)

    def add_category(self, category: str, dimension: Dimension) -> None:
        """ Add a category to the dictionary. """
        if category in self._categories:
            raise DefinitionError(f"{category} is already defined"
                                  " (category names must be unique)")

        self._categories[category] = dimension

    def get_category(self, dimension: Dimension) -> str:
        """ Get a string representation of the dimension.
            Returns "unknown category" if no dimension was found. """
        categories = self.get_categories(dimension)

        if categories:
            return ", ".join(categories)
        else:
            return "unknown category"

    def get_categories(self, dimension: Dimension) -> list[str]:
        """ Get a list of categories matching the dimension."""
        if not isinstance(dimension, Dimension):
            raise DimensionError(f"{dimension!r} is not a valid dimension")

        categories = []
        for category, dimen in self._categories.items():
            if dimension == dimen:
                categories.append(category)

        return categories

    def get_dimension(self, category: str) -> Dimension:
        """ Get dimension for the specified category. """
        try:
            return self._categories[category]
        except KeyError:
            # TODO: should this be another exception class? A CategoryError?
            raise DefinitionError(f"{category} is not a valid category name")

    def __contains__(self, item: str | Dimension) -> bool:
        """ Check if a category or dimension is in the dictionary. """
        return item in self._categories.keys() or item in self._categories.values()
