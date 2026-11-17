from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c6f0e43-fe8c-57c2-a563-414b9301ac4b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic", "Seviper"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Shed Skin",
            game_text="Remove 4 damage counters from Seviper.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Bite and Escape",
            game_text="You may switch Seviper with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Paralyze Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)