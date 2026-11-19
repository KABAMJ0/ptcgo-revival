from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import lightning_discharge, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="54711d47-a6a0-568e-9d1c-611671551d1c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LightningCube01.Name",
    display_name="Lightning Cube 01",
    searchable_by=["Lightning Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=127,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy cards attached to this Pokémon. Then, flip a number of coins equal to the number of Energy cards discarded that way. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=lightning_discharge(40),
        ),
        Ability(
            title="Lightning Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
