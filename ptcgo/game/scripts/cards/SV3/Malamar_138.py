from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.content.definitions import Activations


async def _psychic_insight(ctx):
    theirs = ctx.deck_top(1, ctx.opponent_id)
    if their_top := theirs:
        await ctx.reveal_cards(their_top, to_player=ctx.player_id)
    mine = ctx.deck_top(1)
    if mine:
        await ctx.reveal_cards(mine, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="4ab4ae2d-2051-5e38-8c38-1b866667b27a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Ability(
            title="Psychic Insight",
            game_text="Once during your turn, you may look at the top card of your opponent's deck. If you do, look at the top card of your deck.",
            effect=_psychic_insight,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Hypnotic Ray",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)