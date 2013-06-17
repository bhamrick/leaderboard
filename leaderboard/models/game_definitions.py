from leaderboard.models.datatypes import (
    Enum,
    Time
    )

import inspect
import sys

class Game(object):
    pass

class PokemonRedBlue(Game):
    name = "Pokemon Red/Blue"
    shortname = "rb"
    category_data = {
        "Any% Glitchless": {
            "Game Time": Time(60),
            "Real Time": Time(0.1),
            "Version": Enum("Red", "Blue"),
            "Language": Enum("English"),
            "Platform": Enum("Gameboy",
                             "Gameboy Color",
                             "Gameboy Advance",
                             "Gameboy Player",
                             "N64 Transfer Pak",
                             "Gambatte",
                             "VBA",
                             "Other Emulator"),
            }
        }

class PokemonYellow(Game):
    name = "Pokemon Yellow"
    shortname = "y"
    category_data = {
        "Any% Glitchless": {
            "Game Time": Time(60),
            "Real Time": Time(0.1),
            "Version": Enum("Red", "Blue"),
            "Language": Enum("English"),
            "Platform": Enum("Gameboy",
                             "Gameboy Color",
                             "Gameboy Advance",
                             "Gameboy Player",
                             "N64 Transfer Pak",
                             "Gambatte",
                             "VBA",
                             "Other Emulator"),
            }
        }

games_by_shortname = {}
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj) and issubclass(obj, Game) and obj is not Game:
        games_by_shortname[obj.shortname] = obj
