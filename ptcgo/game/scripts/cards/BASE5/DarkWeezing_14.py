from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for


def _is_koffing_weezing(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name in ("Koffing", "Weezing", "Dark Weezing")


async def mass_explosion(ctx):
    """20 times the number of Koffings, Weezings and Dark Weezings in play, then
    20 to each of them."""
    everyone = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    family = [p for p in everyone if _is_koffing_weezing(p)]
    await ctx.deal_damage(20 * len(family))
    for pokemon in family:
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="ef218cc0-e53d-50c8-9f49-9c2513579228",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWeezing.Name",
    display_name="Dark Weezing",
    searchable_by=["Dark Weezing", "Stage 1", "DarkWeezing"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Mass Explosion",
            game_text="Does 20 damage times the total number of Koffings, Weezings, and Dark Weezings in play (Apply Weakness and Resistance.). Then, this attack does 20 damage to each Koffing, Weezing, and Dark Weezing (even your own). Don't apply Weakness and Resistance.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=mass_explosion,
        ),
        Attack(
            title="Stun Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned; if tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 3},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True, tails_conditions=(SpecialConditions.PARALYZED,)),
        ),
    ],
)