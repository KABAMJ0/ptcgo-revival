from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage


async def selfdestruct(ctx):
    """10 damage to each Benched Pokemon (both sides, no Weakness or
    Resistance for Benched Pokemon), then 60 damage to this Pokemon."""
    await spread_damage(10, side="both")(ctx)
    if ctx.attacker is not None:
        await ctx.deal_damage(60, target=ctx.attacker,
                              apply_modifiers=False)


card = PokemonCardDef(
    guid="5f56bf14-6194-5ad0-a333-e8e59a6b43fd",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=337,
    abilities=[
        Attack(
            title="Lunar Blast",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Lunatone does 60 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=selfdestruct,
        ),
    ],
)