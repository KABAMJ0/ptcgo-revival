from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc2babe9-1399-534b-b052-92f732835639",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Dede-Flash",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 60 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)