from ptcgo.game.data_utils import StadiumCardDef, unimplemented, Ability, Triggers
from ptcgo.game.card_effects.support_common import trigger_counters
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="a662e600-bd33-50bd-9832-dac9d73d0729",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CalamitousSnowyMountain.Name",
    display_name="Calamitous Snowy Mountain",
    searchable_by=["Calamitous Snowy Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=174,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="CalamitousSnowyMountain_174",
        trigger=Triggers.ON_ENERGY_ATTACHED,
        effect=trigger_counters(2, lambda p, c: has_pokemon_subtype(p, "Basic") or True),
    )
)
