from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5d603a0-f5bd-50ff-ac1a-ed4543258de2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    display_name="Snubbull",
    searchable_by=["Snubbull", "Basic", "Snubbull"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=209,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)