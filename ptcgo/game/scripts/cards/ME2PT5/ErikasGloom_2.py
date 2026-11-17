from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6f1ace4a-b257-5301-bc4f-48d0a0d3f088",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    display_name="Erika's Gloom",
    searchable_by=["Erika's Gloom", "Stage 1", "ErikasGloom"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)