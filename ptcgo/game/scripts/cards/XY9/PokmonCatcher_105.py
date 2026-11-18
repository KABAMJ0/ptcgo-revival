from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import if_heads, opponent_bench_to_active

card = ItemCardDef(
    guid="0b9bd788-cfb4-589f-b2fa-b64de85945cb",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=if_heads(opponent_bench_to_active())
)
