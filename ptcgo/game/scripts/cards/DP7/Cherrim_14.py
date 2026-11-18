from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91f571d2-b41d-5498-b3f5-f365fd9dc61a",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Sunny Day",
            game_text="Each of your Grass Pok\u00e9mon's and Fire Pok\u00e9mon's attacks does 10 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Salty-sweet Pollen",
            game_text="Remove 2 damage counters from 1 of your Pok\u00e9mon.",
            cost={},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)