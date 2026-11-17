from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="302891f2-e3c7-5860-be56-4b92a0ee64d5",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogiex.Name",
    display_name="Okidogi ex",
    searchable_by=["Okidogi ex", "Basic", "ex", "Okidogiex"],
    subtypes=["Basic", "ex"],
    collector_number=90,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Poisonous Musculature",
            game_text="Search your deck for up to 2 Basic Darkness Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck. If you attached Energy to a Pok\u00e9mon in this way, this Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Chain-Crazed",
            game_text="If this Pok\u00e9mon is Poisoned, this attack does 130 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)