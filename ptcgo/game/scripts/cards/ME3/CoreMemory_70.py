from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonToolCardDef(
    guid="3794b576-c318-558c-9dbf-56a2153b0179",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoreMemory.Name",
    display_name="Core Memory",
    searchable_by=["Core Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=70,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Geobuster",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=350,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
