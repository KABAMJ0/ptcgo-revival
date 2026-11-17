from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a2db9f08-3c39-56d1-88bf-8d7b0a5ef1bd",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    display_name="Crobat V",
    searchable_by=["Crobat V", "Basic", "V", "CrobatV"],
    subtypes=["Basic", "V"],
    collector_number=20,
    set_code="SWSH11TG",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=169,
    abilities=[
        Ability(
            title="Dark Asset",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may draw cards until you have 6 cards in your hand. You can't use more than 1 Dark Asset Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Venomous Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)