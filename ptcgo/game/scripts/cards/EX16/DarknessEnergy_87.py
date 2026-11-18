from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageBonusPassive
card = EnergyCardDef(
    guid="d1c2c77e-043b-5543-bc3e-3cbbd6bf554c",
    key="EX16",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="EX16",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageBonusPassive(10, PokemonTypes.DARKNESS, "Dark"),
)
