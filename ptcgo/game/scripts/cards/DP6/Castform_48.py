from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.card_effects.support_common import swap_with_named


def _is_castform(card):
    return "Castform" in (getattr(def_for(card.archetype_id), "display_name", "") or "")


async def _weather_ball(ctx):
    stadium = ctx.stadium_in_play()
    owner = getattr(stadium, "owning_player_id", None) if stadium is not None else None
    await ctx.deal_damage(30 + (30 if owner == ctx.opponent_id else 0))
    if owner == ctx.player_id and ctx.attacker is not None:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="c7c7915f-d4d0-5994-8e4d-15647c5317bb",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Ability(
            title="Temperament",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperament",
            game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform. (Any cards attached to Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Castform on top of your deck. Shuffle your deck afterward. You can't use more than 1 Temperament Pok\u00e9-Power each turn.",
            effect=swap_with_named(predicate=_is_castform, destination="deck"),
        ),
        Attack(
            title="Weather Ball",
            game_text="If you have a Stadium card in play, remove 3 damage counters from Castform. If your opponent has a Stadium card in play, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=_weather_ball,
        ),
    ],
)