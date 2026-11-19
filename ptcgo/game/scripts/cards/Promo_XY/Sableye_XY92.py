from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def energy_hunt(ctx):
    """Flip 3 coins; for each heads attach a basic Energy from the discard pile
    to your Benched Pokemon-EX."""
    from ptcgo.game.card_effects.pokemon import is_energy_card, is_pokemon_EX, archetype_id_of
    from ptcgo.game.attributes import AttrID as _Attr
    results = await ctx.flip_coins(3, "Energy Hunt")
    heads = sum(1 for r in results if r)
    bench = [p for p in ctx.my_bench() if is_pokemon_EX(archetype_id_of(p))]
    energies = [c for c in ctx.discard_pile(ctx.player_id)
                if is_energy_card(c) and not bool(c.get_attribute(_Attr.IS_SPECIAL_ENERGY))]
    for _ in range(min(heads, len(energies))):
        if not bench or not energies:
            break
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon-EX")
        if target is None:
            break
        card = (await ctx.choose_cards(energies, 1,
                prompt="Choose a basic Energy from your discard pile"))[0]
        if card is None:
            break
        energies.remove(card)
        await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="f4ade1c1-abc9-54e9-b7dc-8c3d688e1bc1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=302,
    abilities=[
        Attack(
            title="Energy Hunt",
            game_text="Flip 3 coins. For each heads, attach a basic Energy card from your discard pile to your Benched Pok\u00e9mon-EX in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_hunt,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)