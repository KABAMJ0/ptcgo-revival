from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e3b790b-a5d2-555a-8a4b-81c7328f0065",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Curse Spreading",
            game_text="Put 8 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=unimplemented,
        ),
    ],
)