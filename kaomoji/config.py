#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Configuration settings for the Kaomoji class.

Object instances of the Kaomoji class require two configuration
variables passed during instantiaton: the collection of categories
and associated features (CATEGORIES) and a template string with
placeholders for configuring the features into a kaomoji (TEMPLATE).
"""

from typing import Dict

# Template string for kaomoji procedurally generated emoticons
TEMPLATE: str = "{left_arm}({left_eye}{mouth}{right_eye}){right_arm}"

# Categories of kaomoji emoticons and associated description, features, etc.
CATEGORIES: Dict = {
    # TODO: Add descriptions
    "indifference": {
        "description": "A lack of interest, concern, or sympathy.",
        "features": {
            # Arms
            "left_arm": ["ヽ", "┐", "╮", "ᕕ", "¯\_"],
            "right_arm": ["ノ", "┌", "╭", "ᕗ", "_/¯"],
            # Eyes
            "left_eye": ["ー", " ´ ", "︶", "￣", "´", " ˘ ", "‘"],
            "right_eye": ["ー", " ` ", "︶", "￣", "´", " ˘ ", "` "],
            # Mouth
            "mouth": ["_", "ヘ", "～", "д", "▽", "ヮ", "ー", "︿", "､"],
        },
        "valence": "neutral",
    },
    "joy": {
        "description": "A feeling of great pleasure and happiness.",
        "features": {
            # Arms
            "left_arm": ["╰", "＼", "٩", "<"],
            "right_arm": ["ﾉ", "ノ", "o", "／"],
            # Eyes
            "left_eye": ["▔", "^", "¯", "☆"],
            "right_eye": ["▔", "^", "¯", "☆"],
            # Mouth
            "mouth": ["▽", "ω", "ヮ", "∀"],
        },
        "valence": "positive",
    },
    "love": {
        "description": "An intense feeling of deep affection; a great interest and pleasure in something.",
        "features": {
            # Arms
            "left_arm": ["", "♡╰", "ヽ", "♡＼", "٩", "❤ "],
            "right_arm": ["", "ノ", "♡", "╯♡", " ♡", " ❤", "/ ♡", "ノ～ ♡", "۶"],
            # Eyes
            "left_eye": [
                "─",
                "´ ",
                "• ",
                "*",
                "˘",
                "μ",
                "￣",
                " ◡",
                "°",
                "♡",
                "◕",
                "˙",
                "❤",
                "´• ",
                "≧",
            ],
            "right_eye": [
                "─",
                " `",
                "• ",
                "*",
                "˘",
                "μ",
                "￣",
                " ◡",
                "°",
                "♡",
                "◕",
                "˙",
                "❤",
                " •`",
                "≦",
            ],
            # Mouth
            "mouth": ["з", "_", "‿‿", "ω", "︶", "◡", "▽", "ε", "∀", "ᵕ", "‿", "³"],
        },
        "valence": "positive",
    },
    "sadness": {
        "description": "The condition or quality of being sad.",
        "features": {
            # Arms
            "left_arm": [
                "",
                "o",
                ".･ﾟﾟ･",
                "。゜゜",
                "｡･ﾟﾟ*",
                "｡･ﾟ",
                ".｡･ﾟﾟ･",
                "｡ﾟ",
                "･ﾟ･",
                "｡ﾟ･ ",
            ],
            "right_arm": [
                "",
                "o",
                "･ﾟﾟ･.",
                " ゜゜。",
                "*ﾟﾟ･｡",
                "･｡",
                "･ﾟﾟ･｡.",
                "･ﾟ･",
                "･ﾟ｡",
            ],
            # Eyes
            "left_eye": [
                "μ",
                "T",
                "╥",
                "〒",
                "-",
                " ; ",
                "个",
                "╯",
                "ಥ",
                ">",
                "｡•́",
                "╯",
            ],
            "right_eye": [
                "μ",
                "T",
                "╥",
                "〒",
                "-",
                " ; ",
                "个",
                "╯",
                "ಥ",
                "<。",
                "•̀｡",
                "<、",
            ],
            # Mouth
            "mouth": ["_", "ヘ" "ω", "﹏", "Д", "︿", "-ω-", "︵", "╭╮", "Ｏ", "><"],
        },
        "valence": "negative",
    },
}
