from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import gust_then
from ptcgo.game.session.effects import full_stack


async def _poison_new_defender(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.POISONED)


async def _spit_squall(ctx):
    """The opponent puts the Defending Pokemon and its whole stack into
    their hand."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    hand = ctx.board.find_player_area(defender.owning_player_id, "hand")
    if hand is None:
        return
    for card in full_stack(defender):
        ctx.board.move_card(card.entity_id, hand.entity_id)


card = PokemonCardDef(
    guid="452c164c-1029-5c52-a72a-acf8401510dc",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=455,
    abilities=[
        Attack(
            title="Lure Poison",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=gust_then(_poison_new_defender),
        ),
        Attack(
            title="Spit Squall",
            game_text="Your opponent puts the Defending Pok\u00e9mon and all cards attached to it into his or her hand.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=_spit_squall,
        ),
    ],
)