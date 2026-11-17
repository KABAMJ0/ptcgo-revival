from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b78d0b4d-68fd-57da-820a-edb943afe9c1",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic", "Charcadet"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
    abilities=[
        Attack(
            title="Best Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)