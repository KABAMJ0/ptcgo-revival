from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

async def _half_remaining_hp(ctx):
    """Damage equal to half the Defending Pokemon's remaining HP, rounded up to 10."""
    defender = ctx.defender
    if defender is None:
        return
    remaining = defender.get_attribute(AttrID.HP, 0) or 0
    await ctx.deal_damage(((remaining // 2) + 9) // 10 * 10)

card = PokemonCardDef(
    guid="5728f428-dfb0-580a-932b-46cbc44637dc",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Super Fang",
            game_text="Does damage to the Defending Pok\u00e9mon equal to half the Defending Pok\u00e9mon's remaining HP (rounded up to the nearest 10).",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_half_remaining_hp,
        ),
    ],
)