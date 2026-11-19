from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import requires_hand
from ptcgo.game.card_effects.trainers import is_energy_card


_engine_gate = requires_hand(is_energy_card, n=1)


async def _rumbling_engine(ctx):
    """Discard an Energy card from hand, then draw up to 6 cards in hand."""
    if not await ctx.ask_yes_no(
            "Discard an Energy card from your hand to draw until you have 6?"):
        return
    if not await ctx.discard_from_hand(
            1, predicate=is_energy_card,
            prompt="Discard an Energy card from your hand"):
        return
    await ctx.draw_until(6)

card = PokemonCardDef(
    guid="6b01990a-8ca5-5cd6-aed9-57676009b8d2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name",
    display_name="Revavroom",
    searchable_by=["Revavroom", "Stage 1", "Revavroom"],
    subtypes=["Stage 1"],
    collector_number=142,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Ability(
            title="Rumbling Engine",
            game_text="You must discard an Energy card from your hand in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_engine_gate,
            effect=_rumbling_engine,
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=flip_bonus(90),
        ),
    ],
)