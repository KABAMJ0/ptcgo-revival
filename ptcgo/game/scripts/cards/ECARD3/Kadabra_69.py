from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="709b7bd0-dcb5-535b-8590-27e176a2f98f",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1", "Kadabra"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Nightmare",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)