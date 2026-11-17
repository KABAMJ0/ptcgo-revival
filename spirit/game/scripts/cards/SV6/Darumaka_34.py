from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28d72c3f-8ef1-5162-b756-ddf8faa165f7",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic", "Darumaka"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Fire Tackle",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)