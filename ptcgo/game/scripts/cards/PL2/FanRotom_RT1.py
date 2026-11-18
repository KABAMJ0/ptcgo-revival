from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="808ecdc0-2ba1-5b9d-8cca-8cbaa3c21ab8",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FanRotom.Name",
    display_name="Fan Rotom",
    searchable_by=["Fan Rotom", "Basic", "FanRotom"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Ability(
            title="Fan Shift",
            game_text="Once during your turn (before your attack), you may use this power. Fan Rotom's type is Colorless until the end of your turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Spin Storm",
            game_text="Flip a coin. If heads, your opponent returns the Defending Pok\u00e9mon and all cards attached to it to his or her hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Air Slash",
            game_text="Flip a coin. If tails, discard an Energy attached to Fan Rotom.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=unimplemented,
        ),
    ],
)