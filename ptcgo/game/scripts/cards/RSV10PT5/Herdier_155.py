from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="754ec7d6-4014-5fc5-9ee8-91e4fd14be41",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    display_name="Herdier",
    searchable_by=["Herdier", "Stage 1", "Herdier"],
    subtypes=["Stage 1"],
    collector_number=155,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Roar",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)