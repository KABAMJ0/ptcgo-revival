from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import tm_devoluter

card = PokemonToolCardDef(
    guid="ddee6153-1201-58c8-a1ff-be620ae99d18",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTS2.Name",
    display_name="Technical Machine TS-2",
    searchable_by=["Technical Machine TS-2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=137,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Devoluter",
            game_text="Choose 1 of your opponent's Evolved Pokémon (excluding Pokémon LV.X). Remove the highest Stage Evolution card from that Pokémon and put that card back into your opponent's hand.",
            cost={},
            effect=tm_devoluter(),
        ),
    ],
)
