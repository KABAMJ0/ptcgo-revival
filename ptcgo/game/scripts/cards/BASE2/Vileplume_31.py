from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import AttrID


async def heal_power(ctx):
    """Once during your turn, flip a coin; on heads remove 1 damage counter
    from 1 of your Pokemon."""
    heads = await ctx.flip_coins(1, "Heal")
    if not heads or not heads[0]:
        return
    damaged = [p for p in ctx.my_pokemon_in_play()
               if ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0) > 0]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokemon to heal")
    if target is not None:
        await ctx.heal(10, target=target)

card = PokemonCardDef(
    guid="39ecc5bd-edf2-513e-b075-9d2f8f4f9299",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Heal",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, remove 1 damage counter from 1 of your Pok\u00e9mon. This power can't be used if Vileplume is Asleep, Confused, or Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            effect=heal_power,
        ),
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 40 damage times the number of heads. Vileplume is now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)