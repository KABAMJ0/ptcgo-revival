from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="403e9907-4836-582d-92ab-997cef38457f",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1", "Crawdaunt"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Ability(
            title="Power Pinchers",
            game_text="As long as Crawdaunt is your Active Pok\u00e9mon, when any of your Active Pok\u00e9mon does damage to the Defending Pok\u00e9mon, the attack does 10 more damage (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Guillotine",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)