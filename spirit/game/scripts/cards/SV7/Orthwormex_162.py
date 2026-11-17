from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92980934-c58c-5a9d-9d9b-09654b4d4d62",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthwormex.Name",
    display_name="Orthworm ex",
    searchable_by=["Orthworm ex", "Basic", "ex", "Orthwormex"],
    subtypes=["Basic", "ex"],
    collector_number=162,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=968,
    abilities=[
        Ability(
            title="Pummeling Payback",
            game_text="If this Pok\u00e9mon is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon for each Metal Energy attached to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Tomb",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=unimplemented,
        ),
    ],
)