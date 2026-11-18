from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, AttrID, PokemonStage
from ptcgo.game.session.passives import Passive, attacks_of
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.effects import full_stack, is_evolution_pokemon
from ptcgo.game.card_effects.trainers import is_pokemon_EX


class MeteorFallsPassive(Passive):
    """Each player's Active Evolved Pokemon (not Pokemon-ex) may use the attacks
    printed on its Basic or Stage 1 card underneath it."""

    def granted_attacks(self, board, pokemon, carrier):
        if not is_evolution_pokemon(pokemon) or is_pokemon_EX(pokemon):
            return []
        if not is_in_active_spot(pokemon):
            return []
        out = []
        for card in full_stack(pokemon):
            if card is pokemon:
                continue
            stage = card.get_attribute(AttrID.STAGE)
            if stage in (PokemonStage.BASIC.value, PokemonStage.STAGE1.value):
                out.extend(attacks_of(card))
        return out


card = StadiumCardDef(
    guid="a9c287b2-8ce4-57df-b1b7-fa7ddfbfe633",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MeteorFalls.Name",
    display_name="Meteor Falls",
    searchable_by=["Meteor Falls", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=MeteorFallsPassive()
)
