from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def radiating_heat(ctx):
    """20 damage. You may discard an Energy from this Pokémon; if you do,
    discard an Energy from the opponent's Active Pokémon."""
    await ctx.deal_damage()
    if not ctx.attached_energies(ctx.attacker):
        return
    if not await ctx.ask_yes_no("Discard an Energy from this Pokémon?"):
        return
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.defender
    if defender is not None and ctx.attached_energies(defender) \
            and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)

card = PokemonCardDef(
    guid="f1a3c144-d317-5a5b-a7ad-cfb5ea7278f9",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    display_name="Centiskorch V",
    searchable_by=["Centiskorch V", "Basic", "V", "CentiskorchV"],
    subtypes=["Basic", "V"],
    collector_number=14,
    set_code="SWSH11TG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=851,
    abilities=[
        Attack(
            title="Radiating Heat",
            game_text="You may discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=radiating_heat,
        ),
        Attack(
            title="Burning Train",
            cost={PokemonTypes.FIRE: 4},
            damage=180,
        ),
    ],
)