from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="9a9fa1d8-5a9c-5ea2-b705-d806a34dd825",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Metallic Lift",
            game_text="If Metang has any Metal Energy attached to it, the Retreat Cost for Metang is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="Does 40 damage plus 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 10, base=40),
        ),
    ],
)