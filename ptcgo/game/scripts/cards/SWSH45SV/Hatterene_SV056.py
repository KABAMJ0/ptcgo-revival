from ptcgo.game.card_effects.attacks_common import place_counters, count_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_pokemon_card


async def mind_hat(ctx):
    """Once per turn: each player discards a card from their hand (opponent first)."""
    if not await ctx.ask_yes_no("Each player discards a card from their hand?"):
        return
    await ctx.discard_from_hand(
        1, minimum=0, player_id=ctx.opponent_id,
        prompt="Discard a card from your hand.",
    )
    await ctx.discard_from_hand(
        1, minimum=0, player_id=ctx.player_id,
        prompt="Discard a card from your hand.",
    )


card = PokemonCardDef(
    guid="370b1a69-44a6-5126-8757-a0de262edb3e",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatterene.Name",
    display_name="Hatterene",
    searchable_by=["Hatterene", "Stage 2", "Hatterene"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    family_id=856,
    abilities=[
        Ability(
            title="Mind Hat",
            game_text="Once during your turn, you may use this Ability. Each player discards a card from their hand. (Your opponent discards first.)",
            activation=Activations.ONCE_PER_TURN,
            effect=mind_hat,
        ),
        Attack(
            title="Dripping Grudge",
            game_text="Put 1 damage counter on your opponent's Active Pokémon for each Pokémon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(count_discard("mine", is_pokemon_card), "opponent_active"),
        ),
    ],
)
