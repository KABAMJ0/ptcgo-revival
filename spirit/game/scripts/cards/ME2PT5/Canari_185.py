from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import pokemon_of, with_discard_cost

card = SupporterCardDef(
    guid="41dda04f-f147-5b08-8934-8111e0ed2600",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Canari.Name",
    display_name="Canari",
    searchable_by=["Canari", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(pokemon_of("lightning"), count=4))
)
