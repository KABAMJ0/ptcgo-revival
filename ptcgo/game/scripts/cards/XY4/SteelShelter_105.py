from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import condition_immunity_passive, pokemon_of_types
from ptcgo.game.attributes import Rarities, PokemonTypes

card = StadiumCardDef(
    guid="32608b93-6a75-5185-88d7-2e7ab660357d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelShelter.Name",
    display_name="Steel Shelter",
    searchable_by=["Steel Shelter", "Stadium"],
    subtypes=["Stadium"],
    collector_number=105,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(protects=pokemon_of_types(PokemonTypes.METAL.value))
)
