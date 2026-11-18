from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1907ce3-a6e8-5b27-8601-77c5f0cd1781",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Centrifugal Force",
            game_text="Does 20 damage times the number of Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Swirling Ripple",
            game_text="If your opponent has any Water Pok\u00e9mon in play, this attack does 30 damage plus 30 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)