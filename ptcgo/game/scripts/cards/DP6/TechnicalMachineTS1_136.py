from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import tm_evoluter

card = PokemonToolCardDef(
    guid="65de453d-0f58-56c9-8c0e-1c3996e89f3f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTS1.Name",
    display_name="Technical Machine TS-1",
    searchable_by=["Technical Machine TS-1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=136,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Evoluter",
            game_text="Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward.",
            cost={},
            effect=tm_evoluter(),
        ),
    ],
)
