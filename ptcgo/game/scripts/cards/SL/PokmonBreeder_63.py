from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import deck_nonempty, draw_n

card = SupporterCardDef(
    guid="4ab16c4a-4239-5ad8-8502-ea6bd5f0215f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=composed(draw_n(2), heal_item(20, scope="active")),
    condition=deck_nonempty
)
