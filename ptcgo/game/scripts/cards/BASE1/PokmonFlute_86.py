from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_from_discard

card = ItemCardDef(
    guid="c0600115-ca94-5116-8c10-f7105ac806f4",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFlute.Name",
    display_name="Pokémon Flute",
    searchable_by=["Pok\u00e9mon Flute"],
    subtypes=[],
    collector_number=86,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_from_discard()
)
