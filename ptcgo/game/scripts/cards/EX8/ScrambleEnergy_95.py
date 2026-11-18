from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import evolved_excluding_ex, ScrambleEnergyPassive
card = EnergyCardDef(
    guid="5fba8084-7296-5ddc-b42b-c24c7454d384",
    key="EX8",
    name="Scramble Energy",
    display_name="Scramble Energy",
    searchable_by=["Scramble Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=evolved_excluding_ex,
    passive=ScrambleEnergyPassive(),
)
