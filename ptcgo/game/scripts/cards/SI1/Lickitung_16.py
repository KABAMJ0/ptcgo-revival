from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def lick_wounds(ctx):
    results = await ctx.flip_coins(1, "Lick Wounds")
    if not results or not results[0]:
        return 0
    candidates = [pokemon
                  for pokemon in list(ctx.my_pokemon_in_play())
                  + list(ctx.opponent_pokemon_in_play())
                  if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)]
    if not candidates:
        return 0
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 Pokémon with damage counters on it.")
    if target is None:
        return 0
    return await ctx.heal(20, target)

card = PokemonCardDef(
    guid="0738d786-1cc8-53a4-ad40-51606c731d8c",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=108,
    abilities=[
        Attack(
            title="Lick Wounds",
            game_text="Flip a coin. If heads, choose 1 Pok\u00e9mon (yours or your opponent's) with damage counters on it and remove 2 damage counters from it (1 if it only has 1).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lick_wounds,
        ),
        Attack(
            title="Tongue Stretch",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)