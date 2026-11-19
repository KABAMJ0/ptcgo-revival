from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.support_common import swap_with_named


def _is_deoxys(card):
    return (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith("Deoxys")


card = PokemonCardDef(
    guid="a92c2c6b-7fb8-58fb-b9a0-add9809735f5",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysNormalForme.Name",
    display_name="Deoxys Normal Forme",
    searchable_by=["Deoxys Normal Forme", "Basic", "DeoxysNormalForme"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for any Deoxys and switch it with Deoxys Normal Forme. (Any cards attached to Deoxys Normal Forme, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys Normal Forme on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            effect=swap_with_named(predicate=_is_deoxys, destination="deck"),
        ),
        Attack(
            title="Energy Crush",
            game_text="Does 20 damage plus 10 more damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("opponent", cards=True), 10, base=20),
        ),
    ],
)