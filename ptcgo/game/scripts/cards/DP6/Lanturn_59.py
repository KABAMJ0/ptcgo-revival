from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per, spread_damage
from ptcgo.game.card_effects.pokemon import is_energy_card


def _has_energy(pokemon):
    return any(is_energy_card(card) for card in pokemon.children)


card = PokemonCardDef(
    guid="384d9599-e247-5117-a02e-377f11ad87d6",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Energy Split",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon that has any Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=spread_damage(30, side="opponent", include_active=True, pred=_has_energy),
        ),
        Attack(
            title="Aqua Bolt",
            game_text="Does 60 damage plus 10 more damage for each Water Energy attached to Lanturn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.WATER, cards=True), 10, base=60),
        ),
    ],
)