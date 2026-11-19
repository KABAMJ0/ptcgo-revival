from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.trainers import any_of

card = PokemonCardDef(
    guid="a9228534-cbf7-5b28-8efb-f5638f9c4334",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Licking Catch",
            game_text="Search your deck for up to 3 in any combination of Fire Pok\u00e9mon and Basic Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=search_to_hand(
                any_of(lambda card: is_pokemon_of_type(card, "fire"), basic_energy_of("fire")),
                count=3,
                reveal=True,
            ),
        ),
        Attack(
            title="Fire Claws",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
        ),
    ],
)