from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f44d484-6c7d-549d-aa16-e521eb980bf3",
    key="RU1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skuntank.Name",
    display_name="Skuntank",
    searchable_by=["Skuntank", "Stage 1", "Skuntank"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="RU1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    family_id=435,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 20 damage plus 10 more damage for each damage counter on Skuntank.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=20),
        ),
    ],
)