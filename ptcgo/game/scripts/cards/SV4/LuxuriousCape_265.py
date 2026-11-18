from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import combined, gated_hp_bonus, holder_prize_shift, is_rule_box_free_pokemon

card = PokemonToolCardDef(
    guid="8584d25b-27f2-5fa8-868f-9524bf063866",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuriousCape.Name",
    display_name="Luxurious Cape",
    searchable_by=["Luxurious Cape", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=265,
    set_code="SV4",
    rarity=Rarities.Rare,
    passive=combined(gated_hp_bonus(100, is_rule_box_free_pokemon), holder_prize_shift(1, is_rule_box_free_pokemon))
)
