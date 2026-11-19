from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID


async def chain_lightning(ctx):
    """Printed 20, then 10 to every Benched Pokemon of the Defending Pokemon's
    type on both sides - unless the Defending Pokemon is Colorless."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    types = set(defender.get_attribute(AttrID.POKEMON_TYPES) or [])
    if not types or PokemonTypes.COLORLESS.value in types:
        return
    for pid in (ctx.player_id, ctx.opponent_id):
        for pokemon in ctx.board.find_player_area(pid, "bench").children:
            if types & set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
                await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="bf14528a-e0ab-58a5-8e69-49b539484861",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BASE2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=101,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Chain Lightning",
            game_text="If the Defending Pok\u00e9mon isn't Colorless, this attack does 10 damage to each Benched Pok\u00e9mon of the same type as the Defending Pok\u00e9mon (including your own).",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=20,
            effect=chain_lightning,
        ),
    ],
)