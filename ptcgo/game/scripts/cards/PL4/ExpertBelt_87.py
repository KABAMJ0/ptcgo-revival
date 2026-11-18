from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import combined, gated_damage_boost, gated_hp_bonus, holder_prize_shift

card = PokemonToolCardDef(
    guid="f6e78254-28b1-5ada-956c-5badc2a95faa",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpertBelt.Name",
    display_name="Expert Belt",
    searchable_by=["Expert Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=87,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    passive=combined(gated_hp_bonus(20), gated_damage_boost(20), holder_prize_shift(1))
)
