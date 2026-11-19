from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_coin_reroll, pokemon_named, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="f466c6f3-4782-52c0-b0c3-aa3b1963e120",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasESP.Name",
    display_name="Sabrina's ESP",
    searchable_by=["Sabrina's ESP", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=117,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    passive=holder_coin_reroll(),
    attach_to=pokemon_named("sabrina"),
    granted_abilities=[
        Ability(
            title="Sabrina's ESP",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
