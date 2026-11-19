from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, is_basic_pokemon, pokemon_of_subtype, stadium_retreat_shift

card = StadiumCardDef(
    guid="f33cb209-4280-5b4f-87e8-5ff656b7feb4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrokenGroundGym.Name",
    display_name="Broken Ground Gym",
    searchable_by=["Broken Ground Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=92,
    set_code="NEO4",
    rarity=Rarities.Rare,
    passive=stadium_retreat_shift(1, any_of(pokemon_of_subtype('Baby'), is_basic_pokemon))
)
