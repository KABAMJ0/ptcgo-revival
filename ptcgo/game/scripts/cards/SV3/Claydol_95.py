from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import AttrID


async def _kaboom_doll(ctx):
    target = ctx.opponent_active()
    if target is None:
        return
    counters = max(0, (target.get_attribute(AttrID.HP, 0) - 10) // 10)
    if counters <= 0:
        return
    await ctx.place_damage_counters(counters, [target])
    await ctx.deal_damage(120, target=ctx.source, apply_modifiers=False)


card = PokemonCardDef(
    guid="80e1630f-2a99-529b-b71d-59d2f8ac71de",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Kaboom Doll",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10. If you placed any damage counters in this way, this attack also does 120 damage to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_kaboom_doll,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)