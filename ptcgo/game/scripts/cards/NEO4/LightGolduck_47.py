from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.session.effects import is_special_energy


def _special_energy_on_defender(ctx):
    defender = ctx.defender
    if defender is None:
        return 0
    return sum(1 for energy in ctx.attached_energies(defender)
               if is_special_energy(energy))


async def _flipper_stroke(ctx):
    for player_id in (ctx.opponent_id, ctx.player_id):
        top = ctx.deck_top(3, player_id=player_id)
        basic = [card for card in top if is_basic_energy_card(card)]
        if basic:
            picks = await ctx.choose_cards(
                basic, len(basic), minimum=0, player_id=player_id,
                prompt="Choose basic Energy cards to put into your hand")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck(player_id)


card = PokemonCardDef(
    guid="0a59ac17-614c-59d5-ad47-ba01c09a6858",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightGolduck.Name",
    display_name="Light Golduck",
    searchable_by=["Light Golduck", "Stage 1", "LightGolduck"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Flipper Stroke",
            game_text="Your opponent looks at the top 3 cards of his or her deck. If any of them are basic Energy cards, he or she may show any number of them to you and put them into his or her hand. You do the same. Either way, each player shuffles his or her deck.",
            cost={PokemonTypes.WATER: 1},
            effect=_flipper_stroke,
        ),
        Attack(
            title="Core Blast",
            game_text="This attack does 30 damage plus 20 more damage for each Special Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(_special_energy_on_defender, 20, base=30),
        ),
    ],
)