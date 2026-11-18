from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_retreat_free

card = PokemonToolCardDef(
    guid="5d073628-31df-5dd0-91f1-df851a226be7",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloatStone.Name",
    display_name="Float Stone",
    searchable_by=["Float Stone", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=137,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=holder_retreat_free()
)
