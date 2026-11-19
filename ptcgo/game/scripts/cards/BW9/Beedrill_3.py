from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, \
    SpecialConditions


async def swift_sting(ctx):
    """20 damage; at full HP it is 60 and the Defending Pokemon is Confused
    and Poisoned."""
    source = ctx.source
    full_hp = source is not None and \
        source.get_attribute(AttrID.HP, 0) >= ctx.max_hp(source)
    await ctx.deal_damage(20 + (40 if full_hp else 0))
    if full_hp:
        for condition in (SpecialConditions.CONFUSED, SpecialConditions.POISONED):
            await ctx.apply_special_condition(ctx.defender, condition)

card = PokemonCardDef(
    guid="2b6898e5-038f-589c-8ddc-0e0868d6678a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Swift Sting",
            game_text="If this Pok\u00e9mon has full HP, this attack does 40 more damage, and the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="+",
            effect=swift_sting,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)