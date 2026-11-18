from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where, pokemon_of

card = ItemCardDef(
    guid="50d65389-5855-5217-aac8-4262900c4aeb",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragonElixir.Name",
    display_name="Dragon Elixir",
    searchable_by=["Dragon Elixir", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=heal_where(60, "active", pokemon_of("dragon"), min_energy=0)
)
