from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_retreat_free

card = PokemonToolCardDef(
    guid="fdf34d23-7b49-586c-bd51-14cab081eb27",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloatStone.Name",
    display_name="Float Stone",
    searchable_by=["Float Stone", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    passive=holder_retreat_free()
)
