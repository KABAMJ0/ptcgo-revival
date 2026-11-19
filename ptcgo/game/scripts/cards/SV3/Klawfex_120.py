from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon


class CounterattackingPincerPassive(Passive):
    """Active and damaged by an opposing attack: discard an Energy from the attacker."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier_pokemon(carrier) or not is_in_active_spot(target):
            return None
        attacker = calc.attacker
        if attacker is None or not ctx.attached_energies(attacker):
            return None
        await ctx.discard_energy_from(
            attacker, 1,
            prompt="Choose an Energy to discard from the Attacking Pok\u00e9mon")
        return None


card = PokemonCardDef(
    guid="47d962dd-57e0-551b-8616-5444a6127d6e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawfex.Name",
    display_name="Klawf ex",
    searchable_by=["Klawf ex", "Basic", "ex", "Klawfex"],
    subtypes=["Basic", "ex"],
    collector_number=120,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Ability(
            title="Counterattacking Pincer",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), discard an Energy from the Attacking Pok\u00e9mon.",
            passive=CounterattackingPincerPassive(),
        ),
        Attack(
            title="Falling Press",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=flip_bonus(80),
        ),
    ],
)