from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.support_common import swap_with_named
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.legal_actions import attack_cost_satisfied, effective_attack_cost


async def _copy_defender_attack(ctx):
    defender = ctx.defender
    if defender is None:
        return
    candidates = [(defender, attack) for attack in ctx.attacks_of(defender)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    cost = effective_attack_cost(ctx.board, ctx.attacker, chosen.cost)
    if not attack_cost_satisfied(cost, ctx.attached_energies(ctx.attacker), ctx.board):
        return
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="0b99274c-7fa9-5b02-988b-24fb421506b5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=132,
    abilities=[
        Ability(
            title="Duplicate",
            game_text="Once during your turn (before your attack), you may search your deck for another Ditto and switch it with Ditto. (Any cards attached to Ditto, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Ditto on top of your deck. Shuffle your deck afterward. You can't use more than 1 Duplicate Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Duplicate",
            effect=swap_with_named(),
        ),
        Attack(
            title="Copy",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Copy copies that attack. This attack does nothing if Ditto doesn't have the Energy necessary to use that attack. (You must still do anything else required for that attack.) Ditto performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_copy_defender_attack,
        ),
    ],
)