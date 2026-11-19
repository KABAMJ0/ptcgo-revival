from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="8c2d5fc8-8dad-5d28-b997-a01d1975c236",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    display_name="Dewott",
    searchable_by=["Dewott", "Stage 1", "Dewott"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
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