from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import tm_devolve_all, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="e711bfc8-bae6-5392-8656-eb6791b46d78",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineDevolution.Name",
    display_name="Technical Machine: Devolution",
    searchable_by=["Technical Machine: Devolution", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=177,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Devolution",
            game_text="Devolve each of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tm_devolve_all(),
        ),
        Ability(
            title="Technical Machine: Devolution",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
