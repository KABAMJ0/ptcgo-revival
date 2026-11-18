from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="458edbc1-cfd2-56cb-9d43-bb680e8322d9",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    display_name="Nidorina",
    searchable_by=["Nidorina", "Stage 1", "Nidorina"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Jump Tackle",
            game_text="Nidorina does 10 damage to itself, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Stress Poison",
            game_text="If Nidorina has any damage counters on it, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)