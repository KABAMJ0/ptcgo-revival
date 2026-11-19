from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import tm_devolve_all, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="46dd72ab-5db3-532a-9c67-153cb44cdbc1",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineRock.Name",
    display_name="Ancient Technical Machine [Rock]",
    searchable_by=["Ancient Technical Machine [Rock]", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=85,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Stone Generator",
            game_text="If your opponent has any Evolved Pokémon in play, remove the highest Stage Evolution card from each of them and put those cards back into his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tm_devolve_all(),
        ),
        Ability(
            title="Ancient Technical Machine [Rock]",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
