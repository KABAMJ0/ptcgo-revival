from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import if_heads, opponent_bench_to_active

card = ItemCardDef(
    guid="0226b7ac-a852-5ab7-8988-47f9bd363d27",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=126,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=if_heads(opponent_bench_to_active())
)
