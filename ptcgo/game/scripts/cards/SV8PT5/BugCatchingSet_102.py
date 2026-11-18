from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import any_of, basic_energy_of, pokemon_of

card = ItemCardDef(
    guid="4e3125d8-fba7-58c8-b9f9-1d861d1c7757",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatchingSet.Name",
    display_name="Bug Catching Set",
    searchable_by=["Bug Catching Set", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=2, predicate=any_of(pokemon_of("grass"), basic_energy_of("grass")), minimum=0)
)
