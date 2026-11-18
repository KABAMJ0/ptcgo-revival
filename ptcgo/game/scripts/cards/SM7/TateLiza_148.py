from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import choose_one, shuffle_hand_draw, switch

card = SupporterCardDef(
    guid="6bb1a280-76da-577b-a312-eba35a09cb8f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name",
    display_name="Tate & Liza",
    searchable_by=["Tate & Liza", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Shuffle your hand into your deck then draw 5 cards", shuffle_hand_draw(5)), ("Switch your Active Pokémon with 1 of your Benched Pokémon", switch)])
)
