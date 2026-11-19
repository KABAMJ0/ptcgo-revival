from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _Transparency(Passive):
    """Whenever an attack does anything to the holder, flip a coin: heads
    prevents all effects of that attack, including damage. Off while
    afflicted. The flag is cleared by attack_followup at the end of every
    attack so a heads flip can never leak into the next one."""

    def __init__(self):
        self._shielded = False

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if calc.target is not holder:
            return None
        if holder.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return None
        heads = await ctx.flip_coins(1, "Transparency", source=holder)
        if heads and heads[0]:
            self._shielded = True
            calc.prevented = True
            return 0
        return None

    def blocks_attack_effects(self, target, carrier, attacker=None, board=None):
        return self._shielded and target is carrier_pokemon(carrier)

    async def attack_followup(self, ctx, carrier):
        self._shielded = False


_transparency = _Transparency()

card = PokemonCardDef(
    guid="9af10106-a072-5808-aba1-d82efdfb20ad",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1", "Haunter"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Transparency",
            game_text="Whenever an attack does anything to Haunter, flip a coin. If heads, prevent all effects of that attack, including damage, done to Haunter. This power stops working while Haunter is Asleep, Confused, or Paralyzed.",
            passive=_transparency,
        ),
        Attack(
            title="Nightmare",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)