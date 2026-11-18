from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, stadium_attack_tax

card = StadiumCardDef(
    guid="e8f78bfd-5a07-572b-a543-4adaeeab84b1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonLeagueHeadquarters.Name",
    display_name="Pokémon League Headquarters",
    searchable_by=["Pok\u00e9mon League Headquarters", "Stadium"],
    subtypes=["Stadium"],
    collector_number=192,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    passive=stadium_attack_tax(1, is_basic_pokemon)
)
