from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import trade_pokemon

card = ItemCardDef(
    guid="b3553020-045b-563b-b097-f23232244309",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonTrader.Name",
    display_name="Pokémon Trader",
    searchable_by=["Pok\u00e9mon Trader"],
    subtypes=[],
    collector_number=77,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=trade_pokemon()
)
