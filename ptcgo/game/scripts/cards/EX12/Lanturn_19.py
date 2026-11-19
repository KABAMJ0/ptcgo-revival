from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy


card = PokemonCardDef(
    guid="32dabc1a-6a0c-5eb9-9535-7a138fc581a9",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Lanturn has any Water Energy attached to it, Lanturn is both Water and Lightning type.",
            effect=unimplemented,
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Water Gun",
            game_text="Does 40 damage plus 20 more damage for each Water Energy attached to Lanturn but not used to pay for this attack's Energy cost. You can't add more then 40 damage in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per_extra_energy(20, PokemonTypes.WATER, cap=40),
        ),
    ],
)