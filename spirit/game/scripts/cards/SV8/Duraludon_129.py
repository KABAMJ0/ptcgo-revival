from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="785b20e3-b4ea-5e06-8519-d9e3fa1bc7d5",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic", "Duraludon"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=884,
    abilities=[
        Attack(
            title="Confront",
            cost={PokemonTypes.METAL: 2},
            damage=50,
        ),
        Attack(
            title="Duralubeam",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)