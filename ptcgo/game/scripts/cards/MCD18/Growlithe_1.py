from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d14d8fe4-6edb-51f1-be02-3467073e93a2",
    key="MCD18",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic", "Growlithe"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="MCD18",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)