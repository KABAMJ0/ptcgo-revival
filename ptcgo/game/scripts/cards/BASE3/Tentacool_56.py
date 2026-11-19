from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.support_common import remove_self_from_play


def _coward_ready(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    state = getattr(board, "turn_state", None)
    if state is not None and \
            state.entered_play_turn.get(pokemon.entity_id) == state.turn_number:
        return False
    return True


_cowardice = remove_self_from_play(
    destination="hand", with_attachments="discard", optional=True)

card = PokemonCardDef(
    guid="39879b44-da05-574a-99e8-09cae0b17da1",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic", "Tentacool"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Ability(
            title="Cowardice",
            game_text="At any time during your turn (before your attack), you may return Tentacool to your hand. (Discard all cards attached to Tentacool.) This power can't be used the turn you put Tentacool into play or if Tentacool is Asleep, Confused, or Paralyzed.",
            activation=Activations.UNLIMITED,
            condition=_coward_ready,
            effect=_cowardice,
        ),
        Attack(
            title="Acid",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)