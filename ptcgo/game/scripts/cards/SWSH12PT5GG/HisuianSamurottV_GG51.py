from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack


async def basket_crash(ctx):
    """Discard up to 2 Pokémon Tools from your opponent's Pokémon."""
    tools = [t for t, p in ctx.tools_in_play() if p.owning_player_id == ctx.opponent_id]
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, min(2, len(tools)), minimum=0,
        prompt="Discard up to 2 Pokémon Tools from your opponent's Pokémon.",
    )
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="d96d9554-e503-54c6-9790-369e91621fb1",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottV.Name",
    display_name="Hisuian Samurott V",
    searchable_by=["Hisuian Samurott V", "Basic", "V", "HisuianSamurottV"],
    subtypes=["Basic", "V"],
    collector_number=51,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=503,
    abilities=[
        Attack(
            title="Basket Crash",
            game_text="Discard up to 2 Pok\u00e9mon Tools from your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=basket_crash,
        ),
        Attack(
            title="Shadow Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=180,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)