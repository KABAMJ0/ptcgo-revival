from ptcgo.game.card_effects.attacks_common import mill_then_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import energy_provided_options


_FIRE = PokemonTypes.FIRE.value
_LIGHTNING = PokemonTypes.LIGHTNING.value
_TYPE_LABELS = {_FIRE: "Fire", _LIGHTNING: "Lightning"}


def _types_of(ctx, energy):
    """Every type this Energy card provides, after suppression/rewrite hooks."""
    return {type_value for option in energy_provided_options(ctx.board, energy)
            for type_value in option}


async def _dragon_burst(ctx):
    """Discard every basic Fire Energy or every basic Lightning Energy on this
    Pokemon, then pay 60 for each card discarded."""
    attacker = ctx.attacker
    if attacker is None:
        return
    pools = {}
    for energy in ctx.attached_energies(attacker):
        if not is_basic_energy_card(energy):
            continue
        for type_value in _types_of(ctx, energy):
            if type_value in _TYPE_LABELS:
                pools.setdefault(type_value, []).append(energy)
    options = [type_value for type_value in (_FIRE, _LIGHTNING) if pools.get(type_value)]
    if not options:
        return
    pick = 0 if len(options) == 1 else await ctx.choose(
        "Discard all basic Fire Energy or all basic Lightning Energy?",
        [_TYPE_LABELS[type_value] for type_value in options])
    discarded = list(pools[options[pick]])
    await ctx.discard_cards(discarded)
    await ctx.deal_damage(60 * len(discarded))


card = PokemonCardDef(
    guid="2593d077-a5d4-57ac-93ba-c4178ffcb790",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=85,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=384,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mill_then_attach_energy(count=3),
        ),
        Attack(
            title="Dragon Burst",
            game_text="Discard all basic Fire Energy or all basic Lightning Energy attached to this Pok\u00e9mon. This attack does 60 damage times the number of Energy you discarded.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=_dragon_burst,
        ),
    ],
)