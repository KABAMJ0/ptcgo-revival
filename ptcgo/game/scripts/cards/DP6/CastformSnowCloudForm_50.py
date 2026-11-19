from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_all_opponents
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import swap_with_named


def _is_castform(card) -> bool:
    """Any Castform for Temperament's deck search ("search your deck for any
    Castform"); every form shares the display-name prefix."""
    from ptcgo.game.content.definitions import def_for

    d = def_for(getattr(card, "archetype_id", None))
    return (getattr(d, "display_name", None) or "").startswith("Castform")


card = PokemonCardDef(
    guid="34123a6b-a4e5-5546-9912-900e8670a5ef",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSnowCloudForm.Name",
    display_name="Castform Snow-Cloud Form",
    searchable_by=["Castform Snow-Cloud Form", "Basic", "CastformSnowCloudForm"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=351,
    abilities=[
        Ability(
            title="Temperament",
            game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform Snow-cloud Form. (Any cards attached to Castform Snow-cloud Form, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Castform Snow-cloud Form back into your deck. You can't use more than 1 Temperament Pok\u00e9-Power each turn.",
            effect=swap_with_named(predicate=_is_castform),
        ),
        Attack(
            title="Hail",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=damage_all_opponents(10),
        ),
    ],
)