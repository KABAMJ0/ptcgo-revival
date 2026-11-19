from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_energy_card, energy_provides_type

async def spiral_jet(ctx):
    """Discard 2 Water Energy cards from hand. If you don't, this attack does nothing."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=_is_water_energy_card,
        prompt="Discard 2 Water Energy cards from your hand for Spiral Jet",
    )
    if len(discarded) < 2:
        return
    await ctx.deal_damage()


def _is_water_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER)

card = PokemonCardDef(
    guid="f18c0e45-0d3f-5389-8b59-9b98512444d3",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1", "Barraskewda"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Spiral Jet",
            game_text="Discard 2 Water Energy cards from your hand. If you don't, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=130,
            effect=spiral_jet,
        ),
    ],
)