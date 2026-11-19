from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _rushing_flames(ctx):
    pool = [energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon)
            if energy_provides_type(energy, PokemonTypes.FIRE.value)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Choose any number of Fire Energy cards to discard")
    if not picks:
        return
    await ctx.discard_cards(list(picks))
    results = await ctx.flip_coins(len(picks), "Rushing Flames")
    heads = sum(1 for result in results if result)
    if heads > 0:
        await ctx.deal_damage(40 * heads)

card = PokemonCardDef(
    guid="e46dbeea-cd74-5f71-8678-1c5c3670c677",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyphlosion.Name",
    display_name="Dark Typhlosion",
    searchable_by=["Dark Typhlosion", "Stage 2", "DarkTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkQuilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Claw Swipe",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Rushing Flames",
            game_text="You may discard any number of Fire Energy cards attached to your Pok\u00e9mon. Flip a coin for each Fire Energy card discarded in this way. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="x",
            effect=_rushing_flames,
        ),
    ],
)