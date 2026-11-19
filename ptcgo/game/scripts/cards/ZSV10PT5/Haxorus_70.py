from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_basic_pokemon

async def oppressing_sandstorm(ctx):
    """If your opponent's Active Pokemon is a Basic Pokemon, it is Knocked Out."""
    defender = ctx.defender
    if defender is not None and is_basic_pokemon(defender):
        await ctx.knock_out(defender)

card = PokemonCardDef(
    guid="9eae99c1-fab3-51b5-ac19-a27fbec8a7f1",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Axe Blast",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=oppressing_sandstorm,
        ),
    ],
)