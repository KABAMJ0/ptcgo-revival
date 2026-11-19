from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive, previous_evolution_attacks
from ptcgo.game.session.effects import is_evolution_pokemon


class ShrineOfMemoriesPassive(Passive):
    """Each player's evolved Pokemon may use the attacks of its previous Evolutions.

    `previous_evolution_grant_passive` is carrier-scoped (it grants only when
    the carrier IS the Pokemon, `passives_common.py:551`), which a Stadium is
    not, so the same engine helper is applied to every evolved Pokemon here.
    """

    def granted_attacks(self, board, pokemon, carrier):
        if not is_evolution_pokemon(pokemon):
            return []
        return previous_evolution_attacks(pokemon)


card = StadiumCardDef(
    guid="23a9102a-c29c-510f-a38e-8d8488f7a361",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofMemories.Name",
    display_name="Shrine of Memories",
    searchable_by=["Shrine of Memories", "Stadium"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=ShrineOfMemoriesPassive()
)
