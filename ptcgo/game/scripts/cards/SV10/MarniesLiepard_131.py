from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35014ea7-a5f3-512b-af92-36725997915f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesLiepard.Name",
    display_name="Marnie's Liepard",
    searchable_by=["Marnie's Liepard", "Stage 1", "MarniesLiepard"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesPurrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Pointy Claws",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)