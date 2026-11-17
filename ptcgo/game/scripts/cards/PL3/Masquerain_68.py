from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e69bbdf8-1a48-5435-a1c3-8c952f193b35",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Ability(
            title="Intimidating Pattern",
            game_text="As long as Masquerain is your Active Pok\u00e9mon, any damage done by an opponent's attack is reduced by 20 (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Skim Attack",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)