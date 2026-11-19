from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy


card = PokemonCardDef(
    guid="343aea6f-0da5-58b3-a23a-995f7b349e85",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    display_name="Poliwag",
    searchable_by=["Poliwag", "Basic", "Poliwag"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=60,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Poliwag but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per_extra_energy(10, energy_type=PokemonTypes.WATER, cap=20),
        ),
    ],
)