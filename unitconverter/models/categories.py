# Copyright (c) 2022-2025 Mike Cunningham


from unitconverter.exceptions import ConverterError
from unitconverter.models.dimension import Dimension


class Categories:
    """ Used to store and retrieve category names for common dimensions. """

    def __init__(self, categories: dict[str, Dimension] | None = None):
        """ Create a categories dictionary which is used to map dimensions to category names.

        Args:
            categories (dict[str, Dimension] | None, optional):
                A dictionary of pre-defined categories. Defaults to None.
        """
        self._categories: dict[str, Dimension] = {}

        # Add each category individually to validate them
        if categories:
            for name, dimension in categories.items():
                self.add_category(name, dimension)

    def add_category(self, category: str, dimension: Dimension) -> None:
        """ Add a new category to the dictionary.

        Args:
            category (str): A category name. Must be unique.
            dimension (Dimension): The dimension associated with the category.

        Raises:
            ConverterError: If the category name already exists.
        """
        if category in self._categories:
            raise ConverterError(f"{category} is already defined"
                                 " (category names must be unique)")

        self._categories[category] = dimension

    def get_categories(self, dimension: Dimension) -> list[str]:
        """ Find all categories matching the specified dimension.

        Args:
            dimension (Dimension): A dimension instance.

        Raises:
            ConverterError: If the argument isn't a valid Dimension.

        Returns:
            list[str]: A list of category names, or an empty list if no category is found.
        """
        if not isinstance(dimension, Dimension):
            raise ConverterError(f"{dimension!r} is not a valid dimension")

        categories = []
        for category, dimen in self._categories.items():
            if dimension == dimen:
                categories.append(category)

        return categories

    def get_category(self, dimension: Dimension) -> str:
        """ Convert a Dimension and its categories into a category string.

        Args:
            dimension (Dimension): A dimension instance.

        Returns:
            str: A category name, or "unknown category" if no category is found.
        """
        categories = self.get_categories(dimension)
        if categories:
            return ", ".join(categories)
        else:
            return "unknown category"

    def get_dimension(self, category: str) -> Dimension:
        """ Find the dimension matching the specified category.

        Args:
            category (str): The category name.

        Raises:
            ConverterError: If the category doesn't exist.

        Returns:
            Dimension: The category's dimension.
        """
        try:
            return self._categories[category]
        except KeyError:
            raise ConverterError(f"{category} is not a valid category")
