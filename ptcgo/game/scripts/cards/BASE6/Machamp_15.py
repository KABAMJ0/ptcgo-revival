from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.session.passives import Passive
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class StrikesBackPassive(Passive):
    """10 damage back on the attacking Pokemon, unmodified, even on a Knock
    Out; off while Machamp is already affected by a Special Condition."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        if target.get_attribute(AttrID.SPECIAL_CONDITIONS) or []:
            return None
        if calc.attacker is not None:
            await ctx.deal_damage(10, target=calc.attacker,
                                  apply_modifiers=False)
        return None


card = PokemonCardDef(
    guid="0b162c66-eba8-553c-b6fb-2d32cdccbd52",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Strikes Back",
            game_text="Whenever your opponent's attack damages Machamp (even if Machamp is Knocked Out), this power does 10 damage to the attacking Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power can't be used if Machamp is already affected by a Special Condition when your opponent attacks.",
            passive=StrikesBackPassive(),
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)