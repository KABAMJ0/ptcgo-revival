from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.passives_common import composed


async def _peek_opponent_hand(ctx):
    await ctx.reveal_hand(of_player=ctx.opponent_id)


def _energy_in_opponent_hand(ctx):
    return sum(1 for card in ctx.hand(ctx.opponent_id) if is_energy_card(card))


async def _shuffle_attack(ctx):
    await ctx.deal_damage(40)
    defender = ctx.defender
    if defender is None:
        return
    count = len(ctx.attached_energies(defender))
    if count <= 0:
        return
    await ctx.reorder_deck_top(count, ctx.opponent_id,
                               "Put those cards back on top in any order")

from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb636a8e-22fb-540d-b17b-82c1912cafc4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Bursting Hand",
            game_text="Look at your opponent's hand. This attack does 10 damage times the number of Energy cards there.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=composed(_peek_opponent_hand,
                            damage_per(_energy_in_opponent_hand, 10)),
        ),
        Attack(
            title="Shuffle Attack",
            game_text="Look at a number of cards on top of your opponent's deck equal to the number of Energy cards attached to the Defending Pok\u00e9mon. Put those cards in any order, and then put them back on top of your opponent's deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_shuffle_attack,
        ),
    ],
)