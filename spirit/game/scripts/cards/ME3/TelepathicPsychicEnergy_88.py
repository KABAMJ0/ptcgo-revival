from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4d6e165a-c032-556b-ad21-615e38576ac5",
    key="ME3",
    name="Telepathic Psychic Energy",
    display_name="Telepathic Psychic Energy",
    searchable_by=["Telepathic Psychic Energy", "Special"],
    subtypes=["Special"],
    collector_number=88,
    set_code="ME3",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
