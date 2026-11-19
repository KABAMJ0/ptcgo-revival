from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_counters_on_attacker

card = PokemonToolCardDef(
    guid="1aa5bbfa-c57f-55b7-b3cd-ac48fb85691b",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TremendousBomb.Name",
    display_name="Tremendous Bomb",
    searchable_by=["Tremendous Bomb", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=113,
    set_code="ME5",
    rarity=Rarities.Rare,
    granted_abilities=[
        Ability(
            title="Tremendous Bomb",
            game_text="If the Pokémon this card is attached to isn't a Mega Evolution Pokémon ex, is in the Active Spot, and takes 240 or more damage from an attack from your opponent's Mega Evolution Pokémon ex (even if this Pokémon is Knocked Out), place 12 damage counters on the Attacking Pokémon. If you placed any damage counters in this way, discard this card.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_counters_on_attacker(12, 240, True, None, True, True),
        ),
    ],
)
