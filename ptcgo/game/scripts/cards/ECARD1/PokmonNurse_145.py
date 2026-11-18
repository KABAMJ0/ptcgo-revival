from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_then_discard_energy

card = SupporterCardDef(
    guid="14695a35-1796-5554-a762-fd808e6aa235",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonNurse.Name",
    display_name="Pokémon Nurse",
    searchable_by=["Pok\u00e9mon Nurse", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=heal_all_then_discard_energy()
)
