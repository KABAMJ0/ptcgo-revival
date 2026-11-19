from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import entity_name


async def _tag_team(ctx):
    pokemon = ctx.source
    if pokemon is None or is_in_active_spot(pokemon):
        return
    active = ctx.my_active()
    if active is not None and active is not pokemon:
        await ctx.heal(30, active)
    await ctx.switch_active(ctx.player_id, pokemon)


async def _beatdown(ctx):
    defender = ctx.defender
    dark = defender is not None and (
        "Dark" in entity_name(defender)
        or PokemonTypes.DARKNESS.value in (defender.get_attribute(AttrID.POKEMON_TYPES) or []))
    if dark:
        results = await ctx.flip_coins(1, "Beatdown")
        if results and results[0]:
            await ctx.deal_damage(100)
            return
    await ctx.deal_damage(50)


card = PokemonCardDef(
    guid="207a05eb-1fad-5de7-a29a-2e755b3a6a0e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightMachamp.Name",
    display_name="Light Machamp",
    searchable_by=["Light Machamp", "Stage 2", "LightMachamp"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LightMachoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Tag Team",
            trigger=Triggers.ON_PLAY,
            game_text="When you play Light Machamp from your hand, if it is on your Bench, remove 3 damage counters from your Active Pok\u00e9mon. If it has fewer damage counters than that, remove all of them. Then, switch Light Machamp with your Active Pok\u00e9mon.",
            effect=_tag_team,
        ),
        Attack(
            title="Beatdown",
            game_text="If the Defending Pok\u00e9mon has Dark in its name or is a Darkness Pok\u00e9mon, flip a coin. If heads, this attack does 100 damage instead of 50.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
            effect=_beatdown,
        ),
    ],
)