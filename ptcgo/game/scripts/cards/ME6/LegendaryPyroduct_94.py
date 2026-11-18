from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import abilities_off_for, is_evolution_pokemon

card = StadiumCardDef(
    guid="f892c948-6533-566f-bafb-3c301c0b5dad",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendaryPyroduct.Name",
    display_name="Legendary Pyroduct",
    searchable_by=["Legendary Pyroduct", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(is_evolution_pokemon)
)
