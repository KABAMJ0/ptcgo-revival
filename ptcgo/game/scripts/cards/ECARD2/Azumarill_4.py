from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.card_effects.passives_common import is_in_active_spot, unafflicted
from ptcgo.game.card_effects.support_common import remove_self_from_play


def _on_bench_available(board, player_id, pokemon):
    return not is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)


async def _bubble_turn(ctx):
    results = await ctx.flip_coins(1, "Bubble Turn")
    if not (results and results[0]):
        return
    await remove_self_from_play(destination="hand", with_attachments="same")(ctx)


card = PokemonCardDef(
    guid="08576321-6082-53b7-ae4c-0157d914edeb",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Bubble Turn",
            game_text="Once during your turn (before your attack), if Azumarill is on your Bench, you may flip a coin. If heads, return Azumarill and all cards attached to it to your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench_available,
            effect=_bubble_turn,
        ),
        Attack(
            title="Aqua Sonic",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)