from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageBonusPassive
card = EnergyCardDef(
    guid="9aa84bd8-c64d-5e0a-9dc4-ff9a09a9f0c1",
    key="EX1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=93,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageBonusPassive(10, PokemonTypes.DARKNESS, "Dark"),
)
