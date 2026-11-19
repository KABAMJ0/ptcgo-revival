from ptcgo.game.card_effects.attacks_common import damage_reduction_on_self, damage_counters_on
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d24de3c-258a-50d9-96c6-62ce2bcdc02d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1", "Cetitan"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Sweeping Tackle",
            game_text="This attack does 20 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            damage_operator="-",
            effect=damage_reduction_on_self(per=20, count_fn=damage_counters_on("self")),
        ),
    ],
)