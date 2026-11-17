from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d859838-dd17-562c-a2e6-23bbbe11ff96",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FanRotom.Name",
    display_name="Fan Rotom",
    searchable_by=["Fan Rotom", "Basic", "FanRotom"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Fan Call",
            game_text="Once during your first turn, you may search your deck for up to 3 Colorless Pok\u00e9mon with 100 HP or less, reveal them, and put them into your hand. Then, shuffle your deck. You can't use more than 1 Fan Call Ability during your turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Assault Landing",
            game_text="If there is no Stadium in play, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)