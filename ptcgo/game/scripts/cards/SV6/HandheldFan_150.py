from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_move_attacker_energy_to_bench

card = PokemonToolCardDef(
    guid="c6235417-32ec-5ada-b8f8-1111fb414bf6",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandheldFan.Name",
    display_name="Handheld Fan",
    searchable_by=["Handheld Fan", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=150,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Handheld Fan",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), move an Energy from the Attacking Pokémon to 1 of your opponent's Benched Pokémon. You may attach any number of Pokémon Tools to your Pokémon during your turn. You may attach only 1 Pokémon Tool to each Pokémon, and it stays attached. Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_move_attacker_energy_to_bench(),
        ),
    ],
)
