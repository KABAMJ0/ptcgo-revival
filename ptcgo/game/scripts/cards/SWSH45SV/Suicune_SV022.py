from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.trainers import is_energy_card

async def ocean_loop(ctx):
    """210 damage, then put 2 Water Energy attached to this Pokémon into your hand."""
    await ctx.deal_damage()
    attached = [c for c in ctx.attached_energies(ctx.source) if _is_water_energy(c)]
    if not attached:
        return
    picks = await ctx.choose_cards(
        attached, 2, prompt="Choose 2 Water Energy to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


def _is_water_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types

card = PokemonCardDef(
    guid="bab5af39-b213-5ca9-bd52-8b610f71a184",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aurora Loop",
            game_text="Put 2 Water Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ocean_loop,
        ),
    ],
)