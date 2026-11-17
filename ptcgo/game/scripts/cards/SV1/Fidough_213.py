from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b959a887-3e79-51fd-bf5a-4d634ff46ebf",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    display_name="Fidough",
    searchable_by=["Fidough", "Basic", "Fidough"],
    subtypes=["Basic"],
    collector_number=213,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=926,
    abilities=[
        Attack(
            title="Springy",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)