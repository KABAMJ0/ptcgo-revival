from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.support_common import requires_in_play
from ptcgo.game.session.effects import is_basic_pokemon

async def delicious_aroma(ctx):
    """You may flip a coin; on heads switch an opposing Benched Basic in."""
    if not await ctx.ask_yes_no(
            "Flip a coin to switch 1 of your opponent's Benched Basic "
            "Pokémon with their Active Pokémon?"):
        return
    heads = (await ctx.flip_coins(1, "Delicious Aroma"))[0]
    if not heads:
        return
    candidates = [p for p in ctx.opponent_bench() if is_basic_pokemon(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)

card = PokemonCardDef(
    guid="f0eb43dd-a9b5-5176-b401-fed733adf41b",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1", "Appletun"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Delicious Aroma",
            game_text="Once during your turn, you may flip a coin. If heads, switch 1 of your opponent's Benched Basic Pok\u00e9mon with their Active Pok\u00e9mon.",
            effect=delicious_aroma,
            condition=requires_in_play(is_basic_pokemon, side="opponent"),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)