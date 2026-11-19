from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="5bc26ff9-d3cf-5b42-85f8-53bfc109608f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Veil",
            game_text="Prevent all damage counters from being placed on your Benched Pok\u00e9mon by effects of attacks used by your opponent's Basic Pok\u00e9mon.",
            effect=search_to_hand(is_basic_energy_card, count=2, reveal=True),
        ),
        Attack(
            title="Charge Energy",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_basic_energy_card, count=2, reveal=True),
        ),
    ],
)