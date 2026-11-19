from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import named_exactly
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="358f08f9-0e90-55ff-82f8-5a660f896fc9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=69,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Mega Ascension",
            game_text="Search your deck for M Rayquaza-EX, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(
                named_exactly("M Rayquaza-EX"),
                count=1,
                minimum=1,
                reveal=True,
            ),
        ),
        Attack(
            title="Aeroscream",
            game_text="Flip a coin. If tails, discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=unimplemented,
        ),
    ],
)