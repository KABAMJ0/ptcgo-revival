from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import fluorite, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="924a1ac5-f41e-583b-a51a-c95a04675ed3",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineFluorite.Name",
    display_name="Technical Machine: Fluorite",
    searchable_by=["Technical Machine: Fluorite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=188,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Fluorite",
            game_text="Discard all Energy from this Pokémon, and heal all damage from each of your Tera Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            effect=fluorite(),
        ),
        Ability(
            title="Technical Machine: Fluorite",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
