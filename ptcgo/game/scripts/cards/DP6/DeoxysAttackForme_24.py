from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon
from ptcgo.game.card_effects.support_common import swap_with_named


def _is_deoxys(card):
    return (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith("Deoxys")


class _PsychicBoostBase(Passive):
    """Next turn Psychic Boost's base damage is 20."""

    def modify_damage_dealt(self, calc, carrier):
        if not calc.is_attack:
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        if (calc.attack_title or "") != "Psychic Boost":
            return
        calc.amount = 20


async def _psychic_boost(ctx):
    await ctx.deal_damage()
    if ctx.attacker is not None:
        ctx.add_passive_through_own_next_turn(ctx.attacker, _PsychicBoostBase())


card = PokemonCardDef(
    guid="93a0d9b3-f7c5-58fa-9373-42ae40a8850c",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysAttackForme.Name",
    display_name="Deoxys Attack Forme",
    searchable_by=["Deoxys Attack Forme", "Basic", "DeoxysAttackForme"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for any Deoxys and switch it with Deoxys Attack Forme. (Any cards attached to Deoxys Attack Forme, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys Attack Forme on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            effect=swap_with_named(predicate=_is_deoxys, destination="deck"),
        ),
        Attack(
            title="Psychic Boost",
            game_text="During your next turn, Deoxys's Psychic Boost attack's base damage is 20.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_psychic_boost,
        ),
    ],
)