from ptcgo.game.card_effects.passives_common import rewrite_energy_types_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce7ebef5-d739-5ff6-93df-219372a58072",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="DP4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Wild Growth",
            game_text="Each basic Grass Energy card attached to your Grass Pok\u00e9mon provides GrassGrass Energy instead. You can't use more than 1 Wild Growth Pok\u00e9-Body each turn.",
            passive=rewrite_energy_types_passive([PokemonTypes.GRASS.value] * 2, protects="team", basic_only=True, holder_types=[PokemonTypes.GRASS.value]),
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)