from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_pokemon_ex
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_attach_energy


def _can_pay(ctx, attack):
    """Mew copies only while it holds the Energy that attack costs."""
    cost = getattr(attack, "cost", None) or {}
    attached = list(ctx.attached_energies(ctx.attacker))
    for pokemon_type, count in cost.items():
        type_value = getattr(pokemon_type, "value", pokemon_type)
        if type_value in (PokemonTypes.COLORLESS.value,
                          PokemonTypes.UNSET.value):
            continue
        held = sum(1 for energy in attached
                   if energy_provides_type(energy, type_value))
        if held < count:
            return False
    return True


async def copy_attack(ctx):
    defender = ctx.defender
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    attacks = [ability for ability in getattr(definition, "abilities", [])
               if isinstance(ability, Attack)]
    if not attacks:
        return
    picked = await ctx.choose_attack_to_copy(
        [(defender, attack) for attack in attacks],
        "Choose 1 of the Defending Pok\u00e9mon's attacks")
    if picked is None:
        return
    chosen = picked[1]
    if not _can_pay(ctx, chosen):
        return
    await ctx.use_attack(chosen)


async def extra_draw(ctx):
    """Only while the opponent has a Pok\u00e9mon-ex in play."""
    if not any(is_pokemon_ex(pokemon)
               for pokemon in ctx.opponent_pokemon_in_play()):
        return
    await search_attach_energy(is_basic_energy_card, count=2,
                               to_self=True)(ctx)

card = PokemonCardDef(
    guid="be3e8e6c-449a-52b6-a42b-d93ceb684037",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew δ",
    searchable_by=["Mew \u03b4", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Copy",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Copy copies that attack. This attack does nothing if Mew doesn't have the Energy necessary to use that attack. (You must still do anything else required for that attack.) Mew performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_attack,
        ),
        Attack(
            title="Extra Draw",
            game_text="If your opponent has any Pok\u00e9mon-ex in play, search your deck for up to 2 basic Energy cards and attach them to Mew. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=extra_draw,
        ),
    ],
)