from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

async def _tachyon_bits(ctx):
    """On the move to Active: you may put 2 damage counters on 1 opposing Pokemon."""
    if not await ctx.ask_yes_no(
        "Put 2 damage counters on 1 of your opponent's Pokémon?"
    ):
        return
    await ctx.place_damage_counters(2)

card = PokemonCardDef(
    guid="4a574afd-0db6-550f-ad7e-1ba3cf8c3a92",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiantex.Name",
    display_name="Iron Valiant ex",
    searchable_by=["Iron Valiant ex", "Basic", "ex", "Future", "IronValiantex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=225,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Ability(
            title="Tachyon Bits",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=_tachyon_bits,
        ),
        Attack(
            title="Laser Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=lock_self_attack(),
        ),
    ],
)