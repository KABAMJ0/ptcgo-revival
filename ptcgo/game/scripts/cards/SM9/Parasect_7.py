from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.content.definitions import Activations
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

def _opponent_active_confused(board, player_id, pokemon) -> bool:
    """The opponent's Active Pokemon is Confused: the printed gate on this
    ability ('...if your opponent's Active Pokemon is [Confused]...')."""
    from ptcgo.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
    from ptcgo.game.attributes import SpecialConditions
    confused = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED]
    for child in board.playmat.children:
        other = getattr(child, "owning_player_id", None)
        if other is None or other == player_id:
            continue
        active = board.active_pokemon(other)
        if active is None:
            continue
        if confused in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return True
    return False


async def _panic_spores(ctx):
    """2 damage counters on the opponent's Confused Active Pokemon."""
    active = ctx.opponent_active()
    if active is None:
        return
    await ctx.deal_damage(20, target=active, apply_modifiers=False,
                          as_counters=True)

card = PokemonCardDef(
    guid="4e3ba3f3-f282-5516-a7ef-103d3c3f1644",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Ability(
            title="Panic Spores",
            game_text="Once during your turn (before your attack), if your opponent's Active Pok\u00e9mon is Confused, you may put 2 damage counters on that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_opponent_active_confused,
            effect=_panic_spores,
        ),
        Attack(
            title="Mysterious Powder",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)