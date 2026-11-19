from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    basic_energy_of, is_basic_pokemon, search_two_kinds, team_magma_target,
)

card = ItemCardDef(
    guid="489c8b1b-246c-590e-893e-14738017b7d6",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasGreatBall.Name",
    display_name="Team Magma's Great Ball",
    searchable_by=["Team Magma's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=31,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    effect=search_two_kinds(lambda card: is_basic_pokemon(card)
                            and team_magma_target(card), 1,
                            basic_energy_of("Fighting"), 1)
)
