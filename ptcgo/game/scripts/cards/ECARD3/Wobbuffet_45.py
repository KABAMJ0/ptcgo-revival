from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented


async def _return_attack(ctx):
    results = await ctx.flip_coins(2, "Return Attack")
    if not any(results):
        return
    attacker = ctx.attacker
    if attacker is None:
        return
    counters = (ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0)) // 10
    if counters:
        await ctx.deal_damage(10 * counters)

from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4818bdcc-31ef-56f5-8877-c3d9a58b5de9",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Mirror Coat",
            game_text="If Wobbuffet becomes Poisoned or Burned by the Defending Pok\u00e9mon's attack during your opponent's turn, the Defending Pok\u00e9mon becomes affected by the same Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Return Attack",
            game_text="Flip 2 coins. If either is heads, this attack does 10 damage times the number of damage counters on Wobbuffet.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=_return_attack,
        ),
    ],
)