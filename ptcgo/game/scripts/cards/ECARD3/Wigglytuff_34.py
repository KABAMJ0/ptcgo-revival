from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations


async def _good_neighbor_heal(ctx):
    for target in (ctx.my_active(), ctx.opponent_active()):
        if target is not None:
            await ctx.heal(20, target)

from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03b0d551-112e-5c3b-8fff-228ba69d06ba",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Ability(
            title="Good Neighbor",
            game_text="Once during your turn (before your attack), if Wigglytuff is on your bench, you may flip a coin. If heads, each player removes up to 2 damage counters from his or her Active Pok\u00e9mon. This power can't be used if you have already used another Wigglytuff's Good Neighbor Pok\u00e9-Power this turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Good Neighbor",
            condition=lambda board, player_id, pokemon: not is_in_active_spot(pokemon),
            effect=flip_gate(then=_good_neighbor_heal),
        ),
        Attack(
            title="Do the Wave",
            game_text="Flip a coin. If heads, this attack does 10 damage times the number of Pok\u00e9mon you have in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)