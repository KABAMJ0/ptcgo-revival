from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _selfdestruct_recoil(ctx):
    await ctx.deal_damage(50, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="b59ce4e3-34ca-5e8e-a907-e98ffc087f8f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic", "Pineco"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Selfdestruct",
            game_text="This attack does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Pineco does 50 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=spread_damage(10, side="both", also_base=True,
                                 also=_selfdestruct_recoil),
        ),
    ],
)