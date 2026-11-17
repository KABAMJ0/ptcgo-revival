from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="190b7a2f-b33d-587c-8c1b-7d589606c432",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MawileV.Name",
    display_name="Mawile V",
    searchable_by=["Mawile V", "Basic", "V", "MawileV"],
    subtypes=["Basic", "V"],
    collector_number=17,
    set_code="SWSH12TG",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=303,
    abilities=[
        Attack(
            title="Pouty Slap",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Chomp Down",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)