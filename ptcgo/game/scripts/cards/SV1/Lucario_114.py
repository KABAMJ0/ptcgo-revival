import json

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import def_for


def _printed_types(archetype_id):
    definition = def_for(archetype_id)
    spec = (getattr(definition, "extra_attributes", {}) or {}).get(
        str(AttrID.POKEMON_TYPES.value))
    value = spec.get("value") if isinstance(spec, dict) else spec
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except ValueError:
            return set()
    return set(value or [])


def _fighting_knocked_out_last_turn(ctx):
    ledger = ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, [])
    return any(PokemonTypes.FIGHTING.value in _printed_types(record["archetype_id"])
               for record in ledger)


async def _avenging_knuckle(ctx):
    if _fighting_knocked_out_last_turn(ctx):
        await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + 120)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="db6b81bb-4464-5086-8b2d-370ce167046a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Avenging Knuckle",
            game_text="If any of your Fighting Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=_avenging_knuckle,
        ),
        Attack(
            title="Accelerating Stab",
            game_text="During your next turn, this Pok\u00e9mon can't use Accelerating Stab.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)