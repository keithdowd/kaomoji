#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""Example usage of Kaomoji class.

An example of how to to use the Kaomoji class to instantiate a Kaomoji
object and procedurally generate a kaomoji from a random or user-specified
category.

Example:
    $ python -m kaomoji
"""

from kaomoji.kaomoji import Kaomoji

if __name__ == "__main__":
    # Instantiate a Kaomoji object
    kao: Kaomoji = Kaomoji()

    # Create a procedurally generated kaomoji from a random category
    print(f"Random category: {kao.create()}")

    # Create a procedurally generated kaomoji from the "joy" category
    print(f"Joy: {kao.create('joy')}")

    # Create a procedurally generated kaomoji from the "indifference" category
    print(f"Indifference: {kao.create('indifference')}")

    # Create a procedurally generated kaomoji from the "love" category
    print(f"Love: {kao.create('love')}")

    # Print all available catgories
    print(f"Categories: {kao.categories}")

    # Print template placeholders for configuring features into a kaomoji
    print(f"Template placeholders: {kao.template}")
