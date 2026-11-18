from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e8a8a506-3550-53f4-a14b-806f51831b98",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KricketuneV.Name",
    display_name="Kricketune V",
    searchable_by=["Kricketune V", "Basic", "V", "KricketuneV"],
    subtypes=["Basic", "V"],
    collector_number=12,
    set_code="SWSH12TG",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=402,
    abilities=[
        Ability(
            title="Exciting Stage",
            game_text="Once during your turn, you may draw cards until you have 3 cards in your hand. If this Pok\u00e9mon is in the Active Spot, you may draw cards until you have 4 cards in your hand instead. You can't use more than 1 Exciting Stage Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(80),
        ),
    ],
)