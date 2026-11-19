from ptcgo.game.card_effects.attacks_common import lock_opponent_evolutions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_EVOLVED_STAGES = ("Stage 1", "Stage 2")


async def _prehistoric_water(ctx):
    candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                  if any(stage in _EVOLVED_STAGES
                         for stage in subtypes_for(pokemon.archetype_id))]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates,
                                      "Choose one of your opponent's evolved Pokémon")
    if target is None:
        return
    results = await ctx.flip_coins(1, "Prehistoric Water")
    if results and results[0]:
        stripped = await ctx.devolve_pokemon(target, steps=1, destination="deck")
        if stripped:
            await ctx.shuffle_deck(ctx.opponent_id)

card = PokemonCardDef(
    guid="8093d8b4-f282-53cb-8777-2ce65b43f042",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOmastar.Name",
    display_name="Dark Omastar",
    searchable_by=["Dark Omastar", "Stage 2", "DarkOmastar"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOmanyte.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Prehistoric Water",
            game_text="If your opponent has any evolved Pok\u00e9mon in play, choose 1 of them and flip a coin. If heads, your opponent takes the highest Stage Evolution card on that Pok\u00e9mon and shuffles it into his or her deck.",
            cost={PokemonTypes.WATER: 1},
            effect=_prehistoric_water,
        ),
        Attack(
            title="Dark Tentacle",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't evolve except from effects of attacks or Pok\u00e9mon Powers. (Benching that Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=lock_opponent_evolutions(defending_only=True),
        ),
    ],
)