from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="baf3ca65-ba56-5bbf-8550-e516256d9f9d",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucarioex.Name",
    display_name="Lucario ex",
    searchable_by=["Lucario ex", "Stage 1", "ex", "Lucarioex"],
    subtypes=["Stage 1", "ex"],
    collector_number=51,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Aura Uppercut",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
        ),
        Attack(
            title="Tornado Rush",
            game_text="During your next turn, this Pok\u00e9mon's Tornado Rush attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)