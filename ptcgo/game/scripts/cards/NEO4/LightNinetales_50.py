from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, def_for, subtypes_for
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack


def _is_benchable(card):
    if not isinstance(def_for(card.archetype_id), PokemonCardDef):
        return False
    subtypes = subtypes_for(card.archetype_id) or []
    return "Basic" in subtypes or "Baby" in subtypes


async def _guiding_flame(ctx):
    if len(ctx.my_bench()) >= ctx.bench_limit(ctx.player_id):
        return
    candidates = [card for card in ctx.discard_pile() if _is_benchable(card)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Baby or Basic Pok\u00e9mon to put onto your Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="7f2bc2c8-ecae-56ca-a686-d67e77430077",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightNinetales.Name",
    display_name="Light Ninetales",
    searchable_by=["Light Ninetales", "Stage 1", "LightNinetales"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Guiding Flame",
            game_text="Put a Baby Pok\u00e9mon or a Basic Pok\u00e9mon card from your discard pile onto your Bench. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.FIRE: 1},
            effect=_guiding_flame,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy card attached to Light Ninetales in order to use this attack.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE, before_damage=True),
        ),
    ],
)