from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card


def _vortex_fuel(ctx):
    return [card for card in ctx.discard_pile()
            if is_energy_card(card)
            and (energy_provides_type(card, PokemonTypes.WATER.value)
                 or energy_provides_type(card, PokemonTypes.LIGHTNING.value))]


async def dragon_vortex(ctx):
    """20 damage per Water/Lightning Energy card in the discard pile, then
    those same cards shuffle back into the deck."""
    fuel = _vortex_fuel(ctx)
    if fuel:
        await ctx.deal_damage(20 * len(fuel))
    if fuel:
        await ctx.shuffle_into_deck(fuel, ctx.player_id)
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="d8afa93c-a661-50cf-9b63-d0dfd4cf77dc",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=84,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Dragon Vortex",
            game_text="Does 20 damage times the number of Water Energy cards and Lightning Energy cards in your discard pile. Then, shuffle all of those cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=dragon_vortex,
        ),
        Attack(
            title="Tri Bullet",
            game_text="This attack does 30 damage to 3 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(30, pool="any", count=3, apply_modifiers=False),
        ),
    ],
)