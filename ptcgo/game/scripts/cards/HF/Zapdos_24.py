from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import (
    is_lightning_energy, is_pokemon_gx, is_pokemon_EX,
)


async def _hurricane_call(ctx):
    results = await ctx.flip_coins(4, "Hurricane Call")
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if is_pokemon_gx(p) or is_pokemon_EX(p)]
    for _ in range(sum(1 for result in results if result)):
        if not candidates:
            break
        picks = await ctx.search_deck(
            is_lightning_energy, count=1, minimum=0,
            prompt="Choose a Lightning Energy card to attach")
        if not picks:
            break
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon-GX or Pokémon-EX to attach it to")
        if target is None:
            target = candidates[0]
        for card in picks:
            await ctx.attach_energy(card, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="020e6697-16bd-51cd-a0e8-dfcc73c2f9ab",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Hurricane Call",
            game_text="Flip 4 coins. For each heads, search your deck for a Lightning Energy card and attach it to 1 of your Pok\u00e9mon-GX or Pok\u00e9mon-EX. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_hurricane_call,
        ),
        Attack(
            title="Sky-High Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
