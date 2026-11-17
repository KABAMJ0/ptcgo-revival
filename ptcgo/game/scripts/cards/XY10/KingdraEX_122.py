from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c8d0af95-dc7e-5b2a-9516-5a21ebe4d585",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KingdraEX.Name",
    display_name="Kingdra-EX",
    searchable_by=["Kingdra-EX", "Basic", "EX", "KingdraEX"],
    subtypes=["Basic", "EX"],
    collector_number=122,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=230,
    abilities=[
        Attack(
            title="Big Storm",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Trail",
            game_text="This attack does 30 more damage for each basic Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)