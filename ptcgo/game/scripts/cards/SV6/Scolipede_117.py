from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID


async def life_squeeze(ctx):
    """Put damage counters on the opponent's Active until its remaining HP is 10."""
    target = ctx.defender
    if target is None:
        return
    current = target.get_attribute(AttrID.HP, 0)
    amount = current - 10
    if amount > 0:
        await ctx.deal_damage(amount, target=target, as_counters=True)


card = PokemonCardDef(
    guid="89ad75c7-861a-5bd8-ba29-a43ab2664d1d",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name",
    display_name="Scolipede",
    searchable_by=["Scolipede", "Stage 2", "Scolipede"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Dastardly Jab",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=life_squeeze,
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)