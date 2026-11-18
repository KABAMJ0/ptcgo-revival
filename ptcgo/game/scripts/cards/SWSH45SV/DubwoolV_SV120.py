from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dd7b6ef0-badc-5056-a187-19fea3d47c52",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DubwoolV.Name",
    display_name="Dubwool V",
    searchable_by=["Dubwool V", "Basic", "V", "DubwoolV"],
    subtypes=["Basic", "V"],
    collector_number=120,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=832,
    abilities=[
        Ability(
            title="Soft Wool",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)