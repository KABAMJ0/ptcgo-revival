from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

from ptcgo.game.card_effects.pokemon import is_energy_card

async def jet_sword(ctx):
    """100; discarding 2 Energy also puts 10 on each of the opponent's Benched."""
    await ctx.deal_damage(100)
    discarded = await ctx.discard_energy_from(ctx.attacker, 2)
    if len(discarded) < 2:
        return
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="d8043f0f-b94b-561d-a11f-1a10b8192656",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="POP9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Dragon Rage",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=flip_or_nothing(coins=2),
        ),
        Attack(
            title="Jet Sword",
            game_text="Discard 2 Energy attached to Garchomp and this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=jet_sword,
        ),
    ],
)