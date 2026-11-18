from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="47d962dd-57e0-551b-8616-5444a6127d6e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawfex.Name",
    display_name="Klawf ex",
    searchable_by=["Klawf ex", "Basic", "ex", "Klawfex"],
    subtypes=["Basic", "ex"],
    collector_number=120,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Ability(
            title="Counterattacking Pincer",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), discard an Energy from the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Falling Press",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)