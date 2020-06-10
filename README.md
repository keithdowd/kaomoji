# Kaomoji

> Create procedurally generated kaomoji (i.e., Japanese emoticons) using Python! \\(^ヮ^)/

![version](https://img.shields.io/pypi/v/kaomoji?style=for-the-badge)
![python version](https://img.shields.io/pypi/pyversions/kaomoji?style=for-the-badge)

This Python package uses procedural generation to create _kaomoji_ using a collection of features (e.g., eyes, arms, etc.) across a wide variety of different categories, such as emotions (e.g., joy, indifference, love) and animals (e.g., dog, cat, etc.). Also, the individual _kaomoji_ features and template used to organize the features are fully customizable.

[![asciicast](https://asciinema.org/a/337897.svg?speed=2&theme=monokai)](https://asciinema.org/a/337897)

## Installation

Installation is easy using the `pip` package manager.

```console
$ pip install --user kaomoji
```

## Example

Run the following command on the console to view a pre-fab example.

```console
$ python -m kaomoji
```

## Usage

The first step is to import the `Kaomoji` class.

```python
> from kaomoji.kaomoji import Kaomoji
```

Next, instantiate a `Kaomoji` object.

```python
> kao = Kaomoji()
```

Using the `Kaomoji` object, procedurally generate a _kaomoji_ from a random category.

```python
> kao.create()
```

Or, generate a _kaomoji_ from a specific category.

```python
> kao.create("joy")
```

All of the available categories are easily viewable on the `categories` attribute.

```python
> kao.categories
```

## Releases

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). See [`CHANGELOG`](./CHANGELOG.md) for a detailed release history.

## Contributing

Contributions are welcome. See [`CONTRIBUTING`](./CONTRIBUTING.md) for instructions on how to contribute to this project.

## License

Distributed under the [MIT](https://opensource.org/licenses/MIT) license. See [`LICENSE`](./LICENSE.md) for more information.

## Author

This project was made with 💖 by Keith Dowd @ <keith.dowd@gmail.com>.

## Acknowledgements

Big thanks to [Japan](https://www.japan.go.jp/) for creating _kaomoji_ and anime.

Also, huge shoutout to [kaomoji.ru](http://kaomoji.ru/en/) for the history and wonderfully expansive and organized collection of _kaomoji_.
