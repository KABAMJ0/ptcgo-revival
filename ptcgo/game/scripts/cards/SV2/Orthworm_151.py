from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ad819336-17bf-5795-aedb-bee4a428f1e1",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name",
    display_name="Orthworm",
    searchable_by=["Orthworm", "Basic", "Orthworm"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=968,
    abilities=[
        Ability(
            title="Nutritional Iron",
            game_text="If this Pok\u00e9mon has 3 or more Metal Energy attached, it gets +100 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Shoot Through",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)