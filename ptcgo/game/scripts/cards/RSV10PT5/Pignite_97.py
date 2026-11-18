from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ac60ac93-25d6-5aa5-b4dc-47767873c470",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    display_name="Pignite",
    searchable_by=["Pignite", "Stage 1", "Pignite"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)