from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_prizes_remaining
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _sky_scorching_light(ctx):
    """Only when both players' remaining Prize cards total 6 or less; then 6
    damage counters on each of the opponent's Pokemon."""
    if count_prizes_remaining("mine")(ctx) + \
            count_prizes_remaining("theirs")(ctx) > 6:
        return
    for pokemon in ctx.opponent_pokemon_in_play():
        if not ctx.effects_blocked(pokemon):
            await ctx.deal_damage(60, target=pokemon, apply_modifiers=False,
                                  as_counters=True)

card = PokemonCardDef(
    guid="94ff5dfe-75d4-5b15-8473-54988ea1f0cc",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozmaGX.Name",
    display_name="Ultra Necrozma-GX",
    searchable_by=["Ultra Necrozma-GX", "Basic", "GX", "Ultra Beast", "UltraNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=95,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=800,
    abilities=[
        Attack(
            title="Photon Geyser",
            game_text="Discard all basic Psychic Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Sky-Scorching Light-GX",
            game_text="You can use this attack only if the total of both players' remaining Prize cards is 6 or less. Put 6 damage counters on each of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            effect=_sky_scorching_light,
        ),
    ],
)