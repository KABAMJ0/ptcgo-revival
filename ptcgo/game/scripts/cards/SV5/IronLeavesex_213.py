from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

async def _rapid_vernier(ctx):
    """On the bench play: you may switch this Pokemon with your Active, and if
    you did, move any amount of Energy from your other Pokemon to it."""
    if not await ctx.ask_yes_no(
        "Switch this Pokémon with your Active Pokémon?"
    ):
        return
    if not await ctx.switch_active(ctx.player_id, ctx.source):
        return
    sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    if sources:
        await ctx.move_energy_freely(
            sources, [ctx.source],
            prompt="Choose any number of Energy cards to move to Iron Leaves ex")

card = PokemonCardDef(
    guid="35cc4b58-dcc1-564c-ab43-18b670519606",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronLeavesex.Name",
    display_name="Iron Leaves ex",
    searchable_by=["Iron Leaves ex", "Basic", "ex", "Future", "IronLeavesex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=213,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1010,
    abilities=[
        Ability(
            title="Rapid Vernier",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may switch it with your Active Pok\u00e9mon. If you do, you may move any amount of Energy from your other Pok\u00e9mon to this Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=_rapid_vernier,
        ),
        Attack(
            title="Prism Edge",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=lock_self_attack(),
        ),
    ],
)