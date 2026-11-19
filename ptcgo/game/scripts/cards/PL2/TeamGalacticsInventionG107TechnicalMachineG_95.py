from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import damage_porter, pokemon_of_subtype

card = PokemonToolCardDef(
    guid="6e0f0d95-3a33-5f2b-a6a7-950b41e7efa0",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsInventionG107TechnicalMachineG.Name",
    display_name="Team Galactic's Invention G-107 Technical Machine G",
    searchable_by=["Team Galactic's Invention G-107 Technical Machine G", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=95,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    attach_to=pokemon_of_subtype("SP"),
    granted_abilities=[
        Attack(
            title="Damage Porter",
            game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage times the number of damage counters on the Pokémon this card is attached to to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=damage_porter(10),
        ),
    ],
)
