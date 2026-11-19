from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

def flip_the_script_available(board, player_id, pokemon) -> bool:
    """Offered only when one of your Pokemon was Knocked Out during your
    opponent's last turn."""
    turn_state = getattr(board, "turn_state", None)
    ledger = getattr(turn_state, "pokemon_left_play_last_turn", None) or []
    return any(record.get("owner_id") == player_id for record in ledger)


from ptcgo.game.card_effects.trainers import draw_n

card = PokemonCardDef(
    guid="63c0d524-7418-5ddd-a050-e1ccdcad6a04",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipitiex.Name",
    display_name="Fezandipiti ex",
    searchable_by=["Fezandipiti ex", "Basic", "ex", "Fezandipitiex"],
    subtypes=["Basic", "ex"],
    collector_number=142,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1016,
    abilities=[
        Ability(
            title="Flip the Script",
            game_text="Once during your turn, if any of your Pok\u00e9mon were Knocked Out during your opponent's last turn, you may draw 3 cards. You can't use more than 1 Flip the Script Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            condition=flip_the_script_available,
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