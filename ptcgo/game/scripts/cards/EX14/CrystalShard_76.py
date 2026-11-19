from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import crystal_shard_tool

card = PokemonToolCardDef(
    guid="7a50104c-02b9-5e68-b9fe-8f5ba3afa8fa",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=76,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=crystal_shard_tool(),
)
