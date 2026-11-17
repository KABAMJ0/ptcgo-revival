from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, combined, gated_hp_bonus, holder_prize_shift, is_pokemon_EX, is_pokemon_gx

card = PokemonToolCardDef(
    guid="897323f4-ce91-5810-92a6-fb3a9af0a44b",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandChallengeAmulet.Name",
    display_name="Island Challenge Amulet",
    searchable_by=["Island Challenge Amulet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=265,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    passive=combined(gated_hp_bonus(100, any_of(is_pokemon_gx, is_pokemon_EX)), holder_prize_shift(-1, any_of(is_pokemon_gx, is_pokemon_EX)))
)
