from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_then_energy_to_hand, pokemon_of_subtype

card = SupporterCardDef(
    guid="b5b6f139-5b2a-588b-9fe9-dac5663ec536",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysCompassion.Name",
    display_name="Wally's Compassion",
    searchable_by=["Wally's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=heal_all_then_energy_to_hand(pokemon_of_subtype("MEGA"))
)
