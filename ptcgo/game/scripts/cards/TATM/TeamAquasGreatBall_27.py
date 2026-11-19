from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    basic_energy_of, is_basic_pokemon, search_two_kinds, team_aqua_target,
)

card = ItemCardDef(
    guid="67503eb2-c932-5f2f-8aca-6f0c3aea29b6",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasGreatBall.Name",
    display_name="Team Aqua's Great Ball",
    searchable_by=["Team Aqua's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=27,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    effect=search_two_kinds(lambda card: is_basic_pokemon(card)
                            and team_aqua_target(card), 1,
                            basic_energy_of("Water"), 1)
)
