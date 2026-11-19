from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b7926b8e-411d-5266-b7bc-5e176b88b3a4",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=417,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_basic_energy_card, count=1, minimum=1),
        ),
        Attack(
            title="Thunder Jolt",
            game_text="Flip a coin. If tails, Pachirisu does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)