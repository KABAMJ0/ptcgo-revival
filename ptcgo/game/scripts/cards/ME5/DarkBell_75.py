from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import confuse_both_actives, excluding, pokemon_of

card = ItemCardDef(
    guid="1ba045ba-0a51-556c-a326-6328e3550ed7",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkBell.Name",
    display_name="Dark Bell",
    searchable_by=["Dark Bell", "Item"],
    subtypes=["Item"],
    collector_number=75,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    effect=confuse_both_actives(excluding(pokemon_of("darkness")))
)
