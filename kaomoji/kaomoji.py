#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Procedurally generate kaomoji from a collection of features.

A kaomoji is a Japanese emoticon. Instances of the Kaomoji class use a
collection of categories and associated features, as well as a template
string with placeholders for the features to procedurally generate a
kaomoji. The features used to generate the kaomoji are derived from
categories that specify the emotion (e.g., sadness, joy) or type (e.g.,
dog, cat) of kaomoji.

Example:
    > kao: Kaomoji = Kaomoji()
    > kao.create()
    > kao.create("joy")
    > kao.create("indifference")
    > kao.create("love")
    > kao.categories
    > kao.template
"""

import random
import string
from typing import Dict, List, Union

from kaomoji import config


class Kaomoji:
    """Procedurally generate a kaomoji from a collection of features.

    Instances of the Kaomoji class load and use a collection of categories
    and associated features, as well as a template string with placeholders
    for the features to procedurally generate a kaomoji. The features used
    to generate the kaomoji are derived from categories that specify the
    emotion (e.g., sadness, joy) or type (e.g., dog, cat) of kaomoji.
    ...

    Attributes
    ----------
        _categories : Dict
            Collection of categories and associated features.
        _kaomoji : str, None
            The most recently generated kaomoji.
        _template : str
            Template string for configuring features into kaomoji.

    Methods
    -------
    categories() -> List[str]:
        Returns a list of top-level category labels.

    create(category : Union[str, None]) -> Union[str, None]
        Returns a procedurally generated kaomoji from a random or
        user-specified category.

    template() -> List[str]:
        Returns a list of all feature placeholders in the template string.
    """

    def __init__(self) -> None:
        """Instantiate a new kaomoji object.

        This object loads the collection of categories and associated features,
        as well as the template string necessary to combine the features into
        a kaomoji. The collection of features and template string are specified
        in config.py.
        """
        self._categories: Dict = config.CATEGORIES
        self._kaomoji: str = ""
        self._template: str = config.TEMPLATE

    def __repr__(self) -> str:
        """The most recently generated kaomoji.

        Returns the most recently generated kaomoji; returns an empty string,
        otherwise.
        """
        return self._kaomoji

    def __str__(self) -> str:
        """The most recently generated kaomoji.

        Returns the most recently generated kaomoji; returns an empty string,
        otherwise.
        """
        return self._kaomoji

    @property
    def categories(self) -> List[str]:
        """A list of all top-level categories.

        Returns a list of all top-level categories that are specified in
        config.py.
        """
        return [category for category in self._categories]

    @property
    def template(self) -> List[str]:
        """The kaomoji template string.

        Returns the list of placeholders in the template string necessary
        to combine the features into a kaomoji.
        """
        return list(
            set([feature[1] for feature in string.Formatter().parse(self._template)])
        )

    def create(self, category: Union[str, None] = None) -> str:
        """Create a kaomoji.

        Returns a procedurally generated kaomoji from a combination of
        features for a random or user-specified category.

        Parameters
        ----------
        category : Union[str, None] -> str
            A procedurally generated kaomoji.
        """
        features: Dict = {}

        if category is None:
            category = random.choice(self.categories)

        for feature in self.template:
            features[feature] = random.choice(
                self._categories[category]["features"][feature]
            )

        kaomoji: str = self._template.format(**features)

        return kaomoji
