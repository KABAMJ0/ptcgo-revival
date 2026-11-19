from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack

card = PokemonCardDef(
    guid="61616b2d-49fc-5df1-9e8b-d7935bfbd7b5",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIRE: 1},
            effect=discard_stadium_attack(),
        ),
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)