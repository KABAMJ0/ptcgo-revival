from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f317507-b3e6-55c1-abb9-40d1f14214a5",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1", "Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Ability(
            title="Thicket Body",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Loom Over",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)