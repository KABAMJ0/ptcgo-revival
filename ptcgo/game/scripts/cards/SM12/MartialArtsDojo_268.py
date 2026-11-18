from ptcgo.game.data_utils import StadiumCardDef, subtypes_for
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.session.passives import Passive

def _prizes_left(board, player_id):
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area is not None else 0


class MartialArtsDojoPassive(Passive):
    """Non-Ultra Beast attackers with a basic Fighting Energy do +10 to the
    opponent's Active, or +40 while their player has more Prizes remaining."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None:
            return
        if "ultra beast" in [s.lower() for s in subtypes_for(attacker.archetype_id)]:
            return
        board = calc.board
        if not any(is_basic_energy_card(energy)
                   and energy_provides_type(energy, PokemonTypes.FIGHTING.value)
                   for energy in board.attached_energies(attacker)):
            return
        mine = _prizes_left(board, attacker.owning_player_id)
        theirs = _prizes_left(board, calc.target.owning_player_id)
        calc.amount += 40 if mine > theirs else 10


card = StadiumCardDef(
    guid="30472cd5-8572-59ff-b99d-2a300a204f13",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MartialArtsDojo.Name",
    display_name="Martial Arts Dojo",
    searchable_by=["Martial Arts Dojo", "Stadium"],
    subtypes=["Stadium"],
    collector_number=268,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    passive=MartialArtsDojoPassive(),
)
