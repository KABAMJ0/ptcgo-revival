from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.attributes import SpecialConditions


class _DeepSleep(Passive):
    """Every Asleep Pokemon flips two coins at Checkup and only wakes on both
    heads; off while this Dark Gengar itself is Asleep, Confused or Paralyzed."""

    def sleep_recovery_coins(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return None
        return 2


async def _pull_in(ctx):
    """Pull In: may pull a Benched Pokemon up first; either way it sleeps."""
    bench = ctx.opponent_bench()
    if bench and await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokemon with the Defending Pokemon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="00fef6d4-4729-5323-b7a7-32579b822862",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGengar.Name",
    display_name="Dark Gengar",
    searchable_by=["Dark Gengar", "Stage 2", "DarkGengar"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHaunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Deep Sleep",
            game_text="As long as any Dark Gengar are in play, a player flips 2 coins for each of his or her Pok\u00e9mon that is Asleep at the end of each turn. If either of them is tails, that Pok\u00e9mon is still Asleep. This power stops working if Dark Gengar is Asleep, Confused, or Paralyzed.",
            passive=_DeepSleep(),
        ),
        Attack(
            title="Pull In",
            game_text="If your opponent has any Benched Pok\u00e9mon, you may choose 1 of them and switch it with the Defending Pok\u00e9mon (before doing damage or other effects of this attack). Either way, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            effect=_pull_in,
        ),
    ],
)