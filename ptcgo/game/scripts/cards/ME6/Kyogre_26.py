from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91f9aa43-ca07-5e9e-8cc7-cf5ab94264ac",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Brutal Whirlpool",
            game_text="If a Stadium that has \"Legendary\" in its name is in play, this attack also does 50 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)