from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_counters_on_attacker

card = PokemonToolCardDef(
    guid="0c8c26f4-0c27-53a2-bc2a-e73d58b205f3",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PunkHelmet.Name",
    display_name="Punk Helmet",
    searchable_by=["Punk Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Punk Helmet",
            game_text="If the Darkness Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), place 4 damage counters on the Attacking Pokémon. You may attach any number of Pokémon Tools to your Pokémon during your turn. You may attach only 1 Pokémon Tool to each Pokémon, and it stays attached.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_counters_on_attacker(4, 0, False, "DARKNESS"),
        ),
    ],
)
