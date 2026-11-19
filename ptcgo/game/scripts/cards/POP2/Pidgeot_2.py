from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.trainers import bench_into_deck


def _beating_wings_condition(board, player_id, pokemon):
    if pokemon is None or not is_in_active_spot(pokemon):
        return False
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench is not None and bench.children)

card = PokemonCardDef(
    guid="4a0dbed0-168b-50a0-8ee1-b9436f234cb8",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=18,
    abilities=[
        Ability(
            title="Beating Wings",
            game_text="Once during your turn (before your attack), if Pidgeot is your Active Pok\u00e9mon, you may shuffle 1 of your Benched Pok\u00e9mon and all cards attached to it into your deck. This power can't be used if Pidgeot is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_beating_wings_condition,
            effect=bench_into_deck(),
        ),
        Attack(
            title="Sharp Beak",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(50)),
        ),
    ],
)