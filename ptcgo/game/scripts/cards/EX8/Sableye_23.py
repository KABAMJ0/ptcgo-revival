from ptcgo.game.card_effects.attacks_common import lock_opponent_plays
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a35392fc-669a-5d42-9708-eae0056b5864",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=302,
    abilities=[
        Ability(
            title="Night Vision",
            game_text="Once during your turn (before your attack), if Sableye is your Active Pok\u00e9mon, you may look at your opponent's hand. This power can't be used if Sableye is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Limitation",
            game_text="Your opponent can't play any Supporter Cards from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=lock_opponent_plays("supporter", damage=0),
        ),
    ],
)
