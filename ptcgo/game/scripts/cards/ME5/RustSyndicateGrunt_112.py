from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent, knocked_out_last_turn

card = SupporterCardDef(
    guid="b96fcb9f-24cc-54a3-98d8-93837e6477fa",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RustSyndicateGrunt.Name",
    display_name="Rust Syndicate Grunt",
    searchable_by=["Rust Syndicate Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=discard_energy_opponent(), condition=knocked_out_last_turn()
)
