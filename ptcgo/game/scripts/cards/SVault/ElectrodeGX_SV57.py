from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def crush_and_burn_gx(ctx):
    """Printed 30, then 50 more for each Energy card discarded from your Pokemon."""
    pool = [energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon)]
    discarded = []
    if pool:
        discarded = await ctx.choose_cards(
            pool, len(pool), minimum=0, prompt="Choose any amount of Energy to discard")
        if discarded:
            await ctx.discard_cards(list(discarded))
    await ctx.deal_damage(30 + 50 * len(discarded or []))

card = PokemonCardDef(
    guid="6571cafb-9b11-5e9e-b60b-1a8471f33cf7",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ElectrodeGX.Name",
    display_name="Electrode-GX",
    searchable_by=["Electrode-GX", "Stage 1", "GX", "ElectrodeGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=57,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Extra Energy Bomb",
            game_text="Once during your turn (before your attack), you may attach 5 Energy cards from your discard pile to your Pok\u00e9mon, except Pok\u00e9mon-GX or Pok\u00e9mon-EX, in any way you like. If you do, this Pok\u00e9mon is Knocked Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Crush and Burn-GX",
            game_text="Discard any amount of Energy from your Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=crush_and_burn_gx,
        ),
    ],
)