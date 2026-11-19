from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.support_common import swap_with_named


def _is_castform(card):
    return "Castform" in (getattr(def_for(card.archetype_id), "display_name", "") or "")


card = PokemonCardDef(
    guid="c935b04c-d1a4-51cc-afc9-d0a69f6dbc6f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name",
    display_name="Castform Sunny Form",
    searchable_by=["Castform Sunny Form", "Basic", "CastformSunnyForm"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Ability(
            title="Temperament",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperament",
            game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform Sunny Form. (Any cards attached to Castform Sunny Form, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Castform Sunny Form back into your deck. You can't use more than 1 Temperament Pok\u00e9-Power each turn.",
            effect=swap_with_named(predicate=_is_castform, destination="deck"),
        ),
        Attack(
            title="Ember",
            game_text="Discard a Fire Energy attached to Castform Sunny Form.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)