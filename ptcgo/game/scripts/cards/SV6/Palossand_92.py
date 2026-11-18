from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9bd44d8e-f8dc-5a34-ab0e-e01aec9ad9e0",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name",
    display_name="Palossand",
    searchable_by=["Palossand", "Stage 1", "Palossand"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to use an attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Spooky Sand",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
        ),
    ],
)