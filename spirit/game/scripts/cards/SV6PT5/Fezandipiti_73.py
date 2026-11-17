from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85380921-f90e-53b6-a96f-59a6e66ea98c",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipiti.Name",
    display_name="Fezandipiti",
    searchable_by=["Fezandipiti", "Basic", "Fezandipiti"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Ability(
            title="Adrena-Pheromone",
            game_text="If this Pok\u00e9mon has any Darkness Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Feather",
            game_text="This attack does 30 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)