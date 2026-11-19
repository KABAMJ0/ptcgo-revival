from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def leech_seed(ctx):
    """20; if it damaged the Defending Pokemon, one counter comes off Cherubi."""
    dealt = await ctx.deal_damage(20)
    if dealt > 0 and ctx.attacker is not None:
        await ctx.heal(10, ctx.attacker)

card = PokemonCardDef(
    guid="86189593-002d-5d8c-af32-8aaf9f8d4cdc",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    display_name="Cherubi",
    searchable_by=["Cherubi", "Basic", "Cherubi"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="POP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=420,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Leech Seed",
            game_text="If this attack does any damage to the Defending Pok\u00e9mon (after applying Weakness and Resistance), remove 1 damage counter from Cherubi.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=leech_seed,
        ),
    ],
)