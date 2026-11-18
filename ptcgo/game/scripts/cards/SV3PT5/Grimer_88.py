from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85741401-87a9-5056-9586-a04832cf138b",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=88,
    abilities=[
        Attack(
            title="Gummy Press",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's Retreat Cost is Colorless more.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)