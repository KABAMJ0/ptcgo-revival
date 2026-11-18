from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, holder_discount_and_boost, hop, is_pokemon_card, owned_by

card = PokemonToolCardDef(
    guid="506f6862-b24c-55b5-9a3e-59ec4f5ff738",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HopsChoiceBand.Name",
    display_name="Hop's Choice Band",
    searchable_by=["Hop's Choice Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=148,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    passive=holder_discount_and_boost(1, 30, all_of(is_pokemon_card, owned_by("hop")))
)
