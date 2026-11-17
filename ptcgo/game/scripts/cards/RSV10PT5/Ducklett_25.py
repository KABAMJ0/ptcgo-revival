from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e28f505b-7f28-5620-ac1d-bf70c88e3ac0",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    display_name="Ducklett",
    searchable_by=["Ducklett", "Basic", "Ducklett"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=580,
    abilities=[
        Attack(
            title="Firefighting",
            game_text="Discard a Fire Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)