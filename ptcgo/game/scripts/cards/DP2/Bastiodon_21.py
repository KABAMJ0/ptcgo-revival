from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot, prevent_damage_when


def _protects_own_bench(calc, carrier) -> bool:
    return (calc.target.owning_player_id == carrier.owning_player_id
            and not is_in_active_spot(calc.target))


card = PokemonCardDef(
    guid="5a25c9f1-d396-52f3-919d-03b23ecef0b5",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="DP2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Protective Wall",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            passive=prevent_damage_when(_protects_own_bench),
        ),
        Attack(
            title="Anger Revenge",
            game_text="If Bastiodon was damaged by an attack during your opponent's last turn, this attack does 40 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)