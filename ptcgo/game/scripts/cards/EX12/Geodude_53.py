from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage


async def selfdestruct(ctx):
    """10 damage to each Benched Pokemon (both sides, no Weakness or
    Resistance for Benched Pokemon), then 50 damage to this Pokemon."""
    await spread_damage(10, side="both")(ctx)
    if ctx.attacker is not None:
        await ctx.deal_damage(50, target=ctx.attacker,
                              apply_modifiers=False)


card = PokemonCardDef(
    guid="8f025f0d-370f-5e9a-bcf8-be4ed2d5baa9",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    display_name="Geodude",
    searchable_by=["Geodude", "Basic", "Geodude"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=74,
    abilities=[
        Attack(
            title="Selfdestruct",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Geodude does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=selfdestruct,
        ),
    ],
)