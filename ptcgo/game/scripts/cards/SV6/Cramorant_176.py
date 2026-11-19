from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, snipe_attack

async def gmax_rapid_flow(ctx):
    """Discard all Energy from this Pokémon, then 120 to 2 of the opponent's Pokémon (no W/R on Bench)."""
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Choose Energy to discard from this Pokémon"
    )
    await snipe_attack(120, pool="any", count=2)(ctx)

card = PokemonCardDef(
    guid="027b9707-d225-52d1-ab66-d7e1e75470eb",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic", "Cramorant"],
    subtypes=["Basic"],
    collector_number=176,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=845,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Spit Shot",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=gmax_rapid_flow,
        ),
    ],
)