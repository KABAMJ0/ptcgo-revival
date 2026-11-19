from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

async def dark_mist(ctx):
    """Put 1 of the opponent's Benched Pokemon, with everything attached, into
    their hand."""
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokemon")
    if target is None:
        return
    await ctx.put_in_hand([target] + list(getattr(target, "children", None) or []),
                          reveal=False)


card = PokemonCardDef(
    guid="22356117-cc47-58bb-a78e-59026305aa46",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaGX.Name",
    display_name="Greninja-GX",
    searchable_by=["Greninja-GX", "Stage 2", "GX", "GreninjaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=197,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=658,
    abilities=[
        Ability(
            title="Elusive Master",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is the last card in your hand, you may play it onto your Bench. If you do, draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Mist Slash",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Dark Mist-GX",
            game_text="Put 1 of your opponent's Benched Pok\u00e9mon and all cards attached to it into your opponent's hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=dark_mist,
        ),
    ],
)