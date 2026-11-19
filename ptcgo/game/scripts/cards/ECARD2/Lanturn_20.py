from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_lightning_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _conduction(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_lightning_energy,
        prompt="Choose Lightning Energy to discard from Lanturn")
    heads = await ctx.flip_coins(len(discarded), "Conduction") if discarded else []
    await ctx.deal_damage(30 + 40 * sum(1 for h in heads if h))

card = PokemonCardDef(
    guid="9d7d19f0-1fa7-5f18-874e-4d503846a10f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Conduction",
            game_text="Discard all Lightning Energy cards attached to Lanturn. Flip a number of coins equal to the number of Lightning Energy cards you discarded. This attack does 30 damage plus 40 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=_conduction,
        ),
    ],
)
