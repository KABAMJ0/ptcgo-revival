from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _rock_tackle(ctx):
    """Rock Tackle: printed damage, 10 to itself and this attack locked."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                          ctx.ability.ability_id)

card = PokemonCardDef(
    guid="f335917b-8b2f-584f-b5ec-315ef27ee132",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    display_name="Dark Pupitar",
    searchable_by=["Dark Pupitar", "Stage 1", "DarkPupitar"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Rock Tackle",
            game_text="Dark Pupitar does 10 damage to itself. Dark Pupitar can't use this attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            effect=_rock_tackle,
        ),
        Attack(
            title="Explosive Evolution",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Then, search your deck for an Evolution card named Dark Tyranitar and put it on Dark Pupitar. (This counts as evolving Dark Pupitar.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)