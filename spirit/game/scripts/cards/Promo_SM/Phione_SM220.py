from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="200f0d75-c183-5c24-9c4c-d0964827ab5f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=220,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=489,
    abilities=[
        Ability(
            title="Whirlpool Suction",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon. If you do, discard all cards attached to this Pok\u00e9mon and put it on the bottom of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)