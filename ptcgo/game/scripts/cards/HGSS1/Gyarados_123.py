from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1be6022d-e855-599b-89ba-0fe72cdc4d7a",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=123,
    set_code="HGSS1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Thrash",
            game_text="If heads, this attack does 30 damage plus 20 more damage. If tails, Gyarados does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Storm",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)