from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import Triggers, def_for
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import search_to_bench


def _is_beldum(card):
    return (getattr(def_for(card.archetype_id), "display_name", "") or "") == "Beldum"


async def _metal_chain(ctx):
    if getattr(ctx, "energy_receiver", None) is not ctx.source:
        return
    energy = getattr(ctx, "attached_energy", None)
    if energy is None or not energy_provides_type(energy, PokemonTypes.METAL.value):
        return
    if ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return
    if not await ctx.ask_yes_no("Search your deck for Beldum and put it onto your Bench?"):
        return
    await search_to_bench(predicate=_is_beldum, count=1)(ctx)


def _is_beldum(card):
    return (getattr(def_for(card.archetype_id), "display_name", "") or "") == "Beldum"


async def _metal_chain(ctx):
    if getattr(ctx, "energy_receiver", None) is not ctx.source:
        return
    energy = getattr(ctx, "attached_energy", None)
    if energy is None or not energy_provides_type(energy, PokemonTypes.METAL.value):
        return
    if ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return
    if not await ctx.ask_yes_no("Search your deck for Beldum and put it onto your Bench?"):
        return
    await search_to_bench(predicate=_is_beldum, count=1)(ctx)


card = PokemonCardDef(
    guid="4a509e4c-90cb-59ca-9d14-f77157b8842a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=374,
    abilities=[
        Ability(
            title="Metal Chain",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            game_text="Once during your turn (before your attack), when you attach a Metal Energy card from your hand to Beldum (excluding effects of attacks or Pok\u00e9-Powers), you may search your deck for Beldum and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Beldum is affected by a Special Condition.",
            effect=_metal_chain,
        ),
        Attack(
            title="Take Down",
            game_text="Beldum does 10 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)