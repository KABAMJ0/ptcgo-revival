from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import attacks_of


async def _pendulum_influence(ctx):
    coins = await ctx.flip_coins(1, title="Pendulum Influence")
    if not coins or not coins[0]:
        return
    candidates = [(pokemon, attack)
                  for pokemon in ctx.opponent_pokemon_in_play()
                  for attack in attacks_of(pokemon)
                  if getattr(attack, "ability_id", None)]
    if not candidates:
        return
    chosen = await ctx.choose_attack_to_copy(
        candidates,
        "Choose an attack from 1 of your opponent's Pok\u00e9mon")
    if chosen is None:
        return
    await ctx.use_attack(chosen[1], source=chosen[0])


card = PokemonCardDef(
    guid="16e908c4-5f34-5de2-a775-6caf391c3a2c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Pendulum Influence",
            game_text="Flip a coin. If heads, choose an attack from 1 of your opponent's Pok\u00e9mon in play and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_pendulum_influence,
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)