from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="82ec059a-d905-51c6-9412-54ff37e4b23c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    display_name="Staravia",
    searchable_by=["Staravia", "Stage 1", "Staravia"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)