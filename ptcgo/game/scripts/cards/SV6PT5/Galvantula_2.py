from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b264b298-b27e-5f99-8cbe-c669a30b0136",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Ability(
            title="Compound Eyes",
            game_text="Attacks used by this Pok\u00e9mon do 50 more damage to your opponent's Active Pok\u00e9mon that has an Ability (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Shocking Web",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)