from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_prizes_taken, damage_per


async def huge_bite(ctx):
    """260, or only 30 when the Defending Pokemon already has damage on it."""
    defender = ctx.defender
    damaged = defender is not None and \
        defender.get_attribute(AttrID.HP, 0) < ctx.max_hp(defender)
    await ctx.deal_damage(30 if damaged else 260)


card = PokemonCardDef(
    guid="334543ba-4aa4-59ad-84ea-cfc803877e55",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMawileex.Name",
    display_name="Mega Mawile ex",
    searchable_by=["Mega Mawile ex", "Basic", "MEGA", "ex", "MegaMawileex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=162,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=303,
    abilities=[
        Attack(
            title="Gobble Down",
            game_text="This attack does 80 damage for each Prize card you have taken.",
            cost={PokemonTypes.METAL: 2},
            damage=80,
            damage_operator="x",
            effect=damage_per(count_prizes_taken("mine"), 80),
        ),
        Attack(
            title="Huge Bite",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack's base damage is 30.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=huge_bite,
        ),
    ],
)