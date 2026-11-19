from ptcgo.game.card_effects.pokemon import is_pokemon_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.attributes import SpecialConditions, AttrID


async def _carry_off_peek_and_pick(ctx):
    results = await ctx.flip_coins(1, "Carry Off")
    if not (results and results[0]):
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    candidates = [card for card in ctx.hand(ctx.opponent_id) if is_pokemon_card(card)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Pokémon from your opponent's hand to shuffle into their deck")
    if picks:
        await ctx.shuffle_into_deck(picks)


async def _double_cross(ctx):
    results = await ctx.flip_coins(2, "Double Cross")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(40 * heads)
    if heads == 0 and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="6caf0b46-9ff0-5679-9976-c460d8aec328",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Carry Off",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at your opponent's hand. If your opponent has any Baby Pok\u00e9mon, Basic Pok\u00e9mon, or Evolution cards there, choose 1 of them. Your opponent shuffles that card into his or her deck. This power can't be used if Crobat is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=_carry_off_peek_and_pick,
        ),
        Attack(
            title="Double Cross",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads. If both of them are tails, the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=_double_cross,
        ),
    ],
)