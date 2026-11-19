from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _cold_crush(ctx):
    """Printed 70; you may discard an Energy from this Pokemon, and if you do,
    discard an Energy attached to the Defending Pokemon."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or defender is None or ctx.effects_blocked(defender):
        return
    mine = [e for e in ctx.attached_energies(attacker)]
    if not mine:
        return
    picked = await ctx.choose_cards(mine, 1, minimum=0,
                                    prompt="Discard an Energy from this Pok\u00e9mon?")
    if not picked:
        return
    await ctx.discard_cards(picked)
    await ctx.discard_energy_from(defender, 1,
                                  prompt="Choose Energy to discard from the Defending Pok\u00e9mon")


card = PokemonCardDef(
    guid="2a38a46d-0517-5d37-8403-b8bac40fc7e9",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=395,
    abilities=[
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Cold Crush",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_cold_crush,
        ),
    ],
)