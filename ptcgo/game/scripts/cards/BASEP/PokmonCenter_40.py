from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_own_discard_energy

card = ItemCardDef(
    guid="58d8b88f-a7bc-5d17-9f78-bf45c9eb1306",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=40,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    effect=heal_all_own_discard_energy()
)
