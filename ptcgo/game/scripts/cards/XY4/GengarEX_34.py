from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="08f12d37-3f2e-528f-8d8d-07ebdf0941e7",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name",
    display_name="Gengar-EX",
    searchable_by=["Gengar-EX", "Basic", "EX", "GengarEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=94,
    abilities=[
        Attack(
            title="Night Attack",
            game_text="Put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(3, target="choose_any_opponent"),
        ),
        Attack(
            title="Dark Corridor",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)