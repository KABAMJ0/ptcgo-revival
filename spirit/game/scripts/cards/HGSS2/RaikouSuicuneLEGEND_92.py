from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="277f5c0d-b9ff-57a9-aa58-b0001053908e",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaikouSuicuneLEGEND.Name",
    display_name="Raikou & Suicune LEGEND",
    searchable_by=["Raikou & Suicune LEGEND", "LEGEND", "RaikouSuicuneLEGEND"],
    subtypes=["LEGEND"],
    collector_number=92,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Thunderbolt Spear",
            game_text="Raikou & Suicune LEGEND does 50 damage to itself and don't apply Weakness to this damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Gain",
            game_text="Remove 5 damage counters from Raikou & Suicune LEGEND.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)