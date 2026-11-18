from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageBonusPassive
card = EnergyCardDef(
    guid="5b8c4f59-1540-5111-a2a2-7fbc26acfafd",
    key="EX11",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=103,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageBonusPassive(10, PokemonTypes.DARKNESS, "Dark"),
)
