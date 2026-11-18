from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where, pokemon_of

card = SupporterCardDef(
    guid="22fed7a7-bd29-5a06-a06b-b30799ee0d93",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacinthe.Name",
    display_name="Jacinthe",
    searchable_by=["Jacinthe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=heal_where(150, "choice", pokemon_of("psychic"))
)
