from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="5e7d7462-0df1-5eb7-97f1-d2e2c0867d9e",
    key="FUT20",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrookeyontheBall.Name",
    display_name="Grookey on the Ball",
    searchable_by=["Grookey on the Ball", "Basic", "GrookeyontheBall"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="FUT20",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=810,
    abilities=[
        Attack(
            title="Tenacious Defense",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)