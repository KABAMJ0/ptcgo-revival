from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if


def _defender_has_more_energy(ctx):
    defender, attacker = ctx.defender, ctx.attacker
    if defender is None or attacker is None:
        return False
    return len(ctx.attached_energies(defender)) > len(ctx.attached_energies(attacker))


async def _fish_out(ctx):
    for player_id in (ctx.opponent_id, ctx.player_id):
        pile = list(ctx.discard_pile(player_id))
        if not pile:
            continue
        picks = await ctx.choose_cards(
            pile, 3, minimum=0, player_id=player_id,
            prompt="Choose up to 3 cards to shuffle into your deck")
        if picks:
            await ctx.shuffle_into_deck(picks, player_id)


card = PokemonCardDef(
    guid="b374b586-dc59-5283-8d31-6e604ba96f4b",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightSlowbro.Name",
    display_name="Light Slowbro",
    searchable_by=["Light Slowbro", "Stage 1", "LightSlowbro"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=80,
    abilities=[
        Attack(
            title="Fish Out",
            game_text="Your opponent may choose up to 3 Baby Pok\u00e9mon, Basic Pok\u00e9mon, and/or Evolution cards from his or her discard pile and shuffle them into his or her deck. Either way, you may do the same.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_fish_out,
        ),
        Attack(
            title="Splash About",
            game_text="If there are more Energy attached to the Defending Pok\u00e9mon than to Light Slowbro, this attack does 20 damage plus 20 more damage. If not, this attack does 20 damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_defender_has_more_energy, 20),
        ),
    ],
)