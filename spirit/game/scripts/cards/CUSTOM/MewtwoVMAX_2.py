"""Custom test card: Mewtwo VMAX.

Lives in the CUSTOM set so it never collides with real set data. The client gets
its texture from spirit/assets/cards/CUSTOM/MewtwoVMAX_2.png, which the injector
pads to 1024x1024 and packs into an AssetBundle on startup.

Note Mewtwo VMAX does not exist in the real game -- this is deliberately a card
that never shipped, as the first proof that the injection pipeline works.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _psy_purge(ctx):
    """90 damage, then discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None:
        await ctx.discard_energy_from(defender, 1)


async def _star_raid(ctx):
    """160 damage, then discard 2 Energy from this Pokemon."""
    await ctx.deal_damage()
    await ctx.discard_energy_from(ctx.attacker, 2)


card = PokemonCardDef(
    guid="1dbe7830-c6ba-43be-a4e1-5421f3d86a33",
    key="CUSTOM",
    name="Mewtwo VMAX",
    display_name="Mewtwo VMAX",
    searchable_by=["Mewtwo VMAX", "VMAX", "MewtwoVMAX", "Mewtwo"],
    subtypes=["VMAX"],
    collector_number=2,
    set_code="CUSTOM",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="Mewtwo V",
    family_id=150,
    abilities=[
        Attack(
            title="Psy Purge",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=_psy_purge,
        ),
        Attack(
            title="Star Raid",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_star_raid,
        ),
    ],
)
