from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for


async def _swarming_bites(ctx):
    """Swarming Bites: 20 per Basculin in play onto one of their Bench."""
    count = sum(1 for p in ctx.my_pokemon_in_play()
                if "Basculin" in (_display_name(p) or ""))
    bench = ctx.opponent_bench()
    if not count or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
    if target is not None:
        await ctx.deal_damage(20 * count, target=target, apply_modifiers=False)


def _display_name(entity) -> str:
    """The printed name of a card on the board (empty when unknown)."""
    return getattr(def_for(getattr(entity, "archetype_id", "") or ""),
                   "display_name", "") or ""

card = PokemonCardDef(
    guid="fa7503ef-25c6-571c-9035-21ecb69cf5a2",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name",
    display_name="Basculin",
    searchable_by=["Basculin", "Basic", "Basculin"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=550,
    abilities=[
        Attack(
            title="Swarming Bites",
            game_text="This attack does 20 damage for each Basculin you have in play to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_swarming_bites,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)