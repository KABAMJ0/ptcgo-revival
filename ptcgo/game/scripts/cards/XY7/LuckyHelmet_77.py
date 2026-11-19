from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_draw_on_damaged

card = PokemonToolCardDef(
    guid="79c1619f-4224-537e-b42b-552570de9527",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyHelmet.Name",
    display_name="Lucky Helmet",
    searchable_by=["Lucky Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=77,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lucky Helmet",
            game_text="Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. Whenever the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), draw 2 cards. You may play as many Item cards as you like during your turn (before your attack).",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_draw_on_damaged(2),
        ),
    ],
)
