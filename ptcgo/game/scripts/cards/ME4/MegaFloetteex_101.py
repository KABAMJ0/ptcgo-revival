from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8c5cf12e-a34e-5983-800b-1687dfc0f30d",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFloetteex.Name",
    display_name="Mega Floette ex",
    searchable_by=["Mega Floette ex", "Basic", "MEGA", "ex", "MegaFloetteex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=101,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=670,
    abilities=[
        Attack(
            title="Gentle Light",
            game_text="Heal 30 damage from each Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Eternity Bloom",
            game_text="Search your deck for up to 4 Basic Psychic Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)