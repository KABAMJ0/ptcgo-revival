from ptcgo.game.data_utils import StadiumCardDef, Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_heal_all_if_supporter

card = StadiumCardDef(
    guid="2601659d-2b82-5c70-a0a4-717bf6924eb0",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CommunityCenter.Name",
    display_name="Community Center",
    searchable_by=["Community Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=146,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Community Center",
        game_text="Once during each player's turn, if they played a Supporter card "
                  "from their hand this turn, they may heal 10 damage from each of "
                  "their Pokémon.",
        activation=Activations.ONCE_PER_TURN,
        effect=stadium_heal_all_if_supporter(10),
    ),
)
