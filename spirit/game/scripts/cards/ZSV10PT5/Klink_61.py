from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5935395-5c80-5618-9674-94e7380909d7",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic", "Klink"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=599,
    abilities=[
        Attack(
            title="Hard Gears",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)