from ptcgo.game.card_effects.attacks_common import energy_move_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _precious_gift(ctx):
    """End of turn: optionally draw up to 8 cards in hand."""
    if not await ctx.ask_yes_no("Draw cards until you have 8 cards in your hand?"):
        return
    await ctx.draw_until(8)

card = PokemonCardDef(
    guid="3eabc5f4-eb6b-53ee-a5c3-912cb1fd42e8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Precious Gift",
            game_text="Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 8 cards in your hand.",
            trigger=Triggers.END_OF_TURN,
            effect=_precious_gift,
        ),
        Attack(
            title="Power Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=energy_move_attack(1),
        ),
    ],
)