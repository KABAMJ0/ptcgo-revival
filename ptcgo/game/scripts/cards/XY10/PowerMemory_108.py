from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonToolCardDef(
    guid="3ea92e06-a056-54ae-a05d-99ccf7955aba",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerMemory.Name",
    display_name="Power Memory",
    searchable_by=["Power Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=108,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="All Cells Burn",
            game_text="Discard 3 Energy attached to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)
