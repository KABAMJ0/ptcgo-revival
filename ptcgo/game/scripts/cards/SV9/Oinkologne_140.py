from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_defender_attacks


async def tail_whip(ctx):
    """Flip a coin. If heads, the Defending Pokémon can't attack next turn."""
    heads = await ctx.flip_coins(1, "Tail Whip")
    if heads[0]:
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="de554ae8-01d0-56c3-9795-353d1cbb60fc",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1", "Oinkologne"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Aromatic Stomps",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=tail_whip,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)