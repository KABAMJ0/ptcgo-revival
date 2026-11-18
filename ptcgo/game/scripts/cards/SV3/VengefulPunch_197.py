from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import retaliate_on_attack

card = PokemonToolCardDef(
    guid="6c42bcab-d2ec-5e9d-a4fd-3af6f8fd5ff7",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VengefulPunch.Name",
    display_name="Vengeful Punch",
    searchable_by=["Vengeful Punch", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=197,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    passive=retaliate_on_attack(4)
)
