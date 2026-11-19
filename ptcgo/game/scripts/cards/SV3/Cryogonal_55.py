from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import conditions_if


def _first_turn_going_second(ctx):
    """"If you go second and it's your first turn" -- both halves: this player
    is not the first player, and the game is on turn 2 (their first turn)."""
    return ctx.player_id != ctx.session.first_player_id \
        and ctx.session.turn_state.turn_number == 2


card = PokemonCardDef(
    guid="f4598966-0106-5c59-b753-217c082e28d3",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Cryogonal"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="First Freeze",
            game_text="If you go second and it's your first turn, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=conditions_if(_first_turn_going_second, SpecialConditions.PARALYZED),
        ),
    ],
)
