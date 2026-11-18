from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="791f98ee-8e78-5808-bd44-0266352433ba",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic", "Koffing"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Offensive Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Gas Bomb",
            game_text="Koffing does 30 damage to itself, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)