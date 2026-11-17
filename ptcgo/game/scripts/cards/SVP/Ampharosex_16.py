from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b32c8fc-a64b-59c1-a6d0-e107f5d09d98",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharosex.Name",
    display_name="Ampharos ex",
    searchable_by=["Ampharos ex", "Stage 2", "ex", "Ampharosex"],
    subtypes=["Stage 2", "ex"],
    collector_number=16,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title="Thunderstrike Tail",
            game_text="You may discard 2 Energy from this Pok\u00e9mon to have this attack do 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)