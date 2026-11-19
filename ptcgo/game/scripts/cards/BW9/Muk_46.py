from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def sludge_crash(ctx):
    """80 damage, then a coin flipped until tails discards one Energy off the
    Defending Pokemon per heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    defender = ctx.defender
    if heads and defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(
            defender, heads,
            prompt="Choose Energy to discard from the Defending Pok\u00e9mon")

card = PokemonCardDef(
    guid="dfd63c0d-5216-5176-9686-923779e05808",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Team Plasma", "Muk"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=46,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Poison Suction",
            game_text="If the Defending Pok\u00e9mon is Poisoned, heal 60 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Sludge Crash",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=sludge_crash,
        ),
    ],
)