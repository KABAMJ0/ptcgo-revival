from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import combined, gated_damage_boost, gated_hp_bonus, is_basic_pokemon

card = PokemonToolCardDef(
    guid="a1bc0828-b71f-596d-8e12-a06ef6ba2838",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingFuryBelt.Name",
    display_name="Fighting Fury Belt",
    searchable_by=["Fighting Fury Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=combined(gated_hp_bonus(40, is_basic_pokemon), gated_damage_boost(10, is_basic_pokemon))
)
