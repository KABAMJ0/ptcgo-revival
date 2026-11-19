from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID


async def destructive_tsunami(ctx):
    """On heads 40 to each of their Pokemon, on tails 40 to each of mine (no
    Weakness or Resistance on the Bench)."""
    heads = await ctx.flip_coins(1, "Destructive Tsunami")
    pool = list(ctx.opponent_pokemon_in_play()) if heads and heads[0] \
        else list(ctx.my_pokemon_in_play())
    for pokemon in pool:
        await ctx.deal_damage(40, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="d6d14873-200e-5db5-95e2-95b6555c39c5",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Destructive Tsunami",
            game_text="Flip a coin. If heads, this attack does 40 damage to each of your opponent's Pok\u00e9mon. If tails, this attack does 40 damage to each of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            effect=destructive_tsunami,
        ),
    ],
)