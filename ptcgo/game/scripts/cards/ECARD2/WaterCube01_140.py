from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonToolCardDef(
    guid="acac7eec-f073-54fa-b4e7-67d254f65d31",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaterCube01.Name",
    display_name="Water Cube 01",
    searchable_by=["Water Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=140,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Splatter",
            game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. Don't apply Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(20, pool="any", apply_modifiers=False,
                                prompt="Choose a Pokémon to take 20 damage"),
        ),
        Ability(
            title="Water Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("water"),
)
