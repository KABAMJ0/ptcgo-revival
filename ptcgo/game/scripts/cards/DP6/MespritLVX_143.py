from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for, subtypes_for


def _lvx_in_play(ctx, name):
    for pokemon in ctx.my_pokemon_in_play():
        definition = def_for(pokemon.archetype_id)
        if (getattr(definition, "display_name", "") or "").startswith(name) \
                and "Level-Up" in (subtypes_for(pokemon.archetype_id) or []):
            return True
    return False


async def _healing_look(ctx):
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


async def _supreme_blast(ctx):
    if not (_lvx_in_play(ctx, "Uxie") and _lvx_in_play(ctx, "Azelf")):
        return
    await ctx.deal_damage()
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Discard all Energy attached to Mesprit")


card = PokemonCardDef(
    guid="26eedc2b-7976-56d3-98b5-3359c8913236",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MespritLVX.Name",
    display_name="Mesprit LV.X",
    searchable_by=["Mesprit LV.X", "Level-Up", "MespritLVX"],
    subtypes=["Level-Up"],
    collector_number=143,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    family_id=481,
    abilities=[
        Attack(
            title="Healing Look",
            game_text="Remove 3 damage counters from each of your Benched Pok\u00e9mon.",
            cost={},
            effect=_healing_look,
        ),
        Attack(
            title="Supreme Blast",
            game_text="If don't have Uxie LV.X and Azelf LV.X in play, this attack does nothing. Discard all Energy attached to Mesprit.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=200,
            effect=_supreme_blast,
        ),
    ],
)