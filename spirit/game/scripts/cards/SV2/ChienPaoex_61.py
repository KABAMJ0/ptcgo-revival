from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ecbeb00-9d7a-50bb-b20e-95241f459bd8",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPaoex.Name",
    display_name="Chien-Pao ex",
    searchable_by=["Chien-Pao ex", "Basic", "ex", "ChienPaoex"],
    subtypes=["Basic", "ex"],
    collector_number=61,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1002,
    abilities=[
        Ability(
            title="Shivery Chill",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may search your deck for up to 2 Basic Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Hail Blade",
            game_text="You may discard any amount of Water Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)