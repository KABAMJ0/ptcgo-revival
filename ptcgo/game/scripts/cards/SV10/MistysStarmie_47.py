from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9203381-c2fa-5d40-82fd-9873cfdd94e4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStarmie.Name",
    display_name="Misty's Starmie",
    searchable_by=["Misty's Starmie", "Stage 1", "MistysStarmie"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Abrupt Flash",
            game_text="If this Pok\u00e9mon evolved from Misty's Staryu during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)