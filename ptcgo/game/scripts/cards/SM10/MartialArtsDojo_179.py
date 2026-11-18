from ptcgo.game.data_utils import StadiumCardDef, subtypes_for
from ptcgo.game.attributes import AttrID, CardType, PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.session.passives import Passive


def _has_basic_fighting_energy(pokemon):
    fighting = PokemonTypes.FIGHTING.value
    return any(
        child.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value
        and is_basic_energy_card(child)
        and fighting in (child.get_attribute(AttrID.POKEMON_TYPES) or [])
        for child in pokemon.children
    )


def _more_prizes(board, player_id):
    mine = board.find_player_area(player_id, "prizePile")
    theirs = [board.find_player_area(pid, "prizePile")
              for pid in board.player_ids if pid != player_id]
    if mine is None or not theirs or theirs[0] is None:
        return False
    return len(mine.children) > len(theirs[0].children)


class MartialArtsDojoPassive(Passive):
    """Non-Ultra Beast attackers with a basic Fighting Energy attached do 10
    more damage to the opponent's Active Pokemon (40 instead while the
    attacking player has more Prize cards remaining), before Weakness and
    Resistance."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if not calc.to_active:
            return
        if "Ultra Beast" in subtypes_for(attacker.archetype_id):
            return
        if not _has_basic_fighting_energy(attacker):
            return
        calc.amount += 40 if _more_prizes(calc.board, attacker.owning_player_id) else 10


card = StadiumCardDef(
    guid="5514f80a-20a0-578b-97d2-aff6b78b15c6",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MartialArtsDojo.Name",
    display_name="Martial Arts Dojo",
    searchable_by=["Martial Arts Dojo", "Stadium"],
    subtypes=["Stadium"],
    collector_number=179,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=MartialArtsDojoPassive()
)
