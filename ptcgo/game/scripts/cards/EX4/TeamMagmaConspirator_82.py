from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, any_of, is_basic_energy_card, pokemon_named
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_hand

_CONSPIRATOR_CARDS = any_of(
    all_of(is_basic_pokemon, pokemon_named("team magma")),
    is_basic_energy_card)


card = SupporterCardDef(
    guid="57e43eca-5888-5767-8c3f-692192d3b576",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaConspirator.Name",
    display_name="Team Magma Conspirator",
    searchable_by=["Team Magma Conspirator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(_CONSPIRATOR_CARDS, 2)
)
