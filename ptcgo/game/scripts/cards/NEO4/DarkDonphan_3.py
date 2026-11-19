from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import full_stack
from ptcgo.game.card_effects.support_common import opponent_switches


async def _tusk_toss(ctx):
    """Tusk Toss: heads bounces their Active and its stack; tails they switch."""
    bench = ctx.opponent_bench()
    if not bench:
        await ctx.deal_damage()
        return
    heads = await ctx.flip_coins(1, "Tusk Toss")
    defender = ctx.defender
    if heads and all(heads):
        if defender is not None:
            for card in full_stack(defender):
                await ctx.put_in_hand([card], reveal=False)
    else:
        await opponent_switches(ctx)

card = PokemonCardDef(
    guid="76c3f5ee-1184-5f51-b686-5a03c088a15c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDonphan.Name",
    display_name="Dark Donphan",
    searchable_by=["Dark Donphan", "Stage 1", "DarkDonphan"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Tusk Toss",
            game_text="If your opponent has any Benched Pok\u00e9mon, flip a coin. If heads, return the Defending Pok\u00e9mon and all cards attached to it to your opponent's hand. If tails, your opponent chooses 1 of his or her Benched Pok\u00e9mon and switches it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            effect=_tusk_toss,
        ),
        Attack(
            title="Giant Tusk",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)