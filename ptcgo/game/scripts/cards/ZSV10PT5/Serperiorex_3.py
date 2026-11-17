from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1ab2049-13df-56e1-8cfe-acf0d7b229ce",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperiorex.Name",
    display_name="Serperior ex",
    searchable_by=["Serperior ex", "Stage 2", "ex", "Serperiorex"],
    subtypes=["Stage 2", "ex"],
    collector_number=3,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Regal Cheer",
            game_text="Attacks used by your Pok\u00e9mon do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Command the Grass",
            game_text="You may search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)