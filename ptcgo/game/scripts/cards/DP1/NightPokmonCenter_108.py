from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_two_heal_or_discard_energy

card = ItemCardDef(
    guid="5b868f01-dfbf-55da-91d7-65bbc3face46",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightPokmonCenter.Name",
    display_name="Night Pokémon Center",
    searchable_by=["Night Pok\u00e9mon Center", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=flip_two_heal_or_discard_energy()
)
