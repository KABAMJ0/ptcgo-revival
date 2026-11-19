from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.card_effects.passives_common import is_in_active_spot, unafflicted
from ptcgo.game.session.effects import full_stack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _beating_wings_ready(board, player_id, pokemon) -> bool:
    return is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)


async def _beating_wings(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    pick = await ctx.choose_pokemon(
        bench, "Choose 1 of your Benched Pok\u00e9mon to shuffle into your deck")
    if pick is None:
        return
    await ctx.shuffle_into_deck(full_stack(pick), ctx.player_id)

card = PokemonCardDef(
    guid="6e275006-a1ca-5b6a-a426-c0a3b59708da",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Ability(
            title="Beating Wings",
            game_text="Once during your turn (before your attack), if Pidgeot is your Active Pok\u00e9mon, you may shuffle 1 of your Benched Pok\u00e9mon and all cards attached to it into your deck. This power can't be used if Pidgeot is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_beating_wings_ready,
            effect=_beating_wings,
        ),
        Attack(
            title="Sharp Beak",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(50)),
        ),
    ],
)