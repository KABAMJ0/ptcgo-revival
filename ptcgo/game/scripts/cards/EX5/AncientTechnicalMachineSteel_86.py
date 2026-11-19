from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import steel_generator, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="b3a71da2-8057-5887-94bc-ada52dbb6aec",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineSteel.Name",
    display_name="Ancient Technical Machine [Steel]",
    searchable_by=["Ancient Technical Machine [Steel]", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=86,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Steel Generator",
            game_text="If the Defending Pokémon has a Poké-Power or Poké-Body, choose up to 2 basic Energy cards attached to 1 of your opponent's Pokémon and attach them to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=steel_generator(2),
        ),
        Ability(
            title="Ancient Technical Machine [Steel]",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
