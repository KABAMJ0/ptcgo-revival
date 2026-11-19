from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack

from ptcgo.game.data_utils import def_for


def _is_pineco_or_forretress(pokemon):
    name = (getattr(def_for(pokemon.archetype_id), "display_name", "") or "").lower()
    return name.startswith("pineco") or name.startswith("forretress")


async def _everyone_explode_now(ctx):
    mine = [p for p in ctx.my_pokemon_in_play() if _is_pineco_or_forretress(p)]
    await ctx.deal_damage(30 * len(mine))
    for pokemon in mine:
        await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)


card = PokemonCardDef(
    guid="3cb9b9b5-ac5d-5706-958a-e315a2c7d16c",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Mirror Shot",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Everyone Explode Now",
            game_text="Does 30 damage times the number of Pineco and Forretress you have in play. This attack does 30 damage to each of your Pineco and Forretress in play.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=_everyone_explode_now,
        ),
    ],
)