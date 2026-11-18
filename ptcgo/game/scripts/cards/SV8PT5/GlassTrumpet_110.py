from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, attach_discard_energy_to_each, excluding, has_subtype_in_play, is_basic_energy_card, is_in_active_spot, pokemon_of

card = ItemCardDef(
    guid="a2533e87-2539-5c66-81a2-6eccc494a6ad",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlassTrumpet.Name",
    display_name="Glass Trumpet",
    searchable_by=["Glass Trumpet", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=attach_discard_energy_to_each(is_basic_energy_card, per_target=1, targets=2, target_pred=all_of(excluding(is_in_active_spot), pokemon_of("colorless"))), condition=has_subtype_in_play("Tera")
)
