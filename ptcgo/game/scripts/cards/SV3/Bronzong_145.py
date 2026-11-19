from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import draw_n
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.attacks_common import bonus_if

def _same_hand_size(ctx):
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)

card = PokemonCardDef(
    guid="cc5a1d45-fee8-5c4c-a5d5-ec46a7cd9c96",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Oracle Press",
            game_text="During your opponent's next turn, prevent all effects of attacks used by your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=protect_next_turn(effects_too=True),
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 90),
        ),
    ],
)