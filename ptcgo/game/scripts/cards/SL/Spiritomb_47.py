from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import no_retreat_passive, opposing_active, is_in_active_spot
from ptcgo.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="e07d3a7b-fdd9-5cac-9f30-8b749486398c",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=442,
    abilities=[
        Ability(
            title="Cursed Whirlpool",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon can't retreat.",
            passive=no_retreat_passive(lambda p, c: opposing_active(p, c) and is_in_active_spot(c)),
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(3, target="choose_any_opponent"),
        ),
    ],
)