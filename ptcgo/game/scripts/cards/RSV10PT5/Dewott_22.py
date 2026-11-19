from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7fa425b6-9dca-50c2-87fc-6f59c9f8d6d9",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    display_name="Dewott",
    searchable_by=["Dewott", "Stage 1", "Dewott"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    family_id=501,
    abilities=[
        Attack(
            title="Energized Shell",
            game_text="This attack does 30 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy("self"), 30),
        ),
    ],
)