from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class AttackBoostPassive(Passive):
    """The carrier's attacks do N more damage (dealt side, before W/R)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.attacker):
            calc.amount += self.amount


async def lucha_fight(ctx):
    """Printed damage; during the opponent's next turn the Defending Pokemon's
    attacks do 30 more damage."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(defender, AttackBoostPassive(30))


card = PokemonCardDef(
    guid="922d7854-73de-5b5c-ba27-32d854282807",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Lucha Fight",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            effect=lucha_fight,
        ),
    ],
)