from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b579e12-8eb2-5a10-8f71-74e61098c998",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta", "Basic", "Larvesta"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=636,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)