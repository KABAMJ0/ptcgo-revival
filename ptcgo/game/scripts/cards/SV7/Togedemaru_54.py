from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b733c36e-8d19-5013-9746-eaae4236f6af",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic", "Togedemaru"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=777,
    abilities=[
        Attack(
            title="Electrifying Chance",
            game_text="If you have exactly 1 Prize card remaining, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)