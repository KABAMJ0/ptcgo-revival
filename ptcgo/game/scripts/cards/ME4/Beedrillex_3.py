from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9acc9c6-7fe0-511e-900a-aab92c341495",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrillex.Name",
    display_name="Beedrill ex",
    searchable_by=["Beedrill ex", "Stage 2", "ex", "Beedrillex"],
    subtypes=["Stage 2", "ex"],
    collector_number=3,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Rumbling Bees",
            game_text="This attack does 110 damage for each of your Beedrill and Beedrill ex in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=110,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)