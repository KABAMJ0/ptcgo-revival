from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack, on_evolve


async def _evolutionary_swirl_body(ctx):
    """The opponent shuffles their hand into their deck, then draws up to 4."""
    opponent = ctx.opponent_id
    hand = ctx.hand(opponent)
    if hand:
        await ctx.shuffle_into_deck(hand, opponent)
    else:
        await ctx.shuffle_deck(opponent)
    drawn = await ctx.ask_opponent("Draw up to 4 cards",
                                   ["0", "1", "2", "3", "4"])
    if drawn:
        await ctx.draw_cards(drawn, opponent)


card = PokemonCardDef(
    guid="d535f55c-c9ed-5cd0-a0a2-6f1eaae4ed15",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeonex.Name",
    display_name="Vaporeon ex",
    searchable_by=["Vaporeon ex", "Stage 1", "ex", "Vaporeonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=110,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Evolutionary Swirl",
            game_text="Once during your turn, when you play Vaporeon ex from your hand to evolve 1 of your Pok\u00e9mon, you may have your opponent shuffle his or her hand into his or her deck. Then, your opponent draws up to 4 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=on_evolve(_evolutionary_swirl_body),
        ),
        Attack(
            title="Fastwave",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_resistance=True, ignore_target_effects=True),
        ),
        Attack(
            title="Hydrosplash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)