from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _fair_weather_heal(ctx):
    """Heal 20 from 1 of my Pokemon that has any Grass Energy attached."""
    pool = [p for p in ctx.my_pokemon_in_play()
            if any(energy_provides_type(e, PokemonTypes.GRASS.value)
                   for e in ctx.attached_energies(p))]
    if not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(
        pool, "Choose a Pok\u00e9mon to heal")
    if target is not None:
        await ctx.heal(20, target)


card = PokemonCardDef(
    guid="ab426822-f9a2-5c7f-8c22-1f5ce3bf65aa",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Fair-Weather Heal",
            game_text="Once during your turn (before your attack), you may heal 20 damage from 1 of your Pok\u00e9mon that has any Grass Energy attached to it.",
            activation=Activations.ONCE_PER_TURN,
            effect=_fair_weather_heal,
        ),
        Attack(
            title="Random Peck",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)