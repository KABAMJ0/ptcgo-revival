from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import turbo_energize, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="62a9137d-bf93-5390-a49a-a5ef41b21a15",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTurboEnergize.Name",
    display_name="Technical Machine: Turbo Energize",
    searchable_by=["Technical Machine: Turbo Energize", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=179,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Turbo Energize",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=turbo_energize(2),
        ),
        Ability(
            title="Technical Machine: Turbo Energize",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
