from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID

async def whisk_away(ctx):
    """Reveal the opponent's hand, put one Pokemon from it on the bottom of
    their deck; if you do, 30 plus 30 damage."""
    from ptcgo.game.attributes import CardType
    cards = await ctx.reveal_hand(ctx.opponent_id)
    pokemon = [c for c in (cards or [])
               if c.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value]
    bounced = False
    if pokemon:
        picked = await ctx.choose_cards(pokemon, 1, prompt="Choose a Pokemon to put on the bottom")
        if picked:
            for card in picked:
                await ctx.put_on_bottom_of_deck(card)
            bounced = True
    await ctx.deal_damage(60 if bounced else 30)


card = PokemonCardDef(
    guid="cc42f256-9d42-50e7-8186-1d6d90d7e61a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=275,
    abilities=[
        Attack(
            title="Whisk Away",
            game_text="Your opponent reveals his or her hand. Choose a Pok\u00e9mon you find there and put it on the bottom your opponent's deck. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=whisk_away,
        ),
        Attack(
            title="Spirit Dance",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)