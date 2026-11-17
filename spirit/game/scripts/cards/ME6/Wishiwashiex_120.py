from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59abb572-37af-5a6b-b7af-dfa12417a426",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashiex.Name",
    display_name="Wishiwashi ex",
    searchable_by=["Wishiwashi ex", "Basic", "ex", "Wishiwashiex"],
    subtypes=["Basic", "ex"],
    collector_number=120,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Oceanic Gain",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may use this Ability. Heal 50 damage from this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
        ),
    ],
)