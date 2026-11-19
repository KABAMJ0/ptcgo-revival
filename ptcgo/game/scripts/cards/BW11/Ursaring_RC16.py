from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for
from ptcgo.game.card_effects.support_common import is_energy_card


def _is_teddiursa(card):
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "teddiursa"


async def picnic_weather(ctx):
    """A Teddiursa from the discard pile comes onto your Bench, then an Energy
    card from the discard pile is attached to it."""
    teddiursa = [card for card in ctx.discard_pile() if _is_teddiursa(card)]
    if not teddiursa:
        return
    picked = await ctx.choose_cards(
        teddiursa, 1, minimum=0,
        prompt="Choose a Teddiursa to put onto your Bench")
    if not picked:
        return
    before = {pokemon.entity_id for pokemon in ctx.my_bench()}
    if not await ctx.bench_pokemon(picked[0]):
        return
    benched = next((pokemon for pokemon in ctx.my_bench()
                    if pokemon.entity_id not in before), None)
    if benched is None:
        return
    energies = [card for card in ctx.discard_pile() if is_energy_card(card)]
    if not energies:
        return
    attach = await ctx.choose_cards(
        energies, 1, minimum=0,
        prompt="Choose an Energy card to attach to that Pokémon")
    if attach:
        await ctx.attach_energy(attach[0], benched)


card = PokemonCardDef(
    guid="34a0aa9e-6194-5859-90bd-6843797ddf42",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=1016,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Picnic Weather",
            game_text="Put a Teddiursa from your discard pile onto your Bench. Then, attach an Energy card from your discard pile to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=picnic_weather,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=50),
        ),
    ],
)