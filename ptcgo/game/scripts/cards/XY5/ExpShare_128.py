from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_share_on_ally_ko

card = PokemonToolCardDef(
    guid="ea1c08d0-4fa1-5ad8-ab95-1a01337f9cd4",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=128,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    granted_abilities=[Ability(title="Exp. Share",
                game_text="When your Active Pokémon is Knocked Out by damage from an opponent's attack, you may move 1 basic Energy card that was attached to that Pokémon to the Pokémon this card is attached to.",
                trigger=Triggers.ON_ALLY_KNOCKED_OUT,
                effect=exp_share_on_ally_ko())]
)
