from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _icicle_sole(ctx):
    """Counters on 1 of their Pokemon until 30 HP remain."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pok\u00e9mon")
    if target is None:
        return
    counters = (target.get_attribute(AttrID.HP, 0) - 30) // 10
    if counters > 0:
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)

card = PokemonCardDef(
    guid="7f84de08-f1e9-5e42-ba29-630c5e57e20b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareenaex.Name",
    display_name="Tsareena ex",
    searchable_by=["Tsareena ex", "Stage 2", "Tera", "ex", "Tsareenaex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=220,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Icicle Sole",
            game_text="Put damage counters on 1 of your opponent's Pok\u00e9mon until its remaining HP is 30.",
            cost={PokemonTypes.GRASS: 1},
            effect=_icicle_sole,
        ),
        Attack(
            title="Trop Kick",
            game_text="Heal 30 damage from this Pok\u00e9mon, and it recovers from all Special Conditions.",
            cost={PokemonTypes.GRASS: 2},
            damage=180,
            effect=unimplemented,
        ),
    ],
)