from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f00e57eb-ee45-51c3-8f3c-8c1eb263b5c2",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=108,
    abilities=[
        Attack(
            title="Tongue Wrap",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)