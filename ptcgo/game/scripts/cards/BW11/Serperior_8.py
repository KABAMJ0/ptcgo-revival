from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def royal_heal(ctx):
    """Pokemon Checkup: heal 10 damage from each of your Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


card = PokemonCardDef(
    guid="6daf14be-98a7-50f3-912f-657434e1c4ea",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Royal Heal",
            game_text="At any time between turns, heal 10 damage from each of your Pok\u00e9mon.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=royal_heal,
        ),
        Attack(
            title="Leaf Tornado",
            game_text="Move as many Grass Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)