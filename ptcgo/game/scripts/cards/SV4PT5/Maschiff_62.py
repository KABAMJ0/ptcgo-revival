from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93dc5a77-3dc8-504b-bc73-6feca4d4518e",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    display_name="Maschiff",
    searchable_by=["Maschiff", "Basic", "Maschiff"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=942,
    abilities=[
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)