from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import crystal_shard_tool

card = PokemonToolCardDef(
    guid="9dfe7ec3-cfeb-5b78-903f-d67c415ca902",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    passive=crystal_shard_tool(),
)
