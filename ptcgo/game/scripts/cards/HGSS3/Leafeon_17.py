from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="80b9efa0-649d-5dc1-adf1-42a1cd75bec0",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1", "Leafeon"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Miasma Wind",
            game_text="Does 50 damage damage times the number of Special Conditions affecting the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Soothing Scent",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)