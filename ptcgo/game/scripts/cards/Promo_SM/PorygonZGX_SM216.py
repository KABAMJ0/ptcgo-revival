from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def critical_error(ctx):
    """Search the deck for up to 10 cards, discard them, then shuffle."""
    picks = await ctx.search_deck(None, count=10, minimum=0,
                                  prompt="Choose up to 10 cards to discard")
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


async def troubleshooting(ctx):
    """Discard a Special Energy from this Pokemon; if you do, heal 80."""
    from ptcgo.game.attributes import AttrID as _Attr
    source = ctx.source
    specials = [e for e in ctx.attached_energies(source)
                if e.get_attribute(_Attr.IS_SPECIAL_ENERGY)]
    if not specials:
        return
    picks = await ctx.choose_cards(specials, 1, prompt="Discard a Special Energy")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.heal(80, target=source)


card = PokemonCardDef(
    guid="5cc94745-1e52-5413-a42b-0fcb2d451bdf",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZGX.Name",
    display_name="Porygon-Z-GX",
    searchable_by=["Porygon-Z-GX", "Stage 2", "GX", "PorygonZGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=216,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=474,
    abilities=[
        Ability(
            title="Troubleshooting",
            game_text="Once during your turn (before your attack), you may discard a Special Energy from this Pok\u00e9mon. If you do, heal 80 damage from it.",
            activation=Activations.ONCE_PER_TURN,
            effect=troubleshooting,
        ),
        Attack(
            title="Abnormal Overheating",
            game_text="This Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=condition_attack(SpecialConditions.BURNED, self_conditions=(SpecialConditions.BURNED,)),
        ),
        Attack(
            title="Critical Error-GX",
            game_text="Search your deck for up to 10 cards and discard them. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=critical_error,
        ),
    ],
)