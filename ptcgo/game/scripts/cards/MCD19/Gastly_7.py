from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2571ce75-adb4-5b37-ba1e-044c948b18af",
    key="MCD19",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="MCD19",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Ominous Eyes",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(1, target="choose_any_opponent"),
        ),
    ],
)