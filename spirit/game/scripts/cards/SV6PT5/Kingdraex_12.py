from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79347834-d2b9-510c-adb3-5fd83a552da6",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdraex.Name",
    display_name="Kingdra ex",
    searchable_by=["Kingdra ex", "Stage 2", "ex", "Kingdraex"],
    subtypes=["Stage 2", "ex"],
    collector_number=12,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="King's Order",
            game_text="Put up to 3 Water Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 50 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)