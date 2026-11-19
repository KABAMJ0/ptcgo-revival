from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.pokemon import is_basic_water_energy


async def riptide(ctx):
    """20 per Basic Water Energy in the discard pile, then shuffle them in."""
    energies = [card for card in ctx.discard_pile() if is_basic_water_energy(card)]
    if not energies:
        return
    await ctx.deal_damage(20 * len(energies))
    await ctx.shuffle_into_deck(energies, ctx.player_id)


card = PokemonCardDef(
    guid="29e3891e-f14a-5b12-abc1-73143ff22fa0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Riptide",
            game_text="This attack does 20 damage for each Basic Water Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=riptide,
        ),
        Attack(
            title="Swirling Waves",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)