from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23108b28-cd72-5f91-9646-0ae46f0aa2a7",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=35,
    abilities=[
        Attack(
            title="Follow Me",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)