from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9445aa63-cc4a-57cc-b0f9-a2687b43efe6",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic", "Tympole"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=535,
    abilities=[
        Attack(
            title="Get Loud",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Round",
            game_text="This attack does 10 damage times the number of your Pok\u00e9mon in play that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)