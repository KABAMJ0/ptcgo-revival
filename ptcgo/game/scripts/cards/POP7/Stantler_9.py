from ptcgo.game.card_effects.trainers import is_supporter_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cebaf604-0e05-55ba-92f3-6d140cf1501b",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(predicate=is_supporter_card, count=1, minimum=1),
        ),
        Attack(
            title="Frighten Horn",
            game_text="If the Defending Pok\u00e9mon isn't an Evolved Pok\u00e9mon, that Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)