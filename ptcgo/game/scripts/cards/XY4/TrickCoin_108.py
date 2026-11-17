from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_coin_reroll

card = PokemonToolCardDef(
    guid="7e429de7-9066-542d-b839-6c7e4177b718",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrickCoin.Name",
    display_name="Trick Coin",
    searchable_by=["Trick Coin", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=108,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=holder_coin_reroll(None)
)
