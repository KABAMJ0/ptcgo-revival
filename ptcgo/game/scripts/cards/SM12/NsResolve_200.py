from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, discard_top_attach_energy, excluding, is_basic_energy_card, is_in_active_spot, pokemon_of

card = SupporterCardDef(
    guid="274dde60-f147-5ff6-8a63-ebc1e5b0f749",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsResolve.Name",
    display_name="N's Resolve",
    searchable_by=["N's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=discard_top_attach_energy(6, is_basic_energy_card, all_of(excluding(is_in_active_spot), pokemon_of("dragon")))
)
