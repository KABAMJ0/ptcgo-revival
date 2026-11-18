from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import evolved_excluding_ex, ScrambleEnergyPassive
card = EnergyCardDef(
    guid="4efc5f1e-deba-5ca4-90d2-87e9f17147b6",
    key="EX15",
    name="Scramble Energy",
    display_name="Scramble Energy",
    searchable_by=["Scramble Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=evolved_excluding_ex,
    passive=ScrambleEnergyPassive(),
)
