from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.attacks_common import conditions_if
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.trainers import card_named_contains


def defender_has(word):
    return lambda ctx: card_named_contains(word)(ctx.defender)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def magma_spurt(ctx):
    """Mill 5 from my deck, then 30 for each Fire or Fighting basic Energy among them."""
    milled = ctx.deck_top(5, player_id=ctx.player_id)
    if not milled:
        return
    await ctx.discard_cards(milled)
    counted = sum(
        1 for card in milled
        if is_basic_energy_card(card)
        and (energy_provides_type(card, PokemonTypes.FIRE.value)
             or energy_provides_type(card, PokemonTypes.FIGHTING.value)))
    if counted:
        await ctx.deal_damage(30 * counted)

card = PokemonCardDef(
    guid="34e6f5e2-679b-5143-9d81-3bcf8aec7f07",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundoom.Name",
    display_name="Team Magma's Houndoom",
    searchable_by=["Team Magma's Houndoom", "Stage 1", "TeamMagmasHoundoom"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If the Defending Pok\u00e9mon is Burned, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Magma Spurt",
            game_text="Discard the top 5 cards from your deck. This attack does 30 damage times the number of Fire and Fighting basic Energy cards discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=magma_spurt,
        ),
    ],
)