from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="df2fc94c-413d-504f-9321-3c0489001976",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Clairvoyance",
            game_text="Your opponent plays with his or her hand face up. This power stops working while Omanyte is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Omanyte but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per_extra_energy(
                per_energy=10, energy_type=PokemonTypes.WATER, cap=20, base=10),
        ),
    ],
)