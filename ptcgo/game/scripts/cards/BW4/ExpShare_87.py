from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_share_on_ally_ko

card = PokemonToolCardDef(
    guid="a3a2b889-d478-51ff-8112-0988c3bf4a6c",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=87,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Exp. Share",
            game_text="Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. When your Active Pokémon is Knocked Out by damage from an opponent's attack, you may move 1 basic Energy card that was attached to that Pokémon to the Pokémon this card is attached to. You may play as many Item cards as you like during your turn (before your attack).",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_share_on_ally_ko(),
        ),
    ],
)
