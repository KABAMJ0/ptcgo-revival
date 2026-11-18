from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import heal_on_attach
card = EnergyCardDef(
    guid="5ef7ae06-0829-5bfa-9ed4-d97d1b9ce0fd",
    key="EX8",
    name="Heal Energy",
    display_name="Heal Energy",
    searchable_by=["Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=heal_on_attach(1, cure_conditions=True),
)
