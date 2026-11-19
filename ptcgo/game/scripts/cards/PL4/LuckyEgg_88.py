from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import lucky_egg_ko_draw

card = PokemonToolCardDef(
    guid="14a7695d-ff54-5e94-bbfa-f1dbfed733a1",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyEgg.Name",
    display_name="Lucky Egg",
    searchable_by=["Lucky Egg", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=88,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=lucky_egg_ko_draw(7),
)
