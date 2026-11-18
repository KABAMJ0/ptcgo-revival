from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="07ffc088-96ab-568a-b621-c0f0273dcf38",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    display_name="Cherubi",
    searchable_by=["Cherubi", "Basic", "Cherubi"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=420,
    abilities=[
        Attack(
            title="Growth",
            game_text="Attach a Grass Energy from your hand to Cherubi.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)