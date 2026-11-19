from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.card_effects.passives_common import discard_from_hand_then, unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _fighting_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIGHTING.value)


def _regi_cycle_condition(board, player_id, pokemon) -> bool:
    if not unafflicted(board, player_id, pokemon):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(_fighting_energy(card) for card in (discard.children if discard else []))

card = PokemonCardDef(
    guid="e97f5769-6c0e-5095-9520-5e78e4e18cd5",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=377,
    abilities=[
        Ability(
            title="Regi Cycle",
            game_text="Once during your turn (before your attack), if you have a Fighting Energy card in your discard pile, you may discard 2 cards from your hand. Then, attach a Fighting Energy card from your discard pile to Regirock. This power can't be used if Regirock is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_regi_cycle_condition,
            effect=discard_from_hand_then(
                None, 2,
                then=attach_from_discard(_fighting_energy, count=1, target="self")),
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(70)),
        ),
    ],
)