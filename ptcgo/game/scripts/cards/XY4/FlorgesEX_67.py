from ptcgo.game.card_effects.trainers import is_supporter_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="60139a90-8c60-56bf-be4c-864ef0479127",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesEX.Name",
    display_name="Florges-EX",
    searchable_by=["Florges-EX", "Basic", "EX", "FlorgesEX"],
    subtypes=["Basic", "EX"],
    collector_number=67,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=671,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            effect=search_to_hand(predicate=is_supporter_card, count=1, minimum=1),
        ),
        Attack(
            title="Bright Garden",
            game_text="This attack does 20 damage times the number of Grass Pok\u00e9mon and Fairy Pok\u00e9mon you have in play.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)