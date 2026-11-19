from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_draw_on_damaged

card = PokemonToolCardDef(
    guid="4baab8cf-6639-5f5c-a7fa-c77bc77b5b74",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyHelmet.Name",
    display_name="Lucky Helmet",
    searchable_by=["Lucky Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=158,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lucky Helmet",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), draw 2 cards. You may attach any number of Pokémon Tools to your Pokémon during your turn. You may attach only 1 Pokémon Tool to each Pokémon, and it stays attached. Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_draw_on_damaged(2),
        ),
    ],
)
