from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6ab4528-d74c-5a38-a467-51d77467dece",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMabosstiffex.Name",
    display_name="Arven's Mabosstiff ex",
    searchable_by=["Arven's Mabosstiff ex", "Stage 1", "ex", "ArvensMabosstiffex"],
    subtypes=["Stage 1", "ex"],
    collector_number=139,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMaschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Vigorous Tackle",
            game_text="If this Pok\u00e9mon has no damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Boss Headbutt",
            game_text="During your next turn, this Pok\u00e9mon can't use Boss Headbutt.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)