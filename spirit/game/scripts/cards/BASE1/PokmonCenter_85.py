from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import heal_all_own_discard_energy

card = ItemCardDef(
    guid="e9728209-ae39-5204-ae97-b70869663e0e",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=85,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=heal_all_own_discard_energy()
)
