from ptcgo.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.trainers import draw_n, knocked_out_last_turn

def _flip_the_script_condition(board, player_id, pokemon):
    """Ability conditions take (board, player_id, pokemon); the trainer play
    condition behind this one takes (board, player_id)."""
    return knocked_out_last_turn()(board, player_id)

card = PokemonCardDef(
    guid="79cab94d-09b9-5a77-ba4f-01bc3cbf5da4",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipitiex.Name",
    display_name="Fezandipiti ex",
    searchable_by=["Fezandipiti ex", "Basic", "ex", "Fezandipitiex"],
    subtypes=["Basic", "ex"],
    collector_number=38,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Flip the Script",
            game_text="Once during your turn, if any of your Pok\u00e9mon were Knocked Out during your opponent's last turn, you may draw 3 cards. You can't use more than 1 Flip the Script Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Flip the Script",
            condition=_flip_the_script_condition,
            effect=draw_n(3),
        ),
        Attack(
            title="Cruel Arrow",
            game_text="This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(100, pool="any", count=1, apply_modifiers=False),
        ),
    ],
)