from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_stadium_card
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.trainers import any_of

card = PokemonCardDef(
    guid="31ed8763-c8fa-5de7-9ee1-f89295e21045",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Traverse Time",
            game_text="Search your deck for up to 3 in any combination of Grass Pok\u00e9mon and Stadium cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_hand(
                any_of(lambda card: is_pokemon_of_type(card, "grass"), is_stadium_card),
                count=3,
                reveal=True,
            ),
        ),
        Attack(
            title="Solar Cutter",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)