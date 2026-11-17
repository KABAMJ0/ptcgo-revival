from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9bc76c5c-76d4-5fde-a27a-6e007d034857",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaVSTAR.Name",
    display_name="Origin Forme Dialga VSTAR",
    searchable_by=["Origin Forme Dialga VSTAR", "VSTAR", "OriginFormeDialgaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=68,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaV.Name",
    family_id=483,
    abilities=[
        Attack(
            title="Metal Blast",
            game_text="This attack does 40 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Star Chronos",
            game_text="Take another turn after this one. (Skip Pok\u00e9mon Checkup.) (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.METAL: 4, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)