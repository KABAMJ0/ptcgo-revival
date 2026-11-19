from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_defender_lock_attack
from ptcgo.game.card_effects.pokemon import is_water_energy
from ptcgo.game.card_effects.support_common import attach_from_discard


async def _critical_collection(ctx):
    """Count the Prizes the opponent has taken, then attach up to that many
    Water Energy from the discard pile to Kyogre Star."""
    taken = ctx.prizes_taken(ctx.opponent_id)
    if taken <= 0:
        await ctx.deal_damage()
        return
    await attach_from_discard(is_water_energy, count=taken, target="self",
                              minimum=0)(ctx)


card = PokemonCardDef(
    guid="061fe370-8185-5365-8d8b-e4bb2e3d6fa8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre ★",
    searchable_by=["Kyogre \u2605", "Basic", "Star", "Kyogre"],
    subtypes=["Basic", "Star"],
    collector_number=112,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Critical Collection",
            game_text="Count the number of Prize cards your opponent has taken. Search your discard pile for up to that many Water Energy cards and attach them to Kyogre Star.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=_critical_collection,
        ),
        Attack(
            title="Sheer Cold",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_defender_lock_attack(),
        ),
    ],
)