from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="111a2e2b-7bc4-59c5-8097-e44a66b79a86",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)