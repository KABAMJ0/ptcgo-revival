from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_own_discard_energy

card = ItemCardDef(
    guid="e54f6176-665d-5446-bb35-ed5e01b0b3cd",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=114,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=heal_all_own_discard_energy()
)
