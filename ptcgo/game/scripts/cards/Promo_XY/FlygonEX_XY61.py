from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cb3be79-f760-5a31-9e7e-13be78899fcf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlygonEX.Name",
    display_name="Flygon-EX",
    searchable_by=["Flygon-EX", "Basic", "EX", "FlygonEX"],
    subtypes=["Basic", "EX"],
    collector_number=61,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=330,
    abilities=[
        Ability(
            title="Voice of the Sands",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Buzz",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)