from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import named_exactly, pokemon_of_subtype
from ptcgo.game.card_effects.support_common import search_attach_energy

card = ItemCardDef(
    guid="ad0ea3bd-0688-5e4b-9262-ba4ee3a0d232",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColressMachine.Name",
    display_name="Colress Machine",
    searchable_by=["Colress Machine", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=119,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=search_attach_energy(named_exactly("Plasma Energy"), 1, target_pred=pokemon_of_subtype("Team Plasma"))
)
