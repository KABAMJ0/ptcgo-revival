from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import any_of, basic_energy_of, pokemon_of

card = ItemCardDef(
    guid="b08e536d-d378-505a-a5fc-f56a8fb877e3",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatchingSet.Name",
    display_name="Bug Catching Set",
    searchable_by=["Bug Catching Set", "Item"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=2, predicate=any_of(pokemon_of("grass"), basic_energy_of("grass")), minimum=0)
)
