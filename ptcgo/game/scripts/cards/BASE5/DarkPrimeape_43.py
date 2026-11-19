from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import Passive, carrier_pokemon


class FrenzyPassive(Passive):
    """While the carrier is Confused its attacks do 30 more (even to itself)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or calc.attacker is not holder:
            return
        name = "Confused"
        from ptcgo.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions
        if CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED] \
                in (holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            calc.amount += 30


_frenzy = FrenzyPassive()


async def frenzied_attack(ctx):
    """Printed 40, then Dark Primeape is Confused."""
    from ptcgo.game.attributes import SpecialConditions
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="d034d073-5446-5d3e-8b8c-0b2cfe55a37e",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPrimeape.Name",
    display_name="Dark Primeape",
    searchable_by=["Dark Primeape", "Stage 1", "DarkPrimeape"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="If Dark Primeape does any damage while it's Confused (even to itself), it does 30 more damage.",
            passive=_frenzy,
        ),
        Attack(
            title="Frenzied Attack",
            game_text="Dark Primeape is now Confused (after doing damage).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            effect=frenzied_attack,
        ),
    ],
)