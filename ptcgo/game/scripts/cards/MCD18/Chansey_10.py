from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="527e69b4-03a3-5cdb-908e-084f5e4808ea",
    key="MCD18",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MCD18",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Bind Wound",
            game_text="Flip a coin. If heads, heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
        ),
    ],
)