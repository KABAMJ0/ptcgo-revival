from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_share_on_ally_ko

card = PokemonToolCardDef(
    guid="5160345c-b9d0-5a3e-86be-2c7ac2f08a27",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=118,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Exp. Share",
            game_text="Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. When your Active Pokémon is Knocked Out by damage from an opponent's attack, you may move 1 basic Energy card from that Pokémon to the Pokémon this card is attached to. You may play as many Item cards as you like during your turn (before your attack).",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_share_on_ally_ko(),
        ),
    ],
)
