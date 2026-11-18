from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_share_on_ally_ko

card = PokemonToolCardDef(
    guid="ec7cb86c-58a9-56e0-9c51-2c6ac1fe06ae",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=18,
    set_code="DV",
    rarity=Rarities.Common,
    granted_abilities=[Ability(title="Exp. Share",
                game_text="When your Active Pokémon is Knocked Out by damage from an opponent's attack, you may move 1 basic Energy card that was attached to that Pokémon to the Pokémon this card is attached to.",
                trigger=Triggers.ON_ALLY_KNOCKED_OUT,
                effect=exp_share_on_ally_ko())]
)
