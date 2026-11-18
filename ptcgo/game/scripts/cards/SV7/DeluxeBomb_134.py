from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_counters_on_attacker

card = PokemonToolCardDef(
    guid="d45d5213-97cc-55aa-9295-122c2fefa404",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeluxeBomb.Name",
    display_name="Deluxe Bomb",
    searchable_by=["Deluxe Bomb", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=134,
    set_code="SV7",
    rarity=Rarities.Rare,
    granted_abilities=[
        Ability(
            title="Deluxe Bomb",
            game_text="You can't have more than 1 ACE SPEC card in your deck. If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 12 damage counters on the Attacking Pokémon. If you placed any damage counters in this way, discard this card. You may attach any number of Pokémon Tools to your Pokémon during your turn. You may attach only 1 Pokémon Tool to each Pokémon, and it stays attached.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_counters_on_attacker(12, 0, True),
        ),
    ],
)
