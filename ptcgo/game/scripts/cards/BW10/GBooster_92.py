from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonToolCardDef(
    guid="9f942b95-906b-59dc-8b63-2af80c264569",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GBooster.Name",
    display_name="G Booster",
    searchable_by=["G Booster", "Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    collector_number=92,
    set_code="BW10",
    rarity=Rarities.Rare,
    granted_abilities=[
        Attack(
            title="G Booster",
            game_text="Discard 2 Energy attached to this Pokémon. This attack's damage isn't affected by any effects on the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
