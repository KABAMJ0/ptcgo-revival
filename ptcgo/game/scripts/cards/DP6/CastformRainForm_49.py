from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.card_effects.support_common import swap_with_named


def _is_castform(card):
    return "Castform" in (getattr(def_for(card.archetype_id), "display_name", "") or "")


def _is_castform(card):
    return "Castform" in (getattr(def_for(card.archetype_id), "display_name", "") or "")


card = PokemonCardDef(
    guid="eb6208e9-4b91-501a-b667-c25ff5b2846d",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformRainForm.Name",
    display_name="Castform Rain Form",
    searchable_by=["Castform Rain Form", "Basic", "CastformRainForm"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=351,
    abilities=[
        Ability(
            title="Temperament",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperament",
            game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform Rain Form. (Any cards attached to Castform Rain Form, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Castform Rain Form back into your deck. You can't use more than 1 Temperament Pok\u00e9-Power each turn.",
            effect=swap_with_named(predicate=_is_castform, destination="deck"),
        ),
        Attack(
            title="Water Pulse",
            game_text="The defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)