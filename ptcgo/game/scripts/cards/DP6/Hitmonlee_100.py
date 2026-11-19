from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import RetaliateCountersPassive, Passive
from ptcgo.game.data_utils import def_for


def _tyrogue_under(pokemon) -> bool:
    """Whether a Tyrogue is tucked under `pokemon` ("If Tyrogue is anywhere
    under this Pokemon" -- DP6's Hitmon line)."""
    for child in getattr(pokemon, "children", []) or []:
        name = getattr(def_for(getattr(child, "archetype_id", "") or ""), "display_name", "") or ""
        if name == "Tyrogue":
            return True
    return False

async def _gut_kick(ctx):
    """Gut Kick: may send the 30 to a Benched Pokemon instead."""
    bench = ctx.opponent_bench()
    if bench and _tyrogue_under(ctx.attacker) and await ctx.ask_yes_no(
            "Do 30 damage to 1 of your opponent's Benched Pokemon instead?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
        if target is not None:
            await ctx.deal_damage(30, target=target, apply_modifiers=False)
            return
    await ctx.deal_damage()

card = PokemonCardDef(
    guid="695ec2d3-b6c2-522d-a254-b5f6a4c3d673",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name",
    display_name="Hitmonlee",
    searchable_by=["Hitmonlee", "Basic", "Hitmonlee"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=106,
    abilities=[
        Attack(
            title="Gut Kick",
            game_text="If Tyrogue is anywhere under Hitmonlee, you may do 30 damage to any 1 Benched Pok\u00e9mon instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_gut_kick,
        ),
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)