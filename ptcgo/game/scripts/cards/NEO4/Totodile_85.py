from ptcgo.game.card_effects.attacks_common import extra_energy_beyond_cost
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _water_gun(ctx):
    """Water Gun: 10 plus 10 per spare Water Energy, capped at 20 more."""
    extra = min(20, 10 * max(0, extra_energy_beyond_cost(ctx, PokemonTypes.WATER)))
    await ctx.deal_damage(10 + extra)

card = PokemonCardDef(
    guid="7338511b-5a91-5b85-bd83-65ebf408883c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic", "Totodile"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=158,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Totodile but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=_water_gun,
        ),
    ],
)