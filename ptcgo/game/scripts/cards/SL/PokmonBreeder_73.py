from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import deck_nonempty, draw_n

card = SupporterCardDef(
    guid="e3d53a72-4e15-5199-a727-57e92c8346ba",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="SL",
    rarity=Rarities.RareUltra,
    effect=composed(draw_n(2), heal_item(20, scope="active")),
    condition=deck_nonempty
)
