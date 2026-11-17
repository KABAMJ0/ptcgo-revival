from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, is_pokemon_card, owned_by, stadium_no_retreat

card = StadiumCardDef(
    guid="d375bd53-88c9-5764-9272-0a67b123d4f9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsCastle.Name",
    display_name="N's Castle",
    searchable_by=["N's Castle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=152,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    passive=stadium_no_retreat(all_of(is_pokemon_card, owned_by("n")))
)
