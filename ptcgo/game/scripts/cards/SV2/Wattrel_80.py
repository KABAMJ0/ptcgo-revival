from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5789af7-d1f1-518d-839f-4cc437b5910c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    display_name="Wattrel",
    searchable_by=["Wattrel", "Basic", "Wattrel"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=940,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="United Wings",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the United Wings attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)