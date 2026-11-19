from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.legal_actions import attack_cost_satisfied


async def copy_anything(ctx):
    """Use 1 of your opponent's Pokemon's attacks as this attack.

    The copy pays nothing but must be affordable with the Energy already on
    Ditto, or "this attack does nothing" -- checked with the same predicate the
    engine uses to offer a printed attack."""
    candidates = []
    for pokemon in [ctx.opponent_active()] + ctx.opponent_bench():
        if pokemon is None:
            continue
        for attack in ctx.attacks_of(pokemon):
            candidates.append((pokemon, attack))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    source, chosen = picked
    if not attack_cost_satisfied(dict(chosen.cost or {}),
                                 list(ctx.attached_energies(ctx.attacker)),
                                 ctx.board):
        return
    if not await ctx.use_attack(chosen, source=source):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, entry["abilityID"])

card = PokemonCardDef(
    guid="ae95efb5-ae66-5519-a8b0-98d0584dcaf1",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="GUM",
    rarity=Rarities.RareUltra,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Attack(
            title="Copy Anything",
            game_text="Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack. If this Pok\u00e9mon doesn't have the necessary Energy to use that attack, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_anything,
        ),
    ],
)