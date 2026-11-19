from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack

card = PokemonCardDef(
    guid="f2e753fb-7bc3-5610-b542-2a57ecdc8820",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
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