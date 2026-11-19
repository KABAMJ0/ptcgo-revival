from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.card_effects.passives_common import retreat_discount

def _psychic_pokemon(pokemon, carrier):
    return pokemon_of("Psychic")(pokemon)


card = StadiumCardDef(
    guid="cda6e567-c123-5ab4-a437-0e2dae327ca7",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PhoebesStadium.Name",
    display_name="Phoebe's Stadium",
    searchable_by=["Phoebe's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=retreat_discount(2, target_pred=_psychic_pokemon)
)
