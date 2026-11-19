from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import RetaliateCountersPassive, Passive
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.passives import carrier_pokemon


def _tyrogue_under(pokemon) -> bool:
    """Whether a Tyrogue is tucked under `pokemon` ("If Tyrogue is anywhere
    under this Pokemon" -- DP6's Hitmon line)."""
    for child in getattr(pokemon, "children", []) or []:
        name = getattr(def_for(getattr(child, "archetype_id", "") or ""), "display_name", "") or ""
        if name == "Tyrogue":
            return True
    return False

async def _counter_punch(ctx):
    """Counter Punch: 4 counters on whoever damages Hitmonchan next turn."""
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, RetaliateCountersPassive(4))


async def _gut_strike(ctx):
    """Gut Strike: 60 base with Tyrogue under, else the printed 30."""
    await ctx.deal_damage(60 if _tyrogue_under(ctx.attacker) else 30)

card = PokemonCardDef(
    guid="0d2f8dee-d8fb-5a5d-b9c7-479458d9ad63",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Counter Punch",
            game_text="During your opponent's next turn, if Hitmonchan is damaged by an opponent's attack (even if Hitmonchan is Knocked Out), put 4 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=_counter_punch,
        ),
        Attack(
            title="Gut Strike",
            game_text="If Tyrogue is anywhere under Hitmonchan, this attack's base damage is 60 instead of 30.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_gut_strike,
        ),
    ],
)