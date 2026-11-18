from ptcgo.game.card_effects.energies import DamageBonusPassive
from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4d906f0c-fb41-5857-b0c9-07d6e2dc3e71",
    key="ME5",
    name="Voltaic Lightning Energy",
    display_name="Voltaic Lightning Energy",
    searchable_by=["Voltaic Lightning Energy", "Special"],
    subtypes=["Special"],
    collector_number=84,
    set_code="ME5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=True,
    passive=DamageBonusPassive(20, PokemonTypes.LIGHTNING),
)
