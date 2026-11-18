from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of

card = PokemonToolCardDef(
    guid="d73d9dd1-f639-5cb6-a91d-379f556208d2",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventureLantern.Name",
    display_name="Adventure Lantern",
    searchable_by=["Adventure Lantern", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=90,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(basic_energy_of("fire"), basic_energy_of("lightning")), count=1)
)
