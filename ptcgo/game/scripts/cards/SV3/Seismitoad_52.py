from ptcgo.game.card_effects.passives_common import boost_own_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import AttackCostModifierPassive, is_in_active_spot


class QuakingZonePassive(AttackCostModifierPassive):
    """While this Pokemon is Active, the opponent's Active attacks cost [C] more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if not is_in_active_spot(carrier):
            return cost
        return super().modify_attack_cost(cost, pokemon, carrier, board)


card = PokemonCardDef(
    guid="9525dcfb-8cb9-586a-9023-c563faef90b6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Ability(
            title="Quaking Zone",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, attacks used by your opponent's Active Pok\u00e9mon cost Colorless more.",
            passive=QuakingZonePassive(1, pred=lambda mon, board: is_in_active_spot(mon), side="opposing"),
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            effect=boost_own_next_turn(100, attack_title="Echoed Voice"),
        ),
    ],
)