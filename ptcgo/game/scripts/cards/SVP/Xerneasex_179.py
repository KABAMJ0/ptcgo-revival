from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7a680dd9-10c7-5d49-aed5-acec3ea007a0",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneasex.Name",
    display_name="Xerneas ex",
    searchable_by=["Xerneas ex", "Basic", "ex", "Xerneasex"],
    subtypes=["Basic", "ex"],
    collector_number=179,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Rising Horns",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)