from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

def _has_nuzzle(card) -> bool:
    """A Pokemon whose printed attacks include Nuzzle."""
    from ptcgo.game.data_utils import def_for
    definition = def_for(card.archetype_id)
    for block in getattr(definition, "abilities", None) or []:
        title = getattr(block, "title", "")
        title = title if isinstance(title, str) else getattr(title, "id", "")
        if "nuzzle" in (title or "").lower():
            return True
    return False

card = PokemonCardDef(
    guid="7ef59c82-4629-5a9f-b327-22d1845c4a7a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga", "Basic", "Emolga"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=587,
    abilities=[
        Ability(
            title="Nuzzly Gathering",
            game_text="Once during your turn (before your attack), you may search your deck for a Pok\u00e9mon that has the Nuzzle attack, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(_has_nuzzle, count=1, minimum=0,
                                   reveal=True,
                                   prompt="Choose a Pokemon with Nuzzle"),
        ),
        Attack(
            title="Nuzzle",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)